//#define DLOG

#include "series.hpp"

#include "libfspp.hpp"

#include "search.hpp"
#include "graphics.hpp"
#include "busy_indicator.hpp"
#include "shutdown.hpp"
#include "touch.hpp"
#include "rand.hpp"

#include "Movie_info.h"

#include "boost.hpp"
// ostringstream
#include <sstream>
#include <fstream>

#include <assert.h>

using std::string;
using std::vector;
using std::list;

Series::Series()
  : SerieDB("seriehd.db", true), scanning(false), view_new_episodes(false), in_series(true), update_needed(true),
				 pos_serie(0), pos_season(0), pos_episode(0)
{
/*  if (!recurse_mkdir(conf->p_var_data_dir(),"movies", &imdb_dir))
    print_critical(dgettext("mms-movie", "Could not create directory ") + imdb_dir, "MOVIE"); */

  ext_mask = file_tools::create_ext_mask(movie_conf->p_filetypes_m());
  visible = false;
}

void Series::startup_updater()
{
/* #ifndef use_ffmpeg_thumbnailer
  Plugins *plugins = S_Plugins::get_instance();
  thumbnailer = plugins->find(plugins->movie_players, "MPlayer");

  if (thumbnailer == 0)
    std::cerr << "Warning, thumbnailer not found, please install mplayer plugin" << std::endl;
#endif */

  set_folders();

  S_BackgroundUpdater::get_instance()->run_once(boost::bind(&Series::scan, this));
  S_BackgroundUpdater::get_instance()->run_once(boost::bind(&Series::getUpdates, this));

  /* S_Search::get_instance()->register_module(SearchModule(dgettext("mms-movie", "Series"),
							 boost::bind(&Series::gen_search_list, this, _1),
							 boost::bind(&Series::reenter, this, _1))); */
  Movie::startup_updater();

  list_font_small = graphics::resolution_dependant_font_wrapper(12, conf);

}

void Series::action_random()
{
    Rand *rand = S_Rand::get_instance();
    pos_episode = rand->number(episode.size());
    update_needed = true;
    input_master->add_input(Input("action", ""), ""); // send signal to play selected episode 
}

void Series::action_play()
{
  if (episode.size() == 0)
	return; 
  string filename = vector_lookup(episode, pos_episode).filename;
  MyPair filetype = check_type(filename, movie_conf->p_filetypes_m());
  Multifile e = addfile(filename, filetype);
  Multifile m = Multifile(e);
  playmovie(e);
  if (vector_lookup(episode, pos_episode).viewed == 0 && filesystem::getFileSize(filename) > 0) {
    setViewed(vector_lookup(episode, pos_episode).id); // update DB
	episode[pos_episode].viewed = 1; // update vector episode
	if (!view_new_episodes) {
    	series[pos_serie].unviewed -= 1; // update Vector series
	}
  }
}

string Series::cover_path(const string& name) const
{
  // Try to find a cover in the movie folder to enable users to overwrite the
  // imdb cover
/*  string cover = find_cover_in_current_dir();

  if (!cover.empty())
    return cover;
  else */
    // cover not found in directory of movie, use the one from imdb
    //std::cout << "cover_path(" << name <<") " << imdb_dir << name << "_cover.jpg" << std::endl;
    return imdb_dir + name + "_cover.jpg";
}

string Series::banner_path(const string& name) const
{
  // Try to find a cover in the movie folder to enable users to overwrite the
  // imdb cover
/*  string cover = find_cover_in_current_dir();

  if (!cover.empty())
    return cover;
  else */
    // cover not found in directory of movie, use the one from imdb
    //std::cout << "banner_path(" << name <<") " << imdb_dir <<  string_format::lowercase_utf(name) << "_banner.jpg" << std::endl;
    return serie_dir + string_format::lowercase_utf(name) + "_banner.jpg";
}

string Series::fanart_path(const string& name) const
{
  // Try to find a cover in the movie folder to enable users to overwrite the
  // imdb cover
/*  string cover = find_cover_in_current_dir();

  if (!cover.empty())
    return cover;
  else */
    // cover not found in directory of movie, use the one from imdb
    //std::cout << "banner_path(" << name <<") " << imdb_dir <<  string_format::lowercase_utf(name) << "_banner.jpg" << std::endl;
    return serie_dir + string_format::lowercase_utf(name) + "_fanart.jpg";
}

void Series::scan()
{
  scanning = true;
  check_db_consistency();
  check_for_changes();
  series = getSeries();
  loaded_correctly = true;
  scanning = false;
}

std::vector<std::pair<std::string, int> > Series::gen_search_list(const std::string& search_word)
{
  string parent = "", movie_parent = "";

  if (input_master->current_saved_map() == "movie" && search_depth == dgettext("mms-movie", "current folder")) {
    string parent_sql_str = "SELECT id FROM %t WHERE";

    list<string> current_folders = folders.top().first;
    bool first = true;
    foreach (string& folder, current_folders) {
      if (first) {
	parent_sql_str += " filename='" + folder + "'";
	first = false;
      } else
	parent_sql_str += " OR filename='" + folder + "'";
    }

    string parent_ids = "";

    db_mutex.enterMutex();

    SQLQuery *q0 = db.query("Folders", parent_sql_str.c_str());

    if (q0) {
      for (int i = 0; i < q0->numberOfTuples(); ++i) {
	SQLRow &row = (*q0)[i];
	if (i > 0)
	  parent_ids += ", " + row["id"];
	else
	  parent_ids += row["id"];
      }
    }
    delete q0;

    db_mutex.leaveMutex();

    parent = "parent in (" + parent_ids + ") AND";
    movie_parent = "path = (SELECT filename FROM Folders WHERE parent in (" + parent_ids + ")) AND";
  }

  std::vector<std::pair<std::string, int> > result;
  vector<int> ids_already_found;

  db_mutex.enterMutex();

  // folders
  SQLQuery *q = db.query("Folders", ("SELECT id, parent, filename, name, is_folder FROM %t WHERE " + parent + " fuzzycmp('" + search_word + "', lname, 1)").c_str());

  if (q) {

    for (int i = 0; i < q->numberOfTuples(); ++i) {

      SQLRow &row = (*q)[i];

      string out;

      bool result_ok = false;

      if (input_master->current_saved_map() == "movie" && search_depth == dgettext("mms-movie", "current folder")) {
	foreach (string& folder, folders.top().first)
	  if (row["filename"].find(folder) != string::npos) {
	    result_ok = true;
	    break;
	  }
      } else
	result_ok = true;

      if (result_ok && row["parent"] != "0") {
	if (row["is_folder"] == "1")
	  out = row["name"] + "/";
	else
	  out = row["name"];

	int id = conv::atoi(row["id"]);
	result.push_back(std::make_pair(string_format::convert(out), id));
	ids_already_found.push_back(id);
      }
    }
  }
  delete q;

  q = db.query("HDMovie", ("SELECT path, title, Folders.id as id FROM %t, Folders WHERE " + movie_parent + " fuzzycmp('" + search_word + "', ltitle, 1) AND Folders.filename = HDMovie.path").c_str());
  if (q) {
    for (int i = 0; i < q->numberOfTuples(); ++i) {

      SQLRow &row = (*q)[i];

      int id = conv::atoi(row["id"]);

      bool found_match = false;
      foreach (int id_already_found, ids_already_found)
	if (id == id_already_found) {
	  found_match = true;
	  break;
	}

      if (!found_match)
	result.push_back(std::make_pair(row["title"], id));
    }
  }
  delete q;

  db_mutex.leaveMutex();

  return result;
}

// commands
void Series::secondary_menu()
{
  ExtraMenu em;

  if (in_series && !view_new_episodes) {
    em.add_item(ExtraMenuItem(dgettext("mms-movie", "Enter serie"), input_master->find_shortcut("action"),
			      boost::bind(&Series::enter_serie, this)));
  
    em.add_item(ExtraMenuItem(dgettext("mms-movie", "Play all files in dir"), input_master->find_shortcut("play_movie"),
			      boost::bind(&Series::action_play, this)));
  } else {
    em.add_item(ExtraMenuItem(dgettext("mms-movie", "Play movie"), input_master->find_shortcut("action"),
			      boost::bind(&Series::action_play, this)));
    em.add_item(ExtraMenuItem(dgettext("mms-movie", "Random play movie"), input_master->find_shortcut("play_movie"),
			      boost::bind(&Series::action_random, this)));
    em.add_item(ExtraMenuItem(dgettext("mms-movie", "Toggle viewed"), input_master->find_shortcut("reget"),
			      boost::bind(&Series::toggle_viewed, this)));

  }

  /* if (!vector_lookup(files, folders.top().second).m_strTitle.empty()) {
    em.add_item(ExtraMenuItem(dgettext("mms-movie", "Update imdb information"), 
			      input_master->find_shortcut("reget"),
			      boost::bind(&Series::reget_movie_information, this)));

    em.add_item(ExtraMenuItem(dgettext("mms-movie", "Delete imdb information"),
			      input_master->find_shortcut("delete_file_info"),
			      boost::bind(&Series::remove_from_db, this,
					  folders.top().second)));
  } else {
    em.add_item(ExtraMenuItem(dgettext("mms-movie", "Get information on imdb"), 
			      input_master->find_shortcut("reget"),
			      boost::bind(&Series::reget_movie_information, this)));
  } */

/*  if (vector_lookup(files, folders.top().second).type == "file")
    em.add_item(ExtraMenuItem(dgettext("mms-movie", "Print file information"), input_master->find_shortcut("print_file_info"),
			      boost::bind(&Series::print_movie_info, this)));

  em.add_item(ExtraMenuItem(dgettext("mms-movie", "Print imdb information"), input_master->find_shortcut("info"),
			    boost::bind(&Series::print_info, this))); */

  /* if (folders.size() > 1) {
    em.add_item(ExtraMenuItem(dgettext("mms-movie", "Go up one directory"), input_master->find_shortcut("back"),
			      boost::bind(&Series::go_back, this)));
    em.add_item(ExtraMenuItem(dgettext("mms-movie", "Return to startmenu"), input_master->find_shortcut("startmenu"),
			      boost::bind(&Series::exit, this)));
  } else
    em.add_item(ExtraMenuItem(dgettext("mms-movie", "Return to startmenu"), input_master->find_shortcut("back"),
			      boost::bind(&Series::exit, this)));
*/
  add_standard(em);

  foreach (ExtraMenuItem& item, global->menu_items)
    em.add_persistent_item(item);

  conf->s_sam(true);

  em.mainloop();
}

void Series::check_for_changes()
{
  std::cout << "Series::check_for_changes()" << std::endl;

  std::stack<string> queued_dirs;

  foreach (string& dir, serie_folders)
    queued_dirs.push(dir);

  while (!queued_dirs.empty()) {
    string cur_dir = queued_dirs.top();
    queued_dirs.pop();

    for (file_iterator<file_t, default_order> i (cur_dir); i != i.end (); i.advance(false)) {

      string cur_file = string_format::remove_doubles(i->getName());
	  std::cout << "check_for_changes() checking " << cur_file << std::endl;
      if (isDirectory(cur_file)) {
	  std::cout << "check_for_changes() dir queued " << cur_file << std::endl;
	//insert_file_into_db(cur_file, cur_dir, db);
		queued_dirs.push(cur_file);
  	   } else {
		std::cout << "check_for_changes() file " << cur_file << std::endl;
		if (!(check_type(cur_file, movie_conf->p_filetypes_m()) == emptyMyPair)) 
			insert_file_into_db(cur_file);
		else if (!(check_type(cur_file, movie_conf->p_filetypes_d()) == emptyMyPair))
			S_BackgroundUpdater::get_instance()->run_once(boost::bind(&SerieDB::parseXML, this, cur_file));
		//parseXML(cur_file);
	  }
    }
  }
}

void Series::prev()
{
  int size = (in_series && !view_new_episodes ? series.size() : episode.size());
  int pos = (in_series && !view_new_episodes ? pos_serie : pos_episode);

  if (pos != 0)
    --pos;
  else
    pos = size -1;

  if (in_series && !view_new_episodes) { 
	pos_serie = pos; 
	pos_episode = 0; 
  } else 
	pos_episode = pos;
}

void Series::next()
{
  int size = (in_series && !view_new_episodes ? series.size() : episode.size());
  int pos = (in_series && !view_new_episodes ? pos_serie : pos_episode);

  if (pos != size -1)
    ++pos;
  else
    pos = 0;

  if (in_series && !view_new_episodes) { 
	pos_serie = pos; 
	pos_episode = 0; 
  } else 
	pos_episode = pos;
}

void Series::left()
{
  if (in_series) {
	if (view_new_episodes) {
	view_new_episodes = false;
    series = getSeries();

  int curlayer = render->device->get_current_layer();
  render->device->animation_section_begin();
  render->device->switch_to_layer(curlayer);
  render->device->reset_layout_attribs_nowait();
  render->device->set_layout_alpha(0.0, curlayer+1);
  render->device->animation_fade(0,1,40,curlayer);
  render->device->animation_fade(1,0,80,curlayer+1);
  render->device->animation_section_end();


//  int curlayer = render->device->get_current_layer();
//  std::cout << "left: curlayer = " << (curlayer ) << std::endl;
//  render->device->animation_section_begin();
//  render->device->switch_to_layer(curlayer-1);
//  render->device->reset_layout_attribs_nowait();
//  render->device->animation_move(0, 0, conf->p_h_res(), 0,  60, curlayer);
//  render->device->animation_move(-conf->p_h_res(), 0, 0, 0, 60, curlayer-1);
//  render->device->animation_fade(1,0,100,curlayer);
//  render->device->animation_fade(0,1,100,curlayer-1);

  }
	return;
  }

  if (pos_season != 0)
    --pos_season;
  else
    pos_season = seasons.size() -1;
  pos_episode = 0;
  show_serie();
}

void Series::right()
{
  if (in_series) {
	if (!view_new_episodes) {
	view_new_episodes = true;
	episode = getUnviewEpisodes();
	pos_episode = 0;

  int curlayer = render->device->get_current_layer();
  render->device->animation_section_begin(true);
  render->device->switch_to_layer(curlayer);
  render->device->reset_layout_attribs_nowait();
  render->device->set_layout_alpha(0.0, curlayer+1);
  render->device->animation_fade(0,1,80,curlayer);
  render->device->animation_fade(1,0,40,curlayer+1);
  render->device->animation_section_end();


//  render->device->animation_section_begin(true);
//  int curlayer = render->device->get_current_layer();
//  render->device->switch_to_layer(curlayer+1);
//  render->device->reset_layout_attribs_nowait();
//  std::cout << "right: newLayer = " << (curlayer + 1) << std::endl;

//  render->device->set_layout_alpha(0.0, curlayer+1);
//  render->device->animation_move(conf->p_h_res(), 0, 0, 0, 60, curlayer+1);
//  render->device->animation_move(0, 0, -conf->p_h_res(), 0, 60, curlayer);
//  render->device->animation_fade(0,1,100,curlayer+1);
//  render->device->animation_fade(1,0,100,curlayer);

//  render->device->set_layout_alpha(0.0, curlayer+1);
//  render->device->animation_fade(0,1,80,curlayer);
//  render->device->animation_fade(1,0,40,curlayer+1);
  render->device->animation_section_end();
  }
  return;
  }

  if (pos_season != seasons.size() -1)
    ++pos_season;
  else
    pos_season = 0; 
  pos_episode = 0;
  show_serie();
}

void Series::page_up()
{

  int jump = conf->p_jump();
  int size = (in_series && !view_new_episodes ? series.size() : episode.size());
  int pos = (in_series ? pos_serie : pos_episode);

  if (size > jump) {
    int diff = pos - jump;
    if (pos == 0)
      pos = (size -1 ) + diff;
    else if (diff < 0)
      pos = 0;
    else
      pos = diff;
  }

  if (in_series && !view_new_episodes) 
    pos_serie = pos; 
  else 
    pos_episode = pos;

}

void Series::page_down()
{
  int jump = conf->p_jump();
  int size = (in_series && !view_new_episodes ? series.size() : episode.size());
  int pos = (in_series && !view_new_episodes ? pos_serie : pos_episode);

  if (size > jump) {
    if (pos > (size - jump) && pos != (size - 1))
      pos = size - 1;
    else
      pos = (pos + jump) % size;
  }

  if (in_series && !view_new_episodes) 
    pos_serie = pos; 
  else 
    pos_episode = pos;

}

void Series::toggle_viewed()
{
  
  if (in_series && !view_new_episodes) {
  } else {
    bool stat = vector_lookup(episode, pos_episode).viewed;
    setViewed(vector_lookup(episode, pos_episode).id, !stat);
    episode[pos_episode].viewed = !stat; // update vector episode
    series[pos_serie].unviewed += (!stat ? -1 : 1); // update Vector series
  }
}


void Series::enter_serie() 
{
	in_series = false;

  int curlayer = render->device->get_current_layer();
  render->device->animation_section_begin(true);
  render->device->switch_to_layer(curlayer);
  render->device->reset_layout_attribs_nowait();
  render->device->set_layout_alpha(0.0, curlayer+1);
  render->device->animation_fade(0,1,80,curlayer);
  render->device->animation_fade(1,0,40,curlayer+1);
  render->device->animation_section_end();

  show_serie();
}

void Series::show_serie() 
{
	int id =  vector_lookup(series, pos_serie).id;
        seasons = getSeasons(id);
        if (pos_season  > seasons.size()) pos_season = 0;
        string season = vector_lookup(seasons, pos_season).label;

        string filter;
	if (season == dgettext("mms-movie", "all"))
	  filter = "";
	else if  (season == dgettext("mms-movie", "unviewed"))
	  filter = "viewed = 0";
	else if  (season == dgettext("mms-movie", "viewed"))
	  filter = "viewed = 1";
	else
          filter = "season = '" + season + "'";

	episode = getEpisodes(id,  filter);
        if (pos_episode > episode.size()) pos_episode = 0;
	update_needed = true;

}

void Series::leave_serie() {
	update_needed = true;
	in_series = true;
        pos_season = 0;
        pos_episode = 0;

  int curlayer = render->device->get_current_layer();
  render->device->animation_section_begin();
  render->device->switch_to_layer(curlayer);
  render->device->reset_layout_attribs_nowait();
  render->device->set_layout_alpha(0.0, curlayer+1);
  render->device->animation_fade(0,1,40,curlayer);
  render->device->animation_fade(1,0,80,curlayer+1);
  render->device->animation_section_end();
}

void Series::updated_db() {
  if (scanning)
    return;

  if (series.size() == 0) 
	  return;

  string serie_str = vector_lookup(series, pos_serie).name;
  pos_serie = 0;
  series = getSeries();
  for (int i = 0; i < series.size(); ++i) {
   	if (serie_str == vector_lookup(series, i).name) {
		pos_serie = i;
		break;
	}
  }
  if (!in_series) {

    int id = vector_lookup(series, pos_serie).id;
    string season_str = vector_lookup(seasons, pos_season).label;
    pos_season = 0; 
    seasons = getSeasons(id);
    for (int i = 0; i < seasons.size(); ++i) {
   	if (season_str == vector_lookup(seasons, i).label) {
		pos_season = i;
		break;
	}
    }

    string season = vector_lookup(seasons, pos_season).label;
    int id_ep = vector_lookup(episode, pos_episode).id;
    pos_episode = 0;
    episode = getEpisodes(id, season != dgettext("mms-movie", "all") ? season : "");
    for (int i = 0; i < episode.size(); ++i) {
   	if (id_ep == vector_lookup(episode, i).id) {
		pos_episode = i;
		break;
	}
    }
    show_serie();
  }

  if (visible)
    input_master->add_input(Input(), "");
}

string Series::mainloop()
{
  visible = true;

  BusyIndicator *busy_indicator = S_BusyIndicator::get_instance();
  Shutdown *sd = S_Shutdown::get_instance();

  input_master->set_map("movie");

  Input input;

  update_needed = true;

  render->device->animation_section_begin(true);
  int curlayer = render->device->get_current_layer();
  render->device->switch_to_layer(curlayer+1);
  render->device->reset_layout_attribs_nowait();
  render->device->set_layout_alpha(0.0, curlayer+1);
  render->device->animation_zoom(3,3,1,1,40,curlayer+1);
  render->device->animation_fade(0,1,50,curlayer+1);
  render->device->animation_fade(1,0,50,curlayer);
  render->device->animation_section_end();

  while (!exit_loop)
    {
      /*if (reload_dirs) {
	reload_current_dirs();
	update_needed = true;
	reload_dirs = false;
	if (exit_loop)
	  break;
      }*/

      if (update_needed) {
	if (view_new_episodes)
  	  print(episode);
	else if (in_series)
  	  print(series);
	else 
	  print(episode);
	print_lcd_menu();
      }

      input = input_master->get_input_busy_wrapped(busy_indicator);

      if (sd->is_enabled()) {
	sd->cancel();
	continue;
      }

      update_needed = true;

      if (input.key == "touch_input") {
	S_Touch::get_instance()->run_callback();
	continue;
      }

      if (fullscreen_check(input))
	continue;

      if (input.command == "prev")
 	{
	    prev();
 	}
      else if (input.command == "next")
 	{
            next();
 	}
      else if (input.command == "left")
	{
	    left();
	}
      else if (input.command == "right")
	{
	    right();
	}
      else if (input.command == "page_up")
	{
	    page_up();
	}
      else if (input.command == "page_down")
	{
	    page_down();
	}
      else if (input.command == "reget")
	{
 	   toggle_viewed();
	}
      else if (input.command == "search_imdb")
	{
	  //search_imdb();
	}
      else if (input.command == "info" && input.mode == "graphical")
	{
	  //print_info();
	}
      else if (input.command == "print_file_info")
	{
	  //print_movie_info();
	}
      else if (input.command == "action")
	{
	  if (in_series && !view_new_episodes)
	     enter_serie();
	  else
	     action_play();
	}
      else if (input.command == "play_movie")
	{
	  if (!in_series) // FIXME action random with any serie ?
	    action_random();
	}
      else if (input.command == "search")
	{
	  search_func();
        }
      else if (input.command == "second_action")
	{
	  secondary_menu();
	}
      else if(input.command == "back")
      {
        if(in_series)
            exit();
         else
            leave_serie();
      }
      else if (input.command == "startmenu" && input.mode == "general")
        {
	   exit();
        }
      else
	MovieTemplate<Multifile>::movie_mainloop_common(input);

      update_needed = !global->check_commands(input);
    }

 // int lastlayer = (view_new_episodes ? 2 : 1);

//  std::cout << "main: newLayer = " << (curlayer + lastlayer) << std::endl;
  render->device->animation_section_begin();
  render->device->switch_to_layer(curlayer);
  render->device->reset_layout_attribs_nowait();
  render->device->animation_fade(0,1,80,curlayer);
  render->device->animation_zoom(1,1,4,4,40,curlayer+1);
  render->device->animation_fade(1,0,40,curlayer+1);
  render->device->animation_section_end();

  exit_loop = false;

  visible = false;

  return "";
}

void Series::print(const std::vector<Serie>& cur_files)
{
  render->prepare_new_image();

  render->current.add(new PObj(themes->movie_background, 0, 0, 0, SCALE_FULL));

  std::pair<int, int> header_size = string_format::calculate_string_size("abcltuwHPMjJg", header_font);
  int header_box_size = static_cast<int>(header_size.second * 0.75);

  render->current.add(new PFObj(themes->startmenu_movie_dir, 25, 10, header_box_size, header_box_size, 2, true));

  if (themes->show_header) {

    string header = dgettext("mms-movie", "Series");

    if (folders.size() > 1) {
      string top_folder = folders.top().first.front();

      if (top_folder[top_folder.size()-1] == '/')
	top_folder = top_folder.substr(0, top_folder.size()-1);

      assert(top_folder.rfind('/') != string::npos);
      header += " - " + top_folder.substr(top_folder.rfind('/')+1);
      string_format::format_to_size(header, header_font, conf->p_h_res()-220, false);
    }

    std::pair<int, int> header_size = string_format::calculate_string_size(header, header_font);

    render->current.add(new TObj(header, header_font, 100, (70-header_size.second)/2,
				 themes->movie_header_font1, themes->movie_header_font2,
				 themes->movie_header_font3, 2));
  }

  if (search_mode) {
    int y = 10 + header_box_size + 10;

    std::pair<int, int> search_text_size = string_format::calculate_string_size("abcltuwHPMjJg", search_font);
    int search_size = static_cast<int>(search_text_size.second * 0.75);

    if (offset == -1)
      render->current.add(new RObj(0, y, conf->p_h_res(), search_size + 5, 0, 0, 0, 215, 2));
    else
      render->current.add(new RObj(0, y, conf->p_h_res(), search_size + 5,
				   themes->general_search_rectangle_color1,
				   themes->general_search_rectangle_color2,
				   themes->general_search_rectangle_color3,
				   themes->general_search_rectangle_color4, 2));
    
    render->current.add(new PFObj(themes->general_search, 47, y, search_size, search_size, 3, true));
    
    std::pair<int, int> search_select_sizes = string_format::calculate_string_size(search_depth, search_select_font);

    int max_x = conf->p_h_res()-search_select_sizes.first - 25;

    string sw = search_str;

    string s = dgettext("mms-movie", "Search: ");
    int x_size = string_format::calculate_string_width(s, search_font);
    string_format::format_to_size(sw, search_font, max_x-x_size, true);

    int search_text_height = string_format::calculate_string_size(s + sw, search_font).second;

    render->current.add(new TObj(s + sw, search_font, 47 + search_size + 10,
				 y + (search_size + 5 - search_text_height)/2,
				 themes->search_font1, themes->search_font2, themes->search_font3, 3));
  }

  if (cur_files.size() > 0) {
    int pos = folders.top().second;
    if (search_mode && cur_files.size() > 0)
        pos = offset % cur_files.size();

    print_range<Serie>(cur_files, vector_lookup(cur_files, pos_serie), pos_serie,
			   boost::bind(&Series::print_serie_element, this, _1, _2, _3), list_font_height * 2);
  }

   std::ostringstream pos;

  if (search_mode)
    if (cur_files.size() > 0)
      pos << (offset % cur_files.size()) + 1 << "/" << cur_files.size();
    else
      pos << "";
  else
    pos << pos_serie + 1 << "/" << cur_files.size();

  int x = string_format::calculate_string_width(pos.str(), position_font);

  render->current.add(new TObj(pos.str(), position_font, conf->p_h_res()-(60+x), 20,
			       themes->movie_font1, themes->movie_font2,
			       themes->movie_font3, 3));

  render->draw_and_release("serie");
}

void Series::print(const std::vector<Episode>& cur_files)
{
  render->prepare_new_image();

  string fanart;
  if (!view_new_episodes)
	fanart = fanart_path(vector_lookup(series, pos_serie).name);

  if (file_exists(fanart)) {
      render->create_scaled_image_wrapper_crop_upscaled(fanart, conf->p_h_res(), conf->p_v_res());
      render->current.add(new PFObj(fanart, 0, 0, conf->p_h_res(), conf->p_v_res(), false, 0));    
  } else 
    render->current.add(new PObj(themes->movie_background, 0, 0, 0, SCALE_FULL));

  std::pair<int, int> header_size = string_format::calculate_string_size("abcltuwHPMjJg", header_font);
  int header_box_size = static_cast<int>(header_size.second * 0.75);

  render->current.add(new PFObj(themes->startmenu_movie_dir, 25, 10, header_box_size, header_box_size, 2, true));

  if (themes->show_header) {

    string header = string(dgettext("mms-movie", "Series")) + " - " 
		+ (view_new_episodes ? string(dgettext("mms-movie", "New Episodes")) : vector_lookup(series, pos_serie).name);

    if (folders.size() > 1) {
      string top_folder = folders.top().first.front();

      if (top_folder[top_folder.size()-1] == '/')
	top_folder = top_folder.substr(0, top_folder.size()-1);

      assert(top_folder.rfind('/') != string::npos);
      header += " - " + top_folder.substr(top_folder.rfind('/')+1);
      string_format::format_to_size(header, header_font, conf->p_h_res()-220, false);
    }

    std::pair<int, int> header_size = string_format::calculate_string_size(header, header_font);

    render->current.add(new TObj(header, header_font, 100, (70-header_size.second)/2,
				 themes->movie_header_font1, themes->movie_header_font2,
				 themes->movie_header_font3, 2));
  } 

  int season_size = 0;
  if (search_mode) {
    int y = 10 + header_box_size + 10;

    std::pair<int, int> search_text_size = string_format::calculate_string_size("abcltuwHPMjJg", search_font);
    int search_size = static_cast<int>(search_text_size.second * 0.75);

    if (offset == -1)
      render->current.add(new RObj(0, y, conf->p_h_res(), search_size + 5, 0, 0, 0, 215, 2));
    else
      render->current.add(new RObj(0, y, conf->p_h_res(), search_size + 5,
				   themes->general_search_rectangle_color1,
				   themes->general_search_rectangle_color2,
				   themes->general_search_rectangle_color3,
				   themes->general_search_rectangle_color4, 2));
    
    render->current.add(new PFObj(themes->general_search, 47, y, search_size, search_size, 3, true));
    
    std::pair<int, int> search_select_sizes = string_format::calculate_string_size(search_depth, search_select_font);

    int max_x = conf->p_h_res()-search_select_sizes.first - 25;

    string sw = search_str;

    string s = dgettext("mms-movie", "Search: ");
    int x_size = string_format::calculate_string_width(s, search_font);
    string_format::format_to_size(sw, search_font, max_x-x_size, true);

    int search_text_height = string_format::calculate_string_size(s + sw, search_font).second;

    render->current.add(new TObj(s + sw, search_font, 47 + search_size + 10,
				 y + (search_size + 5 - search_text_height)/2,
				 themes->search_font1, themes->search_font2, themes->search_font3, 3));
  } else {
    int y = 10 + header_box_size + 10;

    std::pair<int, int> search_text_size = string_format::calculate_string_size("abcltuwHPMjJg", list_font);
    season_size = static_cast<int>(search_text_size.second * 0.75);

    if (offset == -1)
      render->current.add(new RObj(0, y, conf->p_h_res(), season_size + 5, 0, 0, 0, 215, 2));
    else
      render->current.add(new RObj(0, y, conf->p_h_res(), season_size + 5,
				   themes->general_search_rectangle_color1,
				   themes->general_search_rectangle_color2,
				   themes->general_search_rectangle_color3,
				   themes->general_search_rectangle_color4, 2));
        
    std::pair<int, int> search_select_sizes = string_format::calculate_string_size(search_depth, list_font);

    int max_x = conf->p_h_res()-search_select_sizes.first - 25;

    string sw = search_str;

	if (!view_new_episodes) {
		string s = dgettext("mms-movie", "Season: ");
		int x_size = string_format::calculate_string_width(s, list_font);
		string_format::format_to_size(sw, list_font, max_x-x_size, true);

		int search_text_height = string_format::calculate_string_size(s + sw, search_font).second;

		render->current.add(new TObj(s + sw, list_font, 60,
					 y + (season_size - list_font_height)/2,
					 themes->movie_font1, themes->movie_font2, themes->movie_font3, 3));

		print_season_range(seasons, vector_lookup(seasons, pos_season), pos_season, 30, x_size - 5);
	}

  }

  if (cur_files.size() > 0) {
    int pos = folders.top().second;
    if (search_mode && cur_files.size() > 0)
        pos = offset % cur_files.size();

    print_range<Episode>(cur_files, vector_lookup(cur_files, pos_episode), pos_episode,
			   boost::bind(&Series::print_episode_element, this, _1, _2, _3), list_font_height * 2, season_size + 10);
  }

   std::ostringstream pos;

  if (search_mode)
    if (cur_files.size() > 0)
      pos << (offset % cur_files.size()) + 1 << "/" << cur_files.size();
    else
      pos << "";
  else
    pos << pos_episode + 1 << "/" << cur_files.size();

  int x = string_format::calculate_string_width(pos.str(), position_font);

  render->current.add(new TObj(pos.str(), position_font, conf->p_h_res()-(60+x), 20,
			       themes->movie_font1, themes->movie_font2,
			       themes->movie_font3, 3));

  render->draw_and_release("episodes");
}

// print a video element
void Series::print_episode_element(const Episode& r, const Episode& position, int y)
{
  string name = (view_new_episodes ?  r.serie : r.title);
  if (name == "NULL") name = "";

  string ep = string_format::double_zero(r.season) + "x" + string_format::double_zero(r.episode)
		 + (view_new_episodes ?   " - " + r.title  : "");
/*  if (r.type != "file")
    name += "/"; */

  string_format::format_to_size(name, list_font, conf->p_h_res()-75-155, true);
  int lvl= 3, img_x = 80, w = 80, h = list_font_height * 2;

  if (r == position) {
    render->current.add(new PFObj(themes->general_marked_large, 60, y+2,
				  conf->p_h_res()-2*60, list_font_height * 2, 2, true));

      lvl++;
      img_x = 95;
      w = 120;
      h = list_font_height * 3;


  }

  if (file_exists(cover_path(r.name))) {
    render->create_scaled_image_wrapper_upscaled(cover_path(r.name), w, h);
    render->current.add(new PFObj(cover_path(r.name), conf->p_h_res() - 140 - w/2, y + list_font_height - h/2, w, h, false, lvl));
  }

  render->current.add(new TObj(name, list_font, 75, y,
			       themes->movie_font1, themes->movie_font2,
			       themes->movie_font3, 3));
  render->current.add(new TObj(ep, list_font_small, 75, y + list_font_height,
			       themes->movie_font1, themes->movie_font2,
			       themes->movie_font3, 3));
  if (r.viewed) {
    //FIXME: replace with a eye icon
    render->current.add(new TObj("(V)", list_font_small, 75 + 5 + string_format::calculate_string_width(ep, list_font_small), y + list_font_height,
			       themes->movie_font1, themes->movie_font2,
			       themes->movie_font3, 3));
  }


/*  render->current.add(new TObj(out.str(), list_font, conf->p_h_res()-85, y,
			       themes->movie_font1, themes->movie_font2,
			       themes->movie_font3, 3));*/
}


void Series::print_serie_element(const Serie& r, const Serie& position, int y)
{
  string name = r.name;
  string episodes = string(string_format::double_zero(r.episodes) + " " + dgettext("mms-movie", "episodes")) 
			+ " | " + string(dgettext("mms-movie", "unviewed")) + ": " + string_format::double_zero(r.unviewed);


/*  if (r.type != "file")
    name += "/"; */

  string_format::format_to_size(name, list_font, conf->p_h_res()-75-155, true);

  int w = 240, h = 44;
  if (r == position) {
    render->current.add(new PFObj(themes->general_marked_large, 60, y+2,
				  conf->p_h_res()-2*60, list_font_height * 2, 2, true));
    w = 360; h = 66;
    if (file_exists(banner_path(r.name))) {
      render->create_scaled_image_wrapper_upscaled(banner_path(r.name), w, h);
      render->current.add(new PFObj(banner_path(r.name), 
			conf->p_h_res() - w - 80, y + (list_font_height * 2 - h)/2,
			w, h, false, 4));
    }
  } else 
    if (file_exists(banner_path(r.name))) {
      render->create_scaled_image_wrapper_upscaled(banner_path(r.name), w, h);
      render->current.add(new PFObj(banner_path(r.name), conf->p_h_res() - w - 90, y + (list_font_height * 2 - h)/2, w, h, false, 3));
  }
//  std::ostringstream out; out << r.filenames.size();

  render->current.add(new TObj(name, list_font, 75, y,
			       themes->movie_font1, themes->movie_font2,
			       themes->movie_font3, 3));
  render->current.add(new TObj(episodes, list_font_small, 75, y + list_font_height,
			       themes->movie_font1, themes->movie_font2,
			       themes->movie_font3, 3));
  /* string s = string(dgettext("mms-movie", "episodes")) + ": 000";
  render->current.add(new TObj(unviewed, list_font_small, 75 + string_format::calculate_string_width(s, list_font_small), y + list_font_height,
			       themes->movie_font1, themes->movie_font2,
			       themes->movie_font3, 3)); */
/*  render->current.add(new TObj(out.str(), list_font, conf->p_h_res()-85, y,
			       themes->movie_font1, themes->movie_font2,
			       themes->movie_font3, 3));*/
}

void Series::print_season_element(const Season& r, const Season& position, int x)
{
  int y = 10 + header_box_size + 10;
  int ses_size = 0;
  int season_size = 20;

 /* if (r.label == dgettext("mms-movie", "viewed")) {
    string sep = + "|";
    ses_size = string_format::calculate_string_width(sep, list_font);
    x -= 5;
    render->current.add(new TObj(sep, list_font, x,
				 y + (season_size - list_font_height)/2,
				 themes->movie_font1, themes->movie_font2, themes->movie_font3, 4));
        x += ses_size;
  } */

  ses_size = r.width; // string_format::calculate_string_width(r.label, list_font);

  if (r == position)
    render->current.add(new RObj(x - 5, y, 
			     	     ses_size + 5, season_size + 5, 
				     0, 0, 0, 64, 3));

    render->current.add(new TObj(r.label, list_font, x,
				 y + (season_size - list_font_height)/2,
				 themes->movie_font1, themes->movie_font2, themes->movie_font3, 4));
   // std::cout << "drawing: " << r.label << ", x=" << x << std::endl;
    //x += ses_size + 5;
}

void Series::print_season_range(const std::vector<Season>& ep, const Season& position, const int int_position, const int element_size, int offset = 0)
{
    int x, size = 0, tmp_size, tmp_x = 0;
    bool ses_loop = false;

    foreach (Season ses, ep)
	size += ses.width + 5;

    if ((size + offset) > (conf->p_h_res() - 60*2)) {
	//std::cout << "need cut season" << std::endl;
	// calculate start

	tmp_size = vector_lookup(ep, int_position).width;
	tmp_x = 60 + ((conf->p_h_res() - 60*2) / 2) - tmp_size;
        ses_loop = true;
    } else {
	tmp_x = 60 + ((conf->p_h_res() - 60*2) / 2) - size/2;
	ses_loop = false;
    }
	
    x = tmp_x;
    // print right
    //std::cout << " print right..." << std::endl;
    if (ses_loop) {
      for (vector<Season>::const_iterator i = ep.begin() + int_position,
	   end = ep.end(); i != end && x < (conf->p_h_res() - 60); ++i)
        {
	  //std::cout << x << " < " << (conf->p_h_res() - 60) << std::endl;
	  print_season_element(*i, position, x);
 
	  x += (*i).width + 5;
        }
    }
     for (vector<Season>::const_iterator i = ep.begin(),
	 end = ep.end(); i != end && x < (conf->p_h_res() - 60); ++i)
      {
	  //std::cout << x << " < " << (conf->p_h_res() - 60) << std::endl;
	  print_season_element(*i, position, x);
 
	  x += (*i).width + 5;
      }


    if (ses_loop) {
    x = tmp_x;
   // std::cout << " print left..." << int_position << std::endl;

    for (vector<Season>::const_reverse_iterator i = ep.rend() - int_position,
	 end = ep.rend(); i != end && (x - (*i).width - 5) > (60 + offset); i++)
      {
	  x -= (*i).width + 5;
	  //std::cout << x << ", " << (*i).label << std::endl; 
	  print_season_element(*i, position, x);
      }

    for (vector<Season>::const_reverse_iterator i = ep.rbegin(),
	 end = ep.rend(); i != end && (x - (*i).width - 5) > (60 + offset); i++)
      {
	  x -= (*i).width + 5;
	  //std::cout << x << ", " << (*i).label << std::endl; 
	  print_season_element(*i, position, x);
      }
    }
}

Episode Series::extract_file_info(const string& filename)
{
  
  Episode ep;

  string::size_type i;
  if ((i = filename.rfind('/')) == string::npos)
    i = 0;
  ep.name = filename.substr((i != 0) ? i+1 : i);
  string path = filename.substr(0,i+1);

  if ((i = ep.name.rfind('.')) != string::npos)
    ep.name = ep.name.substr(0, i);  

  std::vector<std::string> vec;
  std::cout << "Series::extract_file_info filename = " << ep.name << std::endl;

  // case: serie name - 01x01 - title
  vec = regex_tools::regex_matches(ep.name, "^(.*?) - ([0-9]{1,2})x([0-9]{1,2}) - (.*?)$");
  for (unsigned int t = 0; t < vec.size(); t++){
    switch (t) {
      case 0: ep.serie   = vec[t].c_str(); break;
      case 1: ep.season  = conv::atoi(vec[t].c_str()); break;
      case 2: ep.episode = conv::atoi(vec[t].c_str()); break;
      case 3: ep.title   = vec[t].c_str(); break;
    }
  }
  
  // case: serie name - 01x01
  if (!ep.serie.size() || ( ep.season == 0  && ep.episode == 0 )) {
    vec = regex_tools::regex_matches(ep.name, "^(.*?) - ([0-9]{1,2})x([0-9]{1,2})$");
    for (unsigned int t = 0; t < vec.size(); t++){
       switch (t) {
	case 0: ep.serie   = vec[t].c_str(); break;
	case 1: ep.season  = conv::atoi(vec[t].c_str()); break;
	case 2: ep.episode = conv::atoi(vec[t].c_str()); break;
      }
    }
  }

  // case: 01x01 - title
  if (!ep.serie.size() || ( ep.season == 0  && ep.episode == 0 )) {
    vec = regex_tools::regex_matches(ep.name, "([0-9]{1,2})x([0-9]{1,2}) - (.*?)$");
    for (unsigned int t = 0; t < vec.size(); t++){
      switch (t) {
	case 0: ep.season  = conv::atoi(vec[t].c_str()); break;
	case 1: ep.episode = conv::atoi(vec[t].c_str()); break;
	case 2: ep.title   = vec[t].c_str(); break;
      }
    }
  }

  // case: 01x01
  if (!ep.serie.size() || ( ep.season == 0  && ep.episode == 0 )) {
    vec = regex_tools::regex_matches(ep.name, "([0-9]{1,2})x([0-9]{1,2})");
    for (unsigned int t = 0; t < vec.size(); t++){
      switch (t) {
	case 0: ep.season  = conv::atoi(vec[t].c_str()); break;
	case 1: ep.episode = conv::atoi(vec[t].c_str()); break;
      }    
    }
  }

  // case: S01E01
  if (!ep.serie.size() || ( ep.season == 0  && ep.episode == 0 )) {
    vec = regex_tools::regex_matches(ep.name, "(S[0-9]{1,2})E([0-9]{1,2})");
    for (unsigned int t = 0; t < vec.size(); t++){
      switch (t) {
	case 0: ep.season  = conv::atoi(vec[t].c_str()); break;
	case 1: ep.episode = conv::atoi(vec[t].c_str()); break;
      }
    }
  }

  // case: 01 - title
  if (!ep.serie.size() || ( ep.season == 0  && ep.episode == 0 )) {
    vec = regex_tools::regex_matches(ep.name, "([0-9]{1,2}) - (.*?)$");
    for (unsigned int t = 0; t < vec.size(); t++){
      switch (t) {
	case 0: ep.episode = conv::atoi(vec[t].c_str()); break;
	case 1: ep.title   = vec[t].c_str(); break;
      }    
    }
  }

  string seek, fold;
  if (!ep.serie.size()) {
    foreach (const string& dir, serie_folders ) {
      i = 0;
      i = dir.find_last_of(path);
            seek = path.substr(i);
    }

//  std::cout << "seek = " << seek << std::endl;
  while ((i = seek.rfind("/")) != string::npos) {
	fold = seek.substr(i+1);
        seek = seek.substr(0, i);

        vec = regex_tools::regex_matches(fold, "season ([0-9]{1,2})", true);
        if (vec.size() > 0 && ep.season == 0) 
	  ep.season = conv::atoi(vec[0].c_str());
      }
//      std::cout << " serie = " << fold << std::endl;
      if (ep.serie.empty()) 
	ep.serie = fold;
  }

  if (!ep.serie.size() || ( ep.season == 0  && ep.episode == 0 )) {
    std::cout << "can't extract season and episode" << std::endl;
  }

 std::cout << "Series::extract_file_info serie = " << ep.serie 
		<< ", season = " << conv::itos(ep.season) 
		<< ", episode = " << conv::itos(ep.episode) 
		<< ", title = " << ep.title << std::endl;

  return ep;
}

int Series::files_size() 
{
  return series.size();
}

void Series::set_folders()
{
  list<string> movie_dirs = movie_conf->p_serie_dirs(); // make compiler happy
  // make sure movie folders are not malformed
  foreach (string& dir, movie_dirs)
    if (dir[dir.size()-1] != '/') {
      serie_folders.push_back(dir + '/');
    } else
      serie_folders.push_back(dir);

#ifdef use_inotify
  S_Notify::get_instance()->register_plugin("series", serie_folders,
					    boost::bind(&Series::fs_change, this, _1, _2));
#endif
  
  reset();
}

#ifdef use_inotify
  // notify
void Series::fs_change(NotifyUpdate::notify_update_type type, const std::string& path)
  {
    std::string file, ext;
    std::string dir =  filesystem::FExpand(path);
    if (dir.empty())
      dir = "/";
    else if (!file_tools::is_directory(dir)) {
      dir = dir.substr(0, dir.rfind('/')+1);
      file = path.substr(path.rfind('/')+1, path.size() - path.rfind('/')+1);
      ext = file.substr(file.rfind(".")+1, file.size() - file.rfind(".")+1);
    } else
      dir +="/"; 

/*
    if (type == NotifyUpdate::CREATE_DIR || type == NotifyUpdate::MOVE || type == NotifyUpdate::DELETE_DIR)
      reload_dir(dir);

    // check if a xml file is created */
    if ( type == NotifyUpdate::WRITE_CLOSE_FILE || type == NotifyUpdate::MOVE || 
				(type == NotifyUpdate::CREATE_FILE && filesystem::getFileSize(path)) /* HARD Links */ ) {
	if (!(check_type(path, movie_conf->p_filetypes_m()) == emptyMyPair)) 
		insert_file_into_db(path);
	else if (!(check_type(path, movie_conf->p_filetypes_d()) == emptyMyPair))
		// on backgrond 
		S_BackgroundUpdater::get_instance()->run_once(boost::bind(&SerieDB::parseXML, this, path));
		//parseXML(path);
    }

/*    bool reparsed_current_dir = false;

    do{
      foreach (std::string& p, folders.top().first)
	if (dir == p) {
	  reparse_current_dir();
	  reparsed_current_dir = true;
	  break;
	}
      if (reparsed_current_dir || dir == "/" || dir.size() < 2)
	break;
      dir = dir.substr(0, dir.rfind('/', dir.size()-2)+1); /* go 1 directory up */
/*    } while(true); */
     
    if (type == NotifyUpdate::DELETE_DIR || type == NotifyUpdate::DELETE_FILE) {
      remove_file_into_db(path);
    }

/*    // sanity check
    if (folders.top().second > files.size()-1)
      folders.top().second = files.size()-1;

    if (!(active_control_player() && active_player->fullscreen()) &&
	!global->playback_in_fullscreen && !printing_information && visible && reparsed_current_dir)
      print(files); */
    //input_master->add_input(Input(), ""); // exit mainloop
  }
#endif

/* void Series::save_runtime_settings()
{
  std::ofstream file;

  string path = conf->p_var_data_dir() + "options/MovieGraphicalRuntime";

  file.open(path.c_str());

  if (!file) {
    print_critical(dgettext("mms-movie", "Could not write options to file ") + path, "MOVIE");
  } else {
    file << "imdb_warning_displayed," << imdb_message_not_displayed << std::endl;
  }

  file.close();
} */

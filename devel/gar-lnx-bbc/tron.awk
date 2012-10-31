#!/usr/bin/gawk -f

# Okay, so I want to be able to have output broken up into
# numerically-indexed files, and for there to be a central
# navigation file somewhere.  

# When you process a file, you have it and a list of all the
# other files for the top-level navbar, in order.  Okay, good.
# Then you parse the file, spitting out HTML to the numbered
# output files.  Then when you're done, you have a full daturbase
# to spit out, full of context, on the end of the files (thanks
# to my table-fu).  Keen gear.

# Tricky things to handle:  doubled-up formatting stuff,
# overloaded symbols (star is bold, but is also used for
# unnumbered lists).

# so we just keep a stack of opened tags, and use a function to
# run through each paragraph and  find each regexp and replace it
# with the tag, pushing stack state all the while.  A close
# symbol will search the stack and try to pop back until it finds
# the right tag to close, and closes all those above it.

# So we have Headers, Emphasis, Urls, Rules, Lists, Citations,
# Blockquotes, and maybe Footnotes (use URL syntax minus URL).

# Headers can contain Emphasis
# Emphasis can contain URLs, Emphasis
# URLs can contain Emphasis
# Rules stand alone
# Lists can contain Emphasis, URLs
# Citations can contain Emphasis, URLs, Rules, and
# 	Blockquotes
# Blockquotes stand alone

# B (short circuit), R (same), C, L, H, U, E

BEGIN {
# Use arbitrary numbers of blank lines to separate records
        RS = "\n[[:space:]]*\n+"
	FS = "\n"
	ORS = "\n\n"
	OFS = "\n"
}

# sanitize all lines, do some first-paragraph checking
{ 
	gsub(/"/, "\\&quot;")
	gsub(/</, "\\&lt;")
	gsub(/>/, "\\&gt;")


	fore = "<p>"
	aft = "</p>"

	# This stuff only runs at the start of the input .txt
	# file.  It sets up filename vars and fills out some of
	# the ugly HTML-storing variables.  Also slurps the title
	# and throws it up top.
	if(NR == 1) {
		outputstem = FILENAME
		sub(/\.txt$/, "", outputstem)

		pagestart = "<html><head> <title>" $0 "</title>  <link rel=\"stylesheet\" type=\"text/css\" href=\"bbc.css\"></head><body bgcolor=\"black\" text=\"#cccccc\" link=\"#0099cc\" vlink=\"#aaaaaa\"> <br/> <table width=\"100%\" border=\"0\"> <tr height=\"116\" style=\"height:116\"> <th valign=\"top\" align=\"center\"> <span width=\"240\"><a href=\"/\"><img src=\"logo.png\" width=\"200\" alt=\"LNX-BBC\" border=\"0\" style=\"width:200px\"/></a> </span> </th> <td rowspan=\"3\" valign=\"top\" width=\"100%\"> " 
		tocstart = "</td></tr><tr height=\"100%\"> <td valign=\"top\" align=\"left\" height=\"100%\"><hr align=\"center\" width=\"25%\"/> "
		pagefinish = "</td></tr><tr height=\"100%\"> <td valign=\"top\" align=\"left\" height=\"100%\"> <a href=\"" outputstem ".txt\">Download this document as plain text</a> </td> </tr> <tr height=\"300\"> <td height=\"300\"> &nbsp; </td> <td height=\"300\"> &nbsp; </td></tr> </table> </div> </body></html>"
		outputfile = outputstem ".html"
		print pagestart > outputfile
		print "<hr align=\"center\" width=\"25%\"/> <h4 class=\"navbar\"><a class=\"navbar\" href=\"" outputfile "\">" $0 "</a></h4><ol class=\"chapter\">" > outputstem ".nav"
		print "<h1>" $0 "</h1>" >> outputfile
		next
	}


}

# A line with just a dot in it is a stupid way to make a new
# paragraph.  This may vanish.
/\n[[:blank:]]*\.[[:blank:]]*\n/ {
	gsub(/\n[[:blank:]]*\.[[:blank:]]*\n/, "\n <p/> \n")
}

# example code is wrapped and skipped
$1 ~ /^-+(8&lt;|&gt;8)-+$/ && blockquotemode != "on" {
	sub(/^-+(8&lt;|&gt;8)-+/, "<p><pre class=\"code\">", $1)
	if( $NF ~ /^-+(8&lt;|&gt;8)-+$/ ) {
		sub(/^-+(8&lt;|&gt;8)-+$/, "</pre></p>", $NF)
	} else {
		blockquotemode = "on"
	}
	print >> outputfile
	next
}

# close example code
$NF ~ /^-+(8&lt;|&gt;8)-+$/ && blockquotemode == "on" {
	sub(/^-+(8&lt;|&gt;8)-+$/, "</pre></p>", $NF)
	blockquotemode = "off"
	print >> outputfile
	next
}

blockquotemode == "on" {
	print >> outputfile
	next
}

# arbitrary chains of -=_ are horizontal rules
/(^|\n)[[:blank:]]*[-=_]+[[:blank:]]*(\n|$)/ {
	# do hr stuff with size soon
	gsub(/(^|\n)[[:blank:]]*[-=_]+[[:blank:]]*(\n|$)/, "\n <hr/> \n")
}

# so this just says that if our first line doesn't begin with
# whitespace or end with a colon and we're in dlist mode, just
# end it all here.
$1 !~ /(^[[:blank:]]|:[[:blank:]]*$)/ && dlist == "on" {
	fore = "</dl>" fore
	dlist = "off"
}

# Multiple dlist lines can be had by setting subsequent
# paragraphs with a tab as the first character
$1 ~ /^\t/ && dlist == "on" {
	fore = "<p><dd>" 
	aft = "</dd></p>"
	#sub(/^\t/,"")
}


# if the first line ends with a colon, we're doing a dictionary
# term.
$1 ~ /:[[:blank:]]*$/ {
	dterm =  $1
	sub(/:[[:blank:]]*$/, "", dterm)
	if(dterm ~ /&lt;.+&gt;/) {
		#e-mail
		dterm = gensub(/&lt;([^[:space:]@]+)@[^[:space:]@]+)&gt;/, "<a href=\"mailto:\\1\">\\1</a>", "g", dterm)
		# images!
		dterm = gensub(/&lt;([^[:space:]]+\.[jpen]+g)[[:space:]]+([^&]+)&gt;/, "<img src=\"\\1\" alt=\"\\2\"/>", "g", dterm) 
		dterm = gensub(/&lt;([^[:space:]]+\.[jpen]+g)&gt;/, "<img src=\"\\1\"/>", "g", dterm) 
		# absolute URLs
		dterm = gensub(/&lt;([[:alpha:]]+:\/\/[^[:space:]]+)[[:space:]]+([^&]+)&gt;/, "<a href=\"\\1\">\\2</a>", "g", dterm) 
		dterm = gensub(/&lt;([[:alpha:]]+:\/\/[^[:space:]]+)&gt;/, "<a href=\"\\1\">\\1</a>", "g", dterm) 
		# relative URLs
		dterm = gensub(/&lt;([^[:space:]]+\.html?)[[:space:]]+([^&]+)&gt;/, "<a href=\"\\1\">\\2</a>", "g", dterm) 
		dterm = gensub(/&lt;([^[:space:]]+\.html?)&gt;/, "<a href=\"\\1\">\\1</a>", "g", dterm) 
	}

	fore = "<p><dt>" dterm "</dt> <dd>"
	aft = "</dd></p>"

	if(dlist != "on") {
		fore = "<dl> " fore
		dlist = "on"
	}
	for( i = 2; i <= NF; i++ ) {
		j = i - 1
		$j = $i
	}
	$NF = ""

}

# Citations are pretty inclusive, but do not nest
$1 ~ /^[[:blank:]]*(&gt;|[\#|])[[:blank:]]/ {
	for(i = 1; i <= NF; i++) {
		sub(/^[[:blank:]]*(&gt;|[\#\|])[[:blank:]]/, "", $i)
	}
	gsub(RS, "<p/>")
	fore = fore "<blockquote type=\"cite\">"
	aft = "</blockquote> " aft
}

# Likewise centered blocks.
$1 ~ /^[[:blank:]]*-\| .* \|-[[:blank:]]*$/ {
        sub(/^[[:blank:]]*-\|/, "<div align=\"center\">")
	sub(/\|-[[:blank:]]*$/, "</div>")
}

# lists can have a lot too
$1 ~ /^[[:blank:]]+[-\*o[:digit:]\.]+[[:blank:]]/ {
	indentlevel = 0
	delete liststack
	delete indentstack
	push(indentstack, 0)
	for(i = 1; i <= NF; i++) {
		#print "for " i >> "/dev/stderr"
		gsub(/\t/, "        ", $i)
		#print "gsub " i >> "/dev/stderr"
		if(match($i,/^ +/)) {
			#print "listing up " i ": " $i >> "/dev/stderr"
			indentlevel = RLENGTH
			if(match($i,/^[[:blank:]]+[[:digit:]\.]+[[:blank:]]/)) {
				listtype = "o"
			} else if (match($i,/^[[:blank:]]+[-\*o\.]+[[:blank:]]/)) {
				listtype = "u"
			} else {
				listtype = "x"
			}

			if(listtype == "x") {
				continue
			}
			if(listtype != top(liststack) && indentlevel == top(indentstack)) {
				sub(/^[[:blank:]]+[-\*o[:digit:]\.]+[[:blank:]]/, "</li> </" pop(liststack) "l> <" listtype "l> <li>", $i)
				push(liststack, listtype)

			} else if (indentlevel > top(indentstack)) {
				sub(/^[[:blank:]]+[-\*o[:digit:]\.]+[[:blank:]]/,  "<" listtype "l> <li>", $i)
				push(liststack, listtype )
				push(indentstack, indentlevel)
			} else if (indentlevel < top(indentstack)) {
				sub(/^[[:blank:]]+[-\*o[:digit:]\.]+[[:blank:]]/,  "</li> </" pop(liststack) "l> <li>", $i)
				pop(indentstack)
			} else if (indentlevel == top(indentstack)) {
				sub(/^[[:blank:]]+[-\*o[:digit:]\.]+[[:blank:]]/,  "</li> <li>", $i)
			}


		#print "matchif " i >> "/dev/stderr"
		}
		#print "endfor " i >> "/dev/stderr"
	}
	while(i = pop(liststack)) {
		$NF = $NF "</" i "l>"
	}

}


# headers
$1 ~ /^[[:blank:]]*=+/ {
	printname = makeprintname($0)
	tocname = maketocname(printname)
	match($1,/=+/)
	hlevel = RLENGTH
	if( hlevel > 5 ) {
		hlevel = 5
	}
	if(hlevel == 1) {
		print "<div class=\"next\" align=\"right\"><a class=\"next\" href=\"" outputstem (chnum + 1) ".html\"><b>Next&raquo;</b></a></div>" >> outputstem chnum ".html"
		chnum++
		outputfile = outputstem chnum ".html"
		print pagestart > outputfile
	}
   	tag = "<h" hlevel "><a name=\"" tocname "\">"
   	closetag = "</a></h" hlevel ">"
	sub(/^[[:blank:]]*=+/, tag, $1)
	sub(/=+[[:blank:]]*$/, closetag, $NF)
	addtoc(printname, tocname, hlevel)
	
}

# URLs
/&lt;.+&gt;/ {
	#e-mail
	$0 = gensub(/&lt;([^[:space:]@]+)@[^[:space:]@]+)&gt;/, "<a href=\"mailto:\\1\">\\1</a>", "g")
	# images!
	$0 = gensub(/&lt;([^[:space:]]+\.[jpen]+g)[[:space:]]+([^&]+)&gt;/, "<img src=\"\\1\" alt=\"\\2\"/>", "g") 
	$0 = gensub(/&lt;([^[:space:]]+\.[jpen]+g)&gt;/, "<img src=\"\\1\"/>", "g") 
	# absolute URLs
	$0 = gensub(/&lt;([[:alpha:]]+:\/\/[^[:space:]]+)[[:space:]]+([^&]+)&gt;/, "<a href=\"\\1\">\\2</a>", "g") 
	$0 = gensub(/&lt;([[:alpha:]]+:\/\/[^[:space:]]+)&gt;/, "<a href=\"\\1\">\\1</a>", "g") 
	# relative URLs
	$0 = gensub(/&lt;([^[:space:]]+\.html?)[[:space:]]+([^&]+)&gt;/, "<a href=\"\\1\">\\2</a>", "g") 
	$0 = gensub(/&lt;([^[:space:]]+\.html?)&gt;/, "<a href=\"\\1\">\\1</a>", "g") 
}

## old-style URLs
#/\[[^\[]+\]/ {
#	# images!
#	$0 = gensub(/\[([^[:space:]\]]+\.[jpen]+g)[[:space:]]+([^\]]+)\]/, "<img src=\"\\1\" alt=\"\\2\"/>", "g") 
#	$0 = gensub(/\[([^[:space:]\]]+\.[jpen]+g)\]/, "<img src=\"\\1\"/>", "g") 
#	# absolute URLs
#	$0 = gensub(/\[([[:alpha:]]+:\/\/[^[:space:]\]]+)[[:space:]]+([^\]]+)\]/, "<a href=\"\\1\">\\2</a>", "g") 
#	$0 = gensub(/\[([[:alpha:]]+:\/\/[^[:space:]\]]+)\]/, "<a href=\"\\1\">\\1</a>", "g") 
#	# relative URLs
#	$0 = gensub(/\[([^[:space:]\]]+\.html?)[[:space:]]+([^\]]+)\]/, "<a href=\"\\1\">\\2</a>", "g") 
#	$0 = gensub(/\[([^[:space:]\]]+\.html?)\]/, "<a href=\"\\1\">\\1</a>", "g") 
#
## TODO: allow for footnotes (urls without the URL)
#
#}

#sidebars
$1 ~ /^[[:space:]]*\[/ && $NF ~ /\][[:space:]]*$/ {
	sub(/<p>/, "<p class=\"sidebar\">", fore)
	sub(/^[[:space:]]*\[/, "", $1)
	sub(/\][[:space:]]*$/, "", $NF)
}



# emphasis
/\*[^\*]+\*/ || /\/[^\/]+\// || /_[^_]+_/ || /{[^}]+}/ {
	#print "chillin on " $0
	$0 = gensub(/([[:space:]_\*])\/([[:punct:][:alpha:]][^\/]+[[:punct:][:alpha:]])\/([[:space:][:punct:]])/, "\\1<em>\\2</em>\\3", "g")
	$0 = gensub(/([[:space:]_\/])\*([[:punct:][:alpha:]][^\*]+[[:punct:][:alpha:]])\*([[:space:][:punct:]])/, "\\1<strong>\\2</strong>\\3", "g")
	$0 = gensub(/([[:space:]\/\*])_([[:punct:][:alpha:]][^_]+[[:punct:][:alpha:]])_([[:space:][:punct:]])/, "\\1<u>\\2</u>\\3", "g")
	$0 = gensub(/{([^}]+)}/, "<tt>\\1</tt>", "g")
}

# STOP YELLING
#/[[:space:]][-A-Z$_]+/ && $1 !~ /<h[1-4]>/ { $0 = gensub(/[[:space:]]([-A-Z$_][-A-Z$_(\)]+)/, " <tt>\\1</tt>", "g") }

# Our own make-inspired magic
/\$[^[:space:]]+/ { $0 = gensub(/(\$[^[:space:]"']+)/, "<tt>\\1</tt>", "g") }

# print the paragraph now
{ 
	print fore $0 aft >> outputfile
}

# wrap up the indices and finish off the html
END { 
	navfile =  outputstem ".nav"
	zootfile = outputstem ".html"

	for(i=0; i < lastlevel; i++) {
		print "</ol>" >> zootfile
	}
	print tocstart >> zootfile
	close("navbar.nav")
	while((getline navline < "navbar.nav") > 0) {
		if(navline ~ zootfile "\">") {
			sub(/class="navbar"/, "class=\"activenavbar\"", navline)
		}
		print navline >> zootfile
	}
	print "</ol>" >> navfile
	close(navfile)
	while((getline navline < navfile) > 0) {
		print navline >> zootfile
	}
	print pagefinish >> zootfile

	for(i=1; i <= chnum; i++) {
		zootfile = outputstem i ".html"
		print tocstart >> zootfile
		close("navbar.nav")
		while((getline navline < "navbar.nav") > 0) {
			print navline >> zootfile
		}
		close(navfile)
		while((getline navline < navfile) > 0) {
			if(navline ~ zootfile "\">") {
				sub(/class="chapter"/, "class=\"activechapter\"", navline)
			}
			print navline >> zootfile
		}
		print pagefinish >> zootfile
	}
}

# ha ha welcome to CS110, where we implement a stack because the
# language we're using is too archaic to include one as a
# first-cass data structure.
function push(array, item,    n, i)
{
	if(!item) {
		return 0
	}
	n = 0
	for(i in array) {
		n++
	}
	array[n] = item
	#print "Array[" n "] is " item >> "/dev/stderr"
}

# yes ladies and gentlemen, pop is the longer function here!
function pop(array,    n, i, ret)
{
	n = 0
	for(i in array) {
		n++
	}
	if(n) {
		ret = array[n - 1]
		delete array[n - 1]
		#print "Array[" n - 1 "] deleted: was " ret >> "/dev/stderr"
		return ret
	} else {
		#print "Nothing to pop!" >> "/dev/stderr"
	}
}

# just run through and show us the top item on the stack.  I'm
# sure this could be optimized but I can't be arsed.
function top(array,    i, ret)
{
	for(i in array) {
		ret = array[i]
	}
	return ret
}

function makeprintname(header)
{
	gsub(/^[[:space:]]*=+[[:space:]]*/, "", header)
	gsub(/[[:space:]]*=+[[:space:]]*$/, "", header)
	return header
}

function maketocname(printname)
{
	gsub(/[^[:alnum:]]+/, "_", printname)
	return printname
}

# at least this is less icky than the itemized list code.
function addtoc(name, anchor, level)
{
	# add a line to the sidebar
	if(level == 1) {
		print "<li class=\"chapter\"><a class=\"navbar\" href=\"" outputstem chnum ".html\">" name "</a></li>" >> outputstem ".nav"
	}
	# add a line to the table of contents on the master html
	# file
	if(chnum) {
		for(i=lastlevel; i > level; i--) {
			print "</ol>" >> outputstem ".html"
		}
		for(i=lastlevel; i < level; i++) {
			print "<ol>" >> outputstem ".html"
		}

		if( lastlevel < level ) {
			print "<li><a href=\"" outputstem chnum ".html#" anchor "\">" name "</a>" >> outputstem ".html"
		} else {
			print "</li>\n\n<li><a href=\"" outputstem chnum ".html#" anchor "\">" name "</a>" >> outputstem ".html"
		}
		lastlevel = level
	}
}


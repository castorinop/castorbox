#!/usr/bin/php
<?

class parser_metalink {

	private $links = array();
	public $path = NULL;
	public $action = "query";
	public $name = NULL;

	function parse() {

		$xml = new SimpleXMLElement($this->file, NULL, TRUE);

		if (!$xml) {
			echo "cant load file";
			exit(1);
		}

		foreach ($xml->files->file as $file) {
			if (trim($file['name'])) {
				//echo "\nname: ".$file['name'];
				foreach ($file->resources->url as $url) {
					$url_fix = html_entity_decode($url, ENT_QUOTES, 'UTF-8');
					switch ($url['type']) {
						case 'ed2k': 
							$ret = $this->ed2k_helper($file['name'], $url_fix);
						break;;
						case 'http': 
							$ret = $this->http_helper($file['name'], $url_fix);
						break;;

						default: 
							echo "\n# warning: no ".$url['type']." handler, ignoring";
					}
					if (eregi("(avi|mkv)$", $file['name']))
						echo "\nVIDEO_FILE='".$file['name']."'\n";
						
					if ($ret == -1) {
						$this->out($ret);
						exit();
					}
					if ($file->size) {
						$bits = (($file->size * $ret) /100);
						$percent += $bits;
						$sizes += $file->size;
					}
					
					if ($percent)
						$total = (int)(100 * $percent / $sizes);
					else 
						$total = $total ? ($ret + $total) / 2 : $ret;
				}
			}
		}
		$this->out((int)$total);
	}

	function ed2k_helper ($name, $url) {
		$CMD='/usr/bin/ed2k-helper "'.$this->action.'" "'.$name.'" "'.$url.'" "'.$this->path.'"';
		$ret = `$CMD`;
		$ret = trim(str_replace("HELPER_RESULT=", NULL, $ret));
		echo "\n# ed2k_helper: $ret <= $CMD";
		return $ret;
	}

	function http_helper ($name, $url) {
		if (eregi("/", $name)) {
			$extra = dirname($name);
			$name = basename($name);
		}
		$CMD='/usr/bin/web-helper "'.$this->action.'" "'.$name.'" "'.$url.'" "'.$this->path.'/'.$extra.'"';
		$ret = `$CMD`;
		$ret = trim(str_replace("HELPER_RESULT=", NULL, $ret));
		echo "\n# http_helper: $ret <= $CMD";
		return $ret;
	}
	
	function out($value) {
		echo "\nHELPER_RESULT=$value\n";
	//	exit($value);
	}

}

$ml = new parser_metalink();

if (!eregi("query|download|download_no_fork", $argv[1]) || !$argv[2] || !$argv[3] || !$argv[4]) {
	echo "usage ".$argv[0]." [ query | download ] <name> <file> <path>\n";
	exit();
}

if (!is_dir($argv[4])) {
	echo "<path> is not dir\n";
	exit();
}

$ml->action = $argv[1];
$ml->name = $argv[2];
$ml->file = $argv[3];
$ml->path = $argv[4];
$ml->parse();

?>

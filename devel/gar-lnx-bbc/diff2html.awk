#! /usr/bin/gawk -f
#
# Unified diff htmlizer/colorifier
# Daniel Lundin <daniel@codefactory.se>
#
# Copyright (c) 2002 Daniel Lundin
# Copyright (c) 2002 CodeFactory AB
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
#  * Neither the name of CodeFactory AB nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


function print_block() {
	if (blk != "") {
                # Changed lines
		if (d_blk != "") { 
			b1 = d_blk;
			b2 = blk;
			d_blk = "";
			style = "changed";
                # Common lines
		} else if (d_state == " ") {
			b1 = b2 = blk;
			style = "common";
                # Added lines
		} else if (d_state == "+") {
			b1 = "";
			b2 = blk;
			style = "added";
                # Removed lines
		} else if (d_state == "-") {
			b1 = blk;
			b2 = "";
			style = "removed";
		}
		print "<tr class=\"blk-text\" valign=\"top\">" \
			"<td class=\"left-" style "\">" \
			b1 "<br></td>" \
			"<td class=\"right-" style "\">" \
			b2 "<br></td>" \
			"</tr>\n";
	}
	blk = d_blk = ""; # Clear block buffer
}

BEGIN {
	print "<table class=\"d2h-table\">";
}

END {
	print_block();
	print "</table>";
}

# Skip header lines
/^Index: / {
	print_block();
	print "</table> <table class=\"d2h-table\">";
	print "<tr class=\"file-hdr\"> <th colspan=\"2\">File: " $2 "</th></tr>";
	getline
	split($3, oldversion, ":")
	split($4, newversion, ":")
	print "<tr class=\"ver-hdr\"> <th>Version " oldversion[2] " </th>"
	print "<th>Version " newversion[2] " </th> </tr>"
	getline
	getline
	next
}

# Diff block header
/^@@ / {
	match ($0, /^@@ [+-]([0-9]*).[0-9]* [+-]([0-9]*)./, m);
	print_block();
	d_state = state;
	print "<tr class=\"blk-hdr\">" \
		 "<th align=\"left\">Line " m[1] "</th>" \
		 "<th align=\"left\">Line " m[2] "</th>" \
		"</tr>\n";
	next;
}

# Diff block lines
{
	state = substr ($0, 0, 1);
	text = substr ($0, 2);
	# Encode [<> \t] into HTML entities
	gsub(/</, "\\&lt;", text);
	gsub(/>/, "\\&gt;", text);	
	gsub(/\t/, "    ", text);
	gsub(/ /, "\\&nbsp; ", text);

	if (state == d_state) {
		blk = blk (blk == "" ? "" : "<br>\n" ) text;
	} else {
		if (state == "+" && d_state == "-")
			d_blk = blk;
		else
			print_block();
		blk = text;
		d_state = state;
	}
}

%define build_test 1
%{?_with_test: %{expand: %%global build_test 1}}
%{?_without_test: %{expand: %%global build_test 0}}

%define _requires_exceptions BEGIN\\|mkinstalldirs\\|pear(\\|/usr/bin/tclsh

%define php5_common_major 5
%define libname %mklibname php5_common %{php5_common_major}

%define suhosin_version 0.9.8

Summary:	The PHP5 scripting language
Name:		php
Version:	5.3.1
Release:	%mkrel 2
Group:		Development/PHP
License:	PHP License
URL:		http://www.php.net
Source0:	http://se.php.net/distributions/php-%{version}.tar.gz
Source1:	php-test.ini
Source2:	maxlifetime
Source3:	php.crond
Patch0:		php-init.diff
Patch1:		php-shared.diff
Patch6:		php-libtool.diff
Patch7:		php-no_egg.diff
Patch8:		php-phpize.diff
Patch10:	php-phpbuilddir.diff
# http://www.outoforder.cc/projects/apache/mod_transform/
# http://www.outoforder.cc/projects/apache/mod_transform/patches/php5-apache2-filters.patch
Patch13:	php5-apache2-filters.diff
# remove libedit once and for all
Patch15:	php-no_libedit.diff
Patch16:	php-xmlrpc_epi.patch 
Patch17:	php-xmlrpc_no_rpath.diff
Patch18:	php-really_external_sqlite2.diff
#####################################################################
# Stolen from PLD
Patch20:	php-mail.diff
Patch22:	php-filter-shared.diff
Patch23:	php-mdv_logo.diff
Patch25:	php-dba-link.patch
Patch26:	php-5.2.8-bdb4.7_fix.diff
Patch27:	php-zlib-for-getimagesize.patch
Patch28:	php-zlib.patch
# stolen from debian
Patch30:	php-session.save_path.diff
Patch32:	php-exif_nesting_level.diff
# for kolab2
Patch50:	php-imap-annotation.diff
Patch51:	php-imap-status-current.diff
Patch52:	php-imap-myrights.diff
#####################################################################
# Stolen from fedora
Patch101:	php-cxx.diff
Patch102:	php-install.diff
Patch105:	php-umask.diff
# Fixes for extension modules
Patch112:	php-shutdown.diff
Patch113:	php-libc-client.diff
Patch114:	php-no_pam_in_c-client.diff
# Functional changes
Patch115:	php-dlopen.diff
# Fix bugs
Patch120:	php-tests-wddx.diff
Patch121:	php-bug43221.diff
Patch123:	php-bug43589.diff
Patch224:	php-5.1.0RC6-CVE-2005-3388.diff
Patch225:	php-extraimapcheck.diff
Patch226:	php-no-fvisibility_hidden_fix.diff
Patch227:	php-5.3.0RC1-enchant_lib64_fix.diff
Patch228:	php-5.3.0RC2-xmlrpc-epi_fix.diff
Patch233:	php-5.3.x-bug49224.diff
# http://www.suhosin.org/
Source300:	suhosin-patch-%{version}-%{suhosin_version}.patch.gz.sig
Patch300:	suhosin-patch-%{version}-%{suhosin_version}.patch.gz
BuildRequires:	apache-devel >= 2.2.8
BuildRequires:	autoconf2.1
BuildRequires:	bison
BuildRequires:	byacc
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	libtool-devel
BuildRequires:	libxml2-devel >= 2.6
BuildRequires:	libxslt-devel >= 1.1.0
BuildRequires:	openssl >= 0.9.7
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pam-devel
BuildRequires:	pcre-devel >= 6.6 
BuildRequires:	re2c >= 0.9.11
BuildRequires:	multiarch-utils >= 1.0.3
BuildRequires:  unixODBC-devel
Epoch: 3
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

# stupid postgresql... stupid build system...
# this is needed due to the postgresql packaging and due to bugs like this:
# https://qa.mandriva.com/show_bug.cgi?id=52527
%define postgresql_version %(pg_config &>/dev/null && pg_config 2>/dev/null | grep "^VERSION" | awk '{ print $4 }' 2>/dev/null || echo 0)

%description
PHP5 is an HTML-embeddable scripting language. PHP5 offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP5 is fairly simple. The
most common use of PHP5 coding is probably as a replacement for CGI scripts.

This version of php has the suhosin patch %{suhosin_version} applied. Please
report bugs here: http://qa.mandriva.com/ so that the official maintainer of
this Mandriva package can help you. More information regarding the
suhosin patch %{suhosin_version} here: http://www.suhosin.org/

%package	cli
Summary:	PHP5 CLI interface
Group:		Development/Other
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	php-ctype >= %{epoch}:%{version}
Requires:	php-filter >= %{epoch}:%{version}
Requires:	php-ftp >= %{epoch}:%{version}
Requires:	php-gettext >= %{epoch}:%{version}
Requires:	php-hash >= %{epoch}:%{version}
Requires:	php-ini >= %{version}
Requires:	php-json >= %{epoch}:%{version}
Requires:	php-openssl >= %{epoch}:%{version}
Requires:	php-pcre >= %{epoch}:%{version}
Requires:	php-posix >= %{epoch}:%{version}
Requires:	php-session >= %{epoch}:%{version}
Requires:	php-suhosin >= 0.9.29
Requires:	php-sysvsem >= %{epoch}:%{version}
Requires:	php-sysvshm >= %{epoch}:%{version}
Requires:	php-timezonedb >= 3:2009.10
Requires:	php-tokenizer >= %{epoch}:%{version}
Requires:	php-xmlreader >= %{epoch}:%{version}
Requires:	php-xmlwriter >= %{epoch}:%{version}
Requires:	php-zlib >= %{epoch}:%{version}
Requires:	php-xml >= %{epoch}:%{version}
Provides:	php = %{epoch}:%{version}

%description	cli
PHP5 is an HTML-embeddable scripting language. PHP5 offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP5 is fairly simple. The
most common use of PHP5 coding is probably as a replacement for CGI scripts.

This package contains a command-line (CLI) version of php. You must also
install libphp5_common. If you need apache module support, you also need to
install the apache-mod_php package.

This version of php has the suhosin patch %{suhosin_version} applied. Please
report bugs here: http://qa.mandriva.com/ so that the official maintainer of
this Mandriva package can help you. More information regarding the
suhosin patch %{suhosin_version} here: http://www.suhosin.org/

%package	cgi
Summary:	PHP5 CGI interface
Group:		Development/Other
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	php-ctype >= %{epoch}:%{version}
Requires:	php-filter >= %{epoch}:%{version}
Requires:	php-ftp >= %{epoch}:%{version}
Requires:	php-gettext >= %{epoch}:%{version}
Requires:	php-hash >= %{epoch}:%{version}
Requires:	php-ini >= %{version}
Requires:	php-json >= %{epoch}:%{version}
Requires:	php-openssl >= %{epoch}:%{version}
Requires:	php-pcre >= %{epoch}:%{version}
Requires:	php-posix >= %{epoch}:%{version}
Requires:	php-session >= %{epoch}:%{version}
Requires:	php-suhosin >= 0.9.29
Requires:	php-sysvsem >= %{epoch}:%{version}
Requires:	php-sysvshm >= %{epoch}:%{version}
Requires:	php-timezonedb >= 3:2009.10
Requires:	php-tokenizer >= %{epoch}:%{version}
Requires:	php-xmlreader >= %{epoch}:%{version}
Requires:	php-xmlwriter >= %{epoch}:%{version}
Requires:	php-zlib >= %{epoch}:%{version}
Requires:	php-xml >= %{epoch}:%{version}
Provides:	php = %{epoch}:%{version}
Provides:	php-fcgi = %{epoch}:%{version}-%{release}
Obsoletes:	php-fcgi
# because of a added compat softlink
Conflicts:	php-fcgi < %{epoch}:%{version}-%{release}

%description	cgi
PHP5 is an HTML-embeddable scripting language. PHP5 offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP5 is fairly simple. The
most common use of PHP5 coding is probably as a replacement for CGI scripts.

This package contains a standalone (CGI) version of php with FastCGI support.
You must also install libphp5_common. If you need apache module support, you
also need to install the apache-mod_php package.

This version of php has the suhosin patch %{suhosin_version} applied. Please
report bugs here: http://qa.mandriva.com/ so that the official maintainer of
this Mandriva package can help you. More information regarding the
suhosin patch %{suhosin_version} here: http://www.suhosin.org/

%package -n	%{libname}
Summary:	Shared library for PHP5
Group:		Development/Other
Provides:	php-pcre = %{epoch}:%{version}
Provides:	php-simplexml = %{epoch}:%{version}

%description -n	%{libname}
This package provides the common files to run with different implementations of
PHP5. You need this package if you install the php standalone package or a
webserver with php support (ie: apache-mod_php).

This version of php has the suhosin patch %{suhosin_version} applied. Please
report bugs here: http://qa.mandriva.com/ so that the official maintainer of
this Mandriva package can help you. More information regarding the
suhosin patch %{suhosin_version} here: http://www.suhosin.org/

%package	devel
Summary:	Development package for PHP5
Group:		Development/C
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	autoconf2.5
Requires:	automake1.7
Requires:	bison
Requires:	byacc
Requires:	chrpath
Requires:	dos2unix
Requires:	flex
Requires:	libtool
Requires:	libxml2-devel >= 2.6
Requires:	libxslt-devel >= 1.1.0
Requires:	openssl >= 0.9.7
Requires:	openssl-devel >= 0.9.7
Requires:	pam-devel
Requires:	pcre-devel >= 6.6
Requires:	re2c >= 0.9.11
Requires:	tcl

%description	devel
The php-devel package lets you compile dynamic extensions to PHP5. Included
here is the source for the php extensions. Instead of recompiling the whole php
binary to add support for, say, oracle, install this package and use the new
self-contained extensions support. For more information, read the file
SELF-CONTAINED-EXTENSIONS.

%package	openssl
Summary:	OpenSSL extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}

%description	openssl
This is a dynamic shared object (DSO) for PHP that will add OpenSSL support.

%package	zlib
Summary:	Zlib extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}

%description	zlib
This is a dynamic shared object (DSO) for PHP that will add zlib compression
support to PHP.

%package	doc
Summary:	Documentation for PHP
Group:		Development/PHP

%description	doc
Documentation for php.

%package	bcmath
Summary:	The bcmath module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}

%description	bcmath
This is a dynamic shared object (DSO) for PHP that will add bc style precision
math functions support.

For arbitrary precision mathematics PHP offers the Binary Calculator which
supports numbers of any size and precision, represented as strings.

%package	bz2
Summary:	Bzip2 extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
BuildRequires:	bzip2-devel

%description	bz2
This is a dynamic shared object (DSO) for PHP that will add bzip2 compression
support to PHP.

The bzip2 functions are used to transparently read and write bzip2 (.bz2)
compressed files.

%package	calendar
Summary:	Calendar extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}

%description	calendar
This is a dynamic shared object (DSO) for PHP that will add calendar support.

The calendar extension presents a series of functions to simplify converting
between different calendar formats. The intermediary or standard it is based on
is the Julian Day Count. The Julian Day Count is a count of days starting from
January 1st, 4713 B.C. To convert between calendar systems, you must first
convert to Julian Day Count, then to the calendar system of your choice. Julian
Day Count is very different from the Julian Calendar! For more information on
Julian Day Count, visit http://www.hermetic.ch/cal_stud/jdn.htm. For more
information on calendar systems visit
http://www.boogle.com/info/cal-overview.html. Excerpts from this page are
included in these instructions, and are in quotes.

%package	ctype
Summary:	Ctype extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}

%description	ctype
This is a dynamic shared object (DSO) for PHP that will add ctype support.

The functions provided by this extension check whether a character or string
falls into a certain character class according to the current locale (see also
setlocale()).

%package	curl
Summary:	Curl extension module for PHP
Group:		Development/PHP
BuildRequires:	curl-devel >= 7.9.8
Requires:	%{libname} >= %{epoch}:%{version}

%description	curl
This is a dynamic shared object (DSO) for PHP that will add curl support.

PHP supports libcurl, a library created by Daniel Stenberg, that allows you to
connect and communicate to many different types of servers with many different
types of protocols. libcurl currently supports the http, https, ftp, gopher,
telnet, dict, file, and ldap protocols. libcurl also supports HTTPS
certificates, HTTP POST, HTTP PUT, FTP uploading (this can also be done with
PHP's ftp extension), HTTP form based upload, proxies, cookies, and
user+password authentication.

%package	dba
Summary:	DBA extension module for PHP
Group:		Development/PHP
BuildRequires:	gdbm-devel
BuildRequires:	db4-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	dba
This is a dynamic shared object (DSO) for PHP that will add flat-file databases
(DBA) support.

These functions build the foundation for accessing Berkeley DB style databases.

This is a general abstraction layer for several file-based databases. As such,
functionality is limited to a common subset of features supported by modern
databases such as Sleepycat Software's DB2. (This is not to be confused with
IBM's DB2 software, which is supported through the ODBC functions.)

%package	dom
Summary:	Dom extension module for PHP
Group:		Development/PHP
BuildRequires:	libxml2-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	dom
This is a dynamic shared object (DSO) for PHP that will add dom support.

The DOM extension is the replacement for the DOM XML extension from PHP 4. The
extension still contains many old functions, but they should no longer be used.
In particular, functions that are not object-oriented should be avoided.

The extension allows you to operate on an XML document with the DOM API.

%package	enchant
Summary:	Libenchant binder, support near all spelling tools
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
BuildRequires:	enchant-devel

%description	enchant
Enchant is a binder for libenchant. Libenchant provides a common API for many
spell libraries:

 - aspell/pspell (intended to replace ispell)
 - hspell (hebrew)
 - ispell 
 - myspell (OpenOffice project, mozilla)
 - uspell (primarily Yiddish, Hebrew, and Eastern European languages)
   A plugin system allows to add custom spell support.
   see www.abisource.com/enchant/

%package	exif
Summary:	EXIF extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	php-mbstring >= %{epoch}:%{version}

%description	exif
This is a dynamic shared object (DSO) for PHP that will add EXIF tags support
in image files.

With the exif extension you are able to work with image meta data. For example,
you may use exif functions to read meta data of pictures taken from digital
cameras by working with information stored in the headers of the JPEG and TIFF
images.

%package	fileinfo
Summary:	Fileinfo extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	file
BuildRequires:  file-devel

%description	fileinfo
This extension allows retrieval of information regarding vast majority of file.
This information may include dimensions, quality, length etc...

Additionally it can also be used to retrieve the mime type for a particular
file and for text files proper language encoding.

%package	filter
Summary:	Extension for safely dealing with input parameters
Group:		Development/PHP
BuildRequires:	pcre-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	filter
The Input Filter extension is meant to address this issue by implementing a set
of filters and mechanisms that users can use to safely access their input data.

%package	ftp
Summary:	FTP extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}

%description	ftp
This is a dynamic shared object (DSO) for PHP that will add FTP support.

The functions in this extension implement client access to file servers
speaking the File Transfer Protocol (FTP) as defined in
http://www.faqs.org/rfcs/rfc959. This extension is meant for detailed access to
an FTP server providing a wide range of control to the executing script. If you
only wish to read from or write to a file on an FTP server, consider using the
ftp:// wrapper  with the filesystem functions  which provide a simpler and more
intuitive interface.

%package	gd
Summary:	GD extension module for PHP
Group:		Development/PHP
BuildRequires:	freetype2-devel
BuildRequires:	gd-devel >= 2.0.33
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libxpm-devel
BuildRequires:	t1lib-devel
BuildRequires:	X11-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	gd
This is a dynamic shared object (DSO) for PHP that will add GD support,
allowing you to create and manipulate images with PHP using the gd library.

PHP is not limited to creating just HTML output. It can also be used to create
and manipulate image files in a variety of different image formats, including
gif, png, jpg, wbmp, and xpm. Even more convenient, PHP can output image
streams directly to a browser. You will need to compile PHP with the GD library
of image functions for this to work. GD and PHP may also require other
libraries, depending on which image formats you want to work with.

You can use the image functions in PHP to get the size of JPEG, GIF, PNG, SWF,
TIFF and JPEG2000 images.

%package	gettext
Summary:	Gettext extension module for PHP
Group:		Development/PHP
BuildRequires:	gettext-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	gettext
This is a dynamic shared object (DSO) for PHP that will add gettext support.

The gettext functions implement an NLS (Native Language Support) API which can
be used to internationalize your PHP applications. Please see the gettext
documentation for your system for a thorough explanation of these functions or
view the docs at http://www.gnu.org/software/gettext/manual/gettext.html.

%package	gmp
Summary:	Gmp extension module for PHP
Group:		Development/PHP
BuildRequires:	gmp-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	gmp
This is a dynamic shared object (DSO) for PHP that will add arbitrary length
number support using the GNU MP library.

%package	hash
Summary:	HASH Message Digest Framework
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}

%description	hash
Native implementations of common message digest algorithms using a generic
factory method.

Message Digest (hash) engine. Allows direct or incremental processing of
arbitrary length messages using a variety of hashing algorithms.

%package	iconv
Summary:	Iconv extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}

%description	iconv
This is a dynamic shared object (DSO) for PHP that will add iconv support.

This module contains an interface to iconv character set conversion facility.
With this module, you can turn a string represented by a local character set
into the one represented by another character set, which may be the Unicode
character set. Supported character sets depend on the iconv implementation of
your system. Note that the iconv function on some systems may not work as you
expect. In such case, it'd be a good idea to install the GNU libiconv library.
It will most likely end up with more consistent results.

%package	imap
Summary:	IMAP extension module for PHP
Group:		Development/PHP
BuildRequires:	c-client-devel >= 2007
Requires:	%{libname} >= %{epoch}:%{version}

%description	imap
This is a dynamic shared object (DSO) for PHP that will add IMAP support.

These functions are not limited to the IMAP protocol, despite their name. The
underlying c-client library also supports NNTP, POP3 and local mailbox access
methods.

%package	intl
Summary:	Internationalization extension module for PHP
Group:		Development/PHP
BuildRequires:	icu-devel >= 3.4
Requires:	%{libname} >= %{epoch}:%{version}

%description	intl
This is a dynamic shared object (DSO) for PHP that will add
Internationalization support.

Internationalization extension implements ICU library functionality in PHP.

%package	json
Summary:	JavaScript Object Notation
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}

%description	json
Support for JSON (JavaScript Object Notation) serialization.

%package	ldap
Summary:	LDAP extension module for PHP
Group:		Development/PHP
BuildRequires:	libldap-devel
BuildRequires:	libsasl-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	ldap
This is a dynamic shared object (DSO) for PHP that will add LDAP support.

LDAP is the Lightweight Directory Access Protocol, and is a protocol used to
access "Directory Servers". The Directory is a special kind of database that
holds information in a tree structure.

The concept is similar to your hard disk directory structure, except that in
this context, the root directory is "The world" and the first level
subdirectories are "countries". Lower levels of the directory structure contain
entries for companies, organisations or places, while yet lower still we find
directory entries for people, and perhaps equipment or documents.

%package	mbstring
Summary:	MBstring extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
BuildRequires:	mbfl-devel
BuildRequires:	onig-devel

%description	mbstring
This is a dynamic shared object (DSO) for PHP that will add multibyte string
support.

mbstring provides multibyte specific string functions that help you deal with
multibyte encodings in PHP. In addition to that, mbstring handles character
encoding conversion between the possible encoding pairs. mbstring is designed
to handle Unicode-based encodings such as UTF-8 and UCS-2 and many single-byte
encodings for convenience.

%package	mcrypt
Summary:	Mcrypt extension module for PHP
Group:		Development/PHP
BuildRequires:	libmcrypt-devel
BuildRequires:	libtool-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	mcrypt
This is a dynamic shared object (DSO) for PHP that will add mcrypt support.

This is an interface to the mcrypt library, which supports a wide variety of
block algorithms such as DES, TripleDES, Blowfish (default), 3-WAY, SAFER-SK64,
SAFER-SK128, TWOFISH, TEA, RC3 and GOST in CBC, OFB, CFB and ECB cipher modes.
Additionally, it supports RC6 and IDEA which are considered "non-free".

%package	mssql
Summary:	MS SQL extension module for PHP
Group:		Development/PHP
Requires:       freetds >= 0.63
BuildRequires:  freetds-devel >= 0.63
Requires:	%{libname} >= %{epoch}:%{version}

%description	mssql
This is a dynamic shared object (DSO) for PHP that will add MS SQL databases
support using the FreeTDS library.

%package	mysql
Summary:	MySQL database module for PHP
Group:		Development/PHP
BuildRequires:	mysql-devel >= 4.0.10
Requires:	%{libname} >= %{epoch}:%{version}

%description	mysql
This is a dynamic shared object (DSO) for PHP that will add MySQL database
support.

These functions allow you to access MySQL database servers. More information
about MySQL can be found at http://www.mysql.com/.

Documentation for MySQL can be found at http://dev.mysql.com/doc/.

%package	mysqli
Summary:	MySQL database module for PHP
Group:		Development/PHP
BuildRequires:	mysql-devel >= 4.1.7
Requires:	%{libname} >= %{epoch}:%{version}

%description	mysqli
This is a dynamic shared object (DSO) for PHP that will add MySQL database
support.

The mysqli extension allows you to access the functionality provided by MySQL
4.1 and above. More information about the MySQL Database server can be found at
http://www.mysql.com/

Documentation for MySQL can be found at http://dev.mysql.com/doc/.

%package	odbc
Summary:	ODBC extension module for PHP
Group:		Development/PHP
BuildRequires:	unixODBC-devel >= 2.2.1
Requires:	%{libname} >= %{epoch}:%{version}

%description	odbc
This is a dynamic shared object (DSO) for PHP that will add ODBC support.

In addition to normal ODBC support, the Unified ODBC functions in PHP allow you
to access several databases that have borrowed the semantics of the ODBC API to
implement their own API. Instead of maintaining multiple database drivers that
were all nearly identical, these drivers have been unified into a single set of
ODBC functions.

%package	pcntl
Summary:	Process Control extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}

%description	pcntl
This is a dynamic shared object (DSO) for PHP that will add process spawning
and control support. It supports functions like fork(), waitpid(), signal()
etc.

Process Control support in PHP implements the Unix style of process creation,
program execution, signal handling and process termination. Process Control
should not be enabled within a webserver environment and unexpected results may
happen if any Process Control functions are used within a webserver
environment.

%package	pdo
Summary:	PHP Data Objects Interface
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}

%description	pdo
PDO provides a uniform data access interface, sporting advanced features such
as prepared statements and bound parameters. PDO drivers are dynamically
loadable and may be developed independently from the core, but still accessed
using the same API.

Read the documentation at http://www.php.net/pdo for more information.

%package	pdo_dblib
Summary:	Sybase Interface driver for PDO
Group:		Development/PHP
Requires:       freetds >= 0.63
BuildRequires:  freetds-devel >= 0.63
Requires:	php-pdo >= %{epoch}:%{version}
Requires:	%{libname} >= %{epoch}:%{version}

%description	pdo_dblib
PDO_DBLIB is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to Microsoft SQL Server and Sybase databases through the
FreeTDS libary.

%package	pdo_mysql
Summary:	MySQL Interface driver for PDO
Group:		Development/PHP
Requires:	php-pdo >= %{epoch}:%{version}
Requires:	%{libname} >= %{epoch}:%{version}

%description	pdo_mysql
PDO_MYSQL is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to MySQL 3.x and 4.x databases.
 
PDO_MYSQL will take advantage of native prepared statement support present in
MySQL 4.1 and higher. If you're using an older version of the mysql client
libraries, PDO will emulate them for you.

%package	pdo_odbc
Summary:	ODBC v3 Interface driver for PDO
Group:		Development/PHP
BuildRequires:	unixODBC-devel
Requires:	php-pdo >= %{epoch}:%{version}
Requires:	%{libname} >= %{epoch}:%{version}

%description	pdo_odbc
PDO_ODBC is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to databases through ODBC drivers or through the IBM DB2
Call Level Interface (DB2 CLI) library. PDO_ODBC currently supports three
different "flavours" of database drivers:
 
 o ibm-db2  - Supports access to IBM DB2 Universal Database, Cloudscape, and
              Apache Derby servers through the free DB2 client. ibm-db2 is not
	      supported in Mandriva.

 o unixODBC - Supports access to database servers through the unixODBC driver
              manager and the database's own ODBC drivers.

 o generic  - Offers a compile option for ODBC driver managers that are not
              explicitly supported by PDO_ODBC.

%package	pdo_pgsql
Summary:	PostgreSQL interface driver for PDO
Group:		Development/PHP
BuildRequires:	postgresql-devel
Requires:	php-pdo >= %{epoch}:%{version}
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	postgresql-libs >= %{postgresql_version}

%description	pdo_pgsql
PDO_PGSQL is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to PostgreSQL databases.

%package	pdo_sqlite
Summary:	SQLite v3 Interface driver for PDO
Group:		Development/PHP
BuildRequires:	sqlite3-devel
BuildRequires:	lemon
Requires:	php-pdo >= %{epoch}:%{version}
Requires:	%{libname} >= %{epoch}:%{version}

%description	pdo_sqlite
PDO_SQLITE is a driver that implements the PHP Data Objects (PDO) interface to
enable access to SQLite 3 databases.

This extension provides an SQLite v3 driver for PDO. SQLite V3 is NOT
compatible with the bundled SQLite 2 in PHP 5, but is a significant step
forwards, featuring complete utf-8 support, native support for blobs, native
support for prepared statements with bound parameters and improved concurrency.

%package	pgsql
Summary:	PostgreSQL database module for PHP
Group:		Development/PHP
BuildRequires:	postgresql-devel
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	postgresql-libs >= %{postgresql_version}

%description	pgsql
This is a dynamic shared object (DSO) for PHP that will add PostgreSQL database
support.

PostgreSQL database is Open Source product and available without cost.
Postgres, developed originally in the UC Berkeley Computer Science Department,
pioneered many of the object-relational concepts now becoming available in some
commercial databases. It provides SQL92/SQL99 language support, transactions,
referential integrity, stored procedures and type extensibility. PostgreSQL is
an open source descendant of this original Berkeley code.

%package	posix
Summary:	POSIX extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}

%description	posix
This is a dynamic shared object (DSO) for PHP that will add POSIX functions
support to PHP.

This module contains an interface to those functions defined in the IEEE 1003.1
(POSIX.1) standards document which are not accessible through other means.
POSIX.1 for example defined the open(), read(), write() and close() functions,
too, which traditionally have been part of PHP 3 for a long time. Some more
system specific functions have not been available before, though, and this
module tries to remedy this by providing easy access to these functions.

%package	pspell
Summary:	Pspell extension module for PHP
Group:		Development/PHP
BuildRequires:	aspell-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	pspell
This is a dynamic shared object (DSO) for PHP that will add pspell support to
PHP.

These functions allow you to check the spelling of a word and offer
suggestions.

%package	readline
Summary:	Readline extension module for PHP
Group:		Development/PHP
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	gpm-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	readline
This PHP module adds support for readline functions (only for cli and cgi
SAPIs).

The readline() functions implement an interface to the GNU Readline library.
These are functions that provide editable command lines. An example being the
way Bash allows you to use the arrow keys to insert characters or scroll
through command history. Because of the interactive nature of this library, it
will be of little use for writing Web applications, but may be useful when
writing scripts used from a command line.

%package	recode
Summary:	Recode extension module for PHP
Group:		Development/PHP
BuildRequires:	recode-devel
BuildRequires:	gettext-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	recode
This is a dynamic shared object (DSO) for PHP that will add recode support
using the recode library.

This module contains an interface to the GNU Recode library. The GNU Recode
library converts files between various coded character sets and surface
encodings. When this cannot be achieved exactly, it may get rid of the
offending characters or fall back on approximations. The library recognises or
produces nearly 150 different character sets and is able to convert files
between almost any pair. Most RFC 1345 character sets are supported.

%package	session
Summary:	Session extension module for PHP
Group:		Development/PHP
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires:	%{libname} >= %{epoch}:%{version}

%description	session
This is a dynamic shared object (DSO) for PHP that will add session support.

Session support in PHP consists of a way to preserve certain data across
subsequent accesses. This enables you to build more customized applications and
increase the appeal of your web site.

A visitor accessing your web site is assigned a unique id, the so-called
session id. This is either stored in a cookie on the user side or is propagated
in the URL.

%package	shmop
Summary:	Shared Memory Operations extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}

%description	shmop
This is a dynamic shared object (DSO) for PHP that will add Shared Memory
Operations support.

Shmop is an easy to use set of functions that allows PHP to read, write, create
and delete Unix shared memory segments.

%package	snmp
Summary:	NET-SNMP extension module for PHP
Group:		Development/PHP
Requires:	net-snmp-mibs
BuildRequires:	net-snmp-devel
BuildRequires:	net-snmp-mibs
BuildRequires:	elfutils-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	snmp
This is a dynamic shared object (DSO) for PHP that will add SNMP support using
the NET-SNMP libraries.

In order to use the SNMP functions you need to install the NET-SNMP package.

%package	soap
Summary:	Soap extension module for PHP
Group:		Development/PHP
BuildRequires:	libxml2-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	soap
This is a dynamic shared object (DSO) for PHP that will add soap support.

The SOAP extension can be used to write SOAP Servers and Clients. It supports
subsets of SOAP 1.1, SOAP 1.2 and WSDL 1.1 specifications.

%package	sockets
Summary:	Sockets extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}

%description	sockets
This is a dynamic shared object (DSO) for PHP that will add sockets support.

The socket extension implements a low-level interface to the socket
communication functions based on the popular BSD sockets, providing the
possibility to act as a socket server as well as a client.

%package	sqlite3
Summary:	SQLite database bindings for PHP
Group:		Development/PHP
Requires:	php-pdo >= %{epoch}:%{version}
Obsoletes:	php-sqlite
Provides:	php-sqlite = %{epoch}:%{version}
BuildRequires:	sqlite3-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	sqlite3
This is an extension for the SQLite Embeddable SQL Database Engine. SQLite is a
C library that implements an embeddable SQL database engine. Programs that link
with the SQLite library can have SQL database access without running a separate
RDBMS process.

SQLite is not a client library used to connect to a big database server. SQLite
is the server. The SQLite library reads and writes directly to and from the
database files on disk.

%package	sybase_ct
Summary:	Sybase extension module for PHP
Group:		Development/PHP
Obsoletes:	php-sybase
Provides:	php-sybase = %{epoch}:%{version}
Requires:	%{libname} >= %{epoch}:%{version}

%description	sybase_ct
This is a dynamic shared object (DSO) for PHP that will add Sybase support to
PHP.

%package	sysvmsg
Summary:	SysV msg extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}

%description	sysvmsg
This is a dynamic shared object (DSO) for PHP that will add SysV message queues
support.

%package	sysvsem
Summary:	SysV sem extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}

%description	sysvsem
This is a dynamic shared object (DSO) for PHP that will add SysV semaphores
support.

%package	sysvshm
Summary:	SysV shm extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}

%description	sysvshm
This is a dynamic shared object (DSO) for PHP that will add SysV Shared Memory
support.

%package	tidy
Summary:	Tidy HTML Repairing and Parsing for PHP
Group:		Development/PHP
BuildRequires:	tidy-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	tidy
Tidy is a binding for the Tidy HTML clean and repair utility which allows you
to not only clean and otherwise manipluate HTML documents, but also traverse
the document tree using the Zend Engine 2 OO semantics.

%package	tokenizer
Summary:	Tokenizer extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}

%description	tokenizer
This is a dynamic shared object (DSO) for PHP that will add Tokenizer support.

The tokenizer functions provide an interface to the PHP tokenizer embedded in
the Zend Engine. Using these functions you may write your own PHP source
analyzing or modification tools without having to deal with the language
specification at the lexical level.

%package	xml
Summary:	XML extension module for PHP
Group:		Development/PHP
BuildRequires:	libxml2-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	xml
This is a dynamic shared object (DSO) for PHP that will add XML support. This
extension lets you create XML parsers and then define handlers for different
XML events.

%package	xmlreader
Summary:	Xmlreader extension module for PHP
Group:		Development/PHP
Requires:	php-dom
BuildRequires:	libxml2-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	xmlreader
XMLReader represents a reader that provides non-cached, forward-only access to
XML data. It is based upon the xmlTextReader api from libxml

%package	xmlrpc
Summary:	Xmlrpc extension module for PHP
Group:		Development/PHP
BuildRequires:	expat-devel
BuildRequires:	xmlrpc-epi-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	xmlrpc
This is a dynamic shared object (DSO) for PHP that will add XMLRPC support.

These functions can be used to write XML-RPC servers and clients. You can find
more information about XML-RPC at http://www.xmlrpc.com/, and more
documentation on this extension and its functions at
http://xmlrpc-epi.sourceforge.net/.

%package	xmlwriter
Summary:	Provides fast, non-cached, forward-only means to write XML data
Group:		Development/PHP
BuildRequires:	libxml2-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	xmlwriter
This extension wraps the libxml xmlWriter API. Represents a writer that
provides a non-cached, forward-only means of generating streams or files
containing XML data.

%package	xsl
Summary:	Xsl extension module for PHP
Group:		Development/PHP
BuildRequires:	libxslt-devel
BuildRequires:	libxml2-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	xsl
This is a dynamic shared object (DSO) for PHP that will add xsl support.

The XSL extension implements the XSL standard, performing XSLT transformations
using the libxslt library

%package	wddx
Summary:	WDDX serialization functions
Group:		Development/PHP
Requires:	php-xml
BuildRequires:  libxml2-devel
Requires:	%{libname} >= %{epoch}:%{version}

%description	wddx
This is a dynamic shared object (DSO) that adds wddx support to PHP. 

These functions are intended for work with WDDX (http://www.openwddx.org/)

%package	zip
Summary:	A zip management extension for PHP
Group:		Development/PHP

%description	zip
This is a dynamic shared object (DSO) for PHP that will add zip support to
create and read zip files using the libzip library.

%prep

%setup -q -n php-%{version}

# the ".droplet" suffix is here to nuke the backups later..., we don't want those in php-devel
%patch0 -p0 -b .init.droplet
%patch1 -p1 -b .shared.droplet
%patch6 -p0 -b .libtool.droplet
%patch8 -p1 -b .phpize.droplet
%patch10 -p1 -b .phpbuilddir.droplet
#
%patch13 -p1 -b .apache2-filters.droplet
%patch15 -p0 -b .no_libedit.droplet
%patch16 -p0 -b .xmlrpc_epi_header
%patch17 -p0 -b .xmlrpc_no_rpath.droplet
%patch18 -p0 -b .really_external_sqlite2.droplet
#####################################################################
# Stolen from PLD
%patch20 -p0 -b .mail.droplet
%patch22 -p0 -b .filter-shared.droplet
%patch25 -p0 -b .dba-link.droplet
%patch26 -p0 -b .bdb4.7_fix.droplet
%patch27 -p0 -b .zlib-for-getimagesize.droplet
%patch28 -p1 -b .zlib.droplet

# stolen from debian
%patch30 -p0 -b .session.save_path.droplet
%patch32 -p0 -b .exif_nesting_level.droplet

# for kolab2
#%patch50 -p1 -b .imap-annotation.droplet <- needs porting
#%patch51 -p1 -b .imap-status-current.droplet <- needs porting
#%patch52 -p1 -b .imap-myrights.droplet <- needs porting

#####################################################################
# Stolen from fedora
%patch101 -p0 -b .cxx.droplet
%patch102 -p0 -b .install.droplet
%patch105 -p0 -b .umask.droplet
%patch112 -p1 -b .shutdown.droplet
%patch113 -p0 -b .libc-client-php.droplet
%patch114 -p0 -b .no_pam_in_c-client.droplet
%patch115 -p0 -b .dlopen.droplet

# upstream fixes
%patch120 -p1 -b .tests-wddx.droplet
%patch121 -p0 -b .bug43221.droplet
%patch123 -p0 -b .bug43589.droplet
%patch224 -p0 -b .CVE-2005-3388.droplet
#%patch225 -p0 -b .open_basedir_and_safe_mode_checks.droplet <- does not apply anymore
%patch226 -p0 -b .no-fvisibility_hidden.droplet
%patch227 -p0 -b .enchant_lib64_fix.droplet
%patch228 -p0 -b .xmlrpc-epi_fix.droplet
%patch233 -p0 -b .bug49224.droplet

%patch300 -p1 -b .suhosin.droplet
%patch7 -p1 -b .no_egg.droplet
%patch23 -p1 -b .mdv_logo.droplet

cp %{SOURCE1} php-test.ini
cp %{SOURCE2} maxlifetime
cp %{SOURCE3} php.crond

# lib64 hack
perl -p -i -e "s|/usr/lib|%{_libdir}|" php.crond

# nuke bogus checks becuase i fixed this years ago in our recode package
rm -f ext/recode/config9.m4

# Change perms otherwise rpm would get fooled while finding requires
find -name "*.inc" | xargs chmod 644
find -name "*.php*" | xargs chmod 644
find -name "*README*" | xargs chmod 644

mkdir -p php-devel/extensions
mkdir -p php-devel/sapi

# Install test files in php-devel
cp -a tests php-devel

cp -dpR ext/* php-devel/extensions/
rm -f php-devel/extensions/informix/stub.c
rm -f php-devel/extensions/standard/.deps
rm -f php-devel/extensions/skeleton/EXPERIMENTAL

# SAPI
cp -dpR sapi/* php-devel/sapi/ 
rm -f php-devel/sapi/thttpd/stub.c
rm -f php-devel/sapi/cgi/php.sym
rm -f php-devel/sapi/fastcgi/php.sym
rm -f php-devel/sapi/pi3web/php.sym

# cleanup
find php-devel -name "*.droplet" | xargs rm -f

# don't ship MS Windows source
rm -rf php-devel/extensions/com_dotnet

# likewise with these:
find php-devel -name "*.dsp" | xargs rm -f
find php-devel -name "*.mak" | xargs rm -f
find php-devel -name "*.w32" | xargs rm

# maek sure using system libs
rm -rf ext/pcre/pcrelib
rm -rf ext/pdo_sqlite/sqlite
rm -rf ext/xmlrpc/libxmlrpc

%build
%serverbuild

export CFLAGS="`echo ${CFLAGS} | sed s/O2/O0/` -fPIC -L%{_libdir} -fno-strict-aliasing"
export CXXFLAGS="${CFLAGS}"
export RPM_OPT_FLAGS="${CFLAGS}"

cat > php-devel/buildext <<EOF
#!/bin/bash
gcc -Wall -fPIC -shared $CFLAGS \\
    -I. \`%{_bindir}/php-config --includes\` \\
    -I%{_includedir}/libxml2 \\
    -I%{_includedir}/freetype \\
    -I%{_includedir}/openssl \\
    -I%{_usrsrc}/php-devel/ext \\
    -I%{_includedir}/\$1 \\
    \$4 \$2 -o \$1.so \$3 -lc
EOF

chmod 755 php-devel/buildext

rm -f configure
export PHP_AUTOCONF=autoconf-2.13
./buildconf --force

# Do this patch with a perl hack...
perl -pi -e "s|'\\\$install_libdir'|'%{_libdir}'|" ltmain.sh

export oldstyleextdir=yes
export EXTENSION_DIR="%{_libdir}/php/extensions"
export PROG_SENDMAIL="%{_sbindir}/sendmail"
export GD_SHARED_LIBADD="$GD_SHARED_LIBADD -lm"

# never use "--disable-rpath", it does the opposite

# Configure php5
for i in cgi cli apxs; do
./configure \
    `[ $i = cgi ] && echo --disable-cli` \
    `[ $i = apxs ] && echo --with-apxs2=%{_sbindir}/apxs` \
    `[ $i = cli ] && echo --disable-cgi --enable-cli` \
    --build=%{_build} \
    --prefix=%{_prefix} \
    --exec-prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --sbindir=%{_sbindir} \
    --sysconfdir=%{_sysconfdir} \
    --datadir=%{_datadir} \
    --includedir=%{_includedir} \
    --libdir=%{_libdir} \
    --libexecdir=%{_libexecdir} \
    --localstatedir=/var/lib \
    --mandir=%{_mandir} \
    --enable-shared=yes \
    --enable-static=no \
    --with-libdir=%{_lib} \
    --with-config-file-path=%{_sysconfdir} \
    --with-config-file-scan-dir=%{_sysconfdir}/php.d \
    --disable-debug  \
    --enable-inline-optimization \
    --with-exec-dir=%{_bindir} \
    --with-regex=system \
    --with-pcre-regex=%{_prefix} \
    --with-freetype-dir=%{_prefix} --with-zlib=%{_prefix} \
    --with-png-dir=%{_prefix} \
	--with-pdo-odbc=unixODBC \
	--disable-mysqlnd-threading \
    --enable-magic-quotes \
    --enable-safe-mode \
    --with-zlib=shared,%{_prefix} --with-zlib-dir=%{_prefix} \
    --with-openssl=shared,%{_prefix} \
    --enable-libxml=%{_prefix} --with-libxml-dir=%{_prefix} \
    --enable-mod_charset \
    --without-pear \
    --enable-bcmath=shared \
    --with-bz2=shared,%{_prefix} \
    --enable-calendar=shared \
    --enable-ctype=shared \
    --with-curl=shared,%{_prefix} --without-curlwrappers \
    --enable-dba=shared --with-gdbm --with-db4 --with-cdb  \
    --enable-dom=shared,%{_prefix} --with-libxml-dir=%{_prefix} \
    --with-enchant=shared,%{_prefix} \
    --enable-exif=shared \
    --enable-fileinfo=shared \
    --enable-filter=shared --with-pcre-dir=%{_prefix} \
    --enable-intl=shared --with-icu-dir=%{_prefix} \
    --enable-json=shared \
    --with-openssl-dir=%{_prefix} --enable-ftp=shared \
    --with-gd=shared,%{_prefix} --with-jpeg-dir=%{_prefix} --with-png-dir=%{_prefix} --with-zlib-dir=%{_prefix} --with-xpm-dir=%{_prefix}/X11R6 --with-freetype-dir=%{_prefix} --enable-gd-native-ttf --with-t1lib=%{_prefix} \
    --with-gettext=shared,%{_prefix} \
    --with-gmp=shared,%{_prefix} \
    --enable-hash=shared,%{_prefix} \
    --with-iconv=shared \
    --with-imap=shared,%{_prefix} --with-imap-ssl=%{_prefix} \
    --with-ldap=shared,%{_prefix} --with-ldap-sasl=%{_prefix} \
    --enable-mbstring=shared,%{_prefix} --enable-mbregex --with-libmbfl=%{_prefix} --with-onig=%{_prefix} \
    --with-mcrypt=shared,%{_prefix} \
    --with-mssql=shared,%{_prefix} \
    --with-mysql=shared,%{_prefix} --with-mysql-sock=/var/lib/mysql/mysql.sock --with-zlib-dir=%{_prefix} \
    --with-mysqli=shared,%{_bindir}/mysql_config \
    --with-unixODBC=shared,%{_prefix} \
    --enable-pcntl=shared \
    --enable-pdo=shared,%{_prefix} --with-pdo-dblib=shared,%{_prefix} --with-pdo-mysql=shared,%{_prefix} --with-pdo-odbc=shared,unixODBC,%{_prefix} --with-pdo-pgsql=shared,%{_prefix} --with-pdo-sqlite=shared,%{_prefix} \
    --with-pgsql=shared,%{_prefix} \
    --disable-phar \
    --enable-posix=shared \
    --with-pspell=shared,%{_prefix} \
    --with-readline=shared,%{_prefix} \
    --with-recode=shared,%{_prefix} \
    --enable-session=shared,%{_prefix} \
    --enable-shmop=shared,%{_prefix} \
    --enable-simplexml \
    --with-snmp=shared,%{_prefix} --enable-ucd-snmp-hack \
    --enable-soap=shared,%{_prefix} --with-libxml-dir=%{_prefix} \
    --enable-sockets=shared,%{_prefix} \
    --without-sqlite \
    --with-sqlite3=shared,%{_prefix} \
    --with-sybase-ct=shared,%{_prefix} \
    --enable-sysvmsg=shared,%{_prefix} \
    --enable-sysvsem=shared,%{_prefix} \
    --enable-sysvshm=shared,%{_prefix} \
    --with-tidy=shared,%{_prefix} \
    --enable-tokenizer=shared,%{_prefix} \
    --enable-xml=shared,%{_prefix} --with-libxml-dir=%{_prefix} \
    --enable-xmlreader=shared,%{_prefix} \
    --with-xmlrpc=shared,%{_prefix} \
    --enable-xmlwriter=shared,%{_prefix} \
    --with-xsl=shared,%{_prefix} \
    --enable-wddx=shared --with-libxml-dir=%{_prefix} \
    --enable-zip=shared

cp -f Makefile Makefile.$i

# left for debugging purposes
cp -f main/php_config.h php_config.h.$i

# when all else failed...
perl -pi -e "s|-prefer-non-pic -static||g" Makefile.$i

done

# remove all confusion...
perl -pi -e "s|^#define CONFIGURE_COMMAND .*|#define CONFIGURE_COMMAND \"This is irrelevant, look inside the %{_docdir}/libphp5_common%{php5_common_major}-%{version}/configure_command file. urpmi is your friend, use it to install extensions not shown below.\"|g" main/build-defs.h
cp config.nice configure_command; chmod 644 configure_command

%make

# make php-cgi
cp -af php_config.h.cgi main/php_config.h
make -f Makefile.cgi sapi/cgi/php-cgi
cp -af php_config.h.apxs main/php_config.h

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}/php.d
install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_usrsrc}/php-devel
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_sysconfdir}/cron.d
install -d %{buildroot}/var/lib/php

#perl -pi -e "s|^libdir=.*|libdir='%{_libdir}'|g" .libs/*.la*

make -f Makefile.apxs install \
	INSTALL_ROOT=%{buildroot} \
	INSTALL_IT="\$(LIBTOOL) --mode=install install libphp5_common.la %{buildroot}%{_libdir}/" \
	INSTALL_CLI="\$(LIBTOOL) --silent --mode=install install sapi/cli/php %{buildroot}%{_bindir}/php"

./libtool --silent --mode=install install sapi/cgi/php-cgi %{buildroot}%{_bindir}/php-cgi

# compat php-fcgi symink
ln -s php-cgi %{buildroot}%{_bindir}/php-fcgi

cp -dpR php-devel/* %{buildroot}%{_usrsrc}/php-devel/
install -m0644 run-tests*.php %{buildroot}%{_usrsrc}/php-devel/
install -m0644 main/internal_functions.c %{buildroot}%{_usrsrc}/php-devel/

install -m0644 sapi/cli/php.1 %{buildroot}%{_mandir}/man1/
install -m0644 scripts/man1/phpize.1 %{buildroot}%{_mandir}/man1/
install -m0644 scripts/man1/php-config.1 %{buildroot}%{_mandir}/man1/

ln -snf extensions %{buildroot}%{_usrsrc}/php-devel/ext

# extensions
echo "extension = openssl.so"		> %{buildroot}%{_sysconfdir}/php.d/21_openssl.ini
echo "extension = zlib.so"		> %{buildroot}%{_sysconfdir}/php.d/21_zlib.ini
echo "extension = bcmath.so"		> %{buildroot}%{_sysconfdir}/php.d/66_bcmath.ini
echo "extension = bz2.so"		> %{buildroot}%{_sysconfdir}/php.d/10_bz2.ini
echo "extension = calendar.so"		> %{buildroot}%{_sysconfdir}/php.d/11_calendar.ini
echo "extension = ctype.so"		> %{buildroot}%{_sysconfdir}/php.d/12_ctype.ini
echo "extension = curl.so"		> %{buildroot}%{_sysconfdir}/php.d/13_curl.ini
echo "extension = dba.so"		> %{buildroot}%{_sysconfdir}/php.d/14_dba.ini
echo "extension = dom.so"		> %{buildroot}%{_sysconfdir}/php.d/18_dom.ini
echo "extension = exif.so"		> %{buildroot}%{_sysconfdir}/php.d/19_exif.ini
echo "extension = filter.so"		> %{buildroot}%{_sysconfdir}/php.d/81_filter.ini
echo "extension = ftp.so"		> %{buildroot}%{_sysconfdir}/php.d/22_ftp.ini
echo "extension = gd.so"		> %{buildroot}%{_sysconfdir}/php.d/23_gd.ini
echo "extension = gettext.so"		> %{buildroot}%{_sysconfdir}/php.d/24_gettext.ini
echo "extension = gmp.so"		> %{buildroot}%{_sysconfdir}/php.d/25_gmp.ini
echo "extension = hash.so"		> %{buildroot}%{_sysconfdir}/php.d/54_hash.ini
echo "extension = iconv.so"		> %{buildroot}%{_sysconfdir}/php.d/26_iconv.ini
echo "extension = imap.so"		> %{buildroot}%{_sysconfdir}/php.d/27_imap.ini
echo "extension = intl.so"		> %{buildroot}%{_sysconfdir}/php.d/27_intl.ini
echo "extension = ldap.so"		> %{buildroot}%{_sysconfdir}/php.d/28_ldap.ini
echo "extension = mbstring.so"		> %{buildroot}%{_sysconfdir}/php.d/29_mbstring.ini
echo "extension = mcrypt.so"		> %{buildroot}%{_sysconfdir}/php.d/30_mcrypt.ini
echo "extension = fileinfo.so"		> %{buildroot}%{_sysconfdir}/php.d/32_fileinfo.ini
echo "extension = mssql.so"		> %{buildroot}%{_sysconfdir}/php.d/35_mssql.ini
echo "extension = mysql.so"		> %{buildroot}%{_sysconfdir}/php.d/36_mysql.ini
echo "extension = mysqli.so"		> %{buildroot}%{_sysconfdir}/php.d/37_mysqli.ini
echo "extension = enchant.so"		> %{buildroot}%{_sysconfdir}/php.d/38_enchant.ini
echo "extension = odbc.so"		> %{buildroot}%{_sysconfdir}/php.d/39_odbc.ini
echo "extension = pcntl.so"		> %{buildroot}%{_sysconfdir}/php.d/40_pcntl.ini
echo "extension = pdo.so"		> %{buildroot}%{_sysconfdir}/php.d/70_pdo.ini
echo "extension = pdo_dblib.so"		> %{buildroot}%{_sysconfdir}/php.d/71_pdo_dblib.ini
echo "extension = pdo_mysql.so"		> %{buildroot}%{_sysconfdir}/php.d/73_pdo_mysql.ini
echo "extension = pdo_odbc.so"		> %{buildroot}%{_sysconfdir}/php.d/75_pdo_odbc.ini
echo "extension = pdo_pgsql.so"		> %{buildroot}%{_sysconfdir}/php.d/76_pdo_pgsql.ini
echo "extension = pdo_sqlite.so"	> %{buildroot}%{_sysconfdir}/php.d/77_pdo_sqlite.ini
echo "extension = pgsql.so"		> %{buildroot}%{_sysconfdir}/php.d/42_pgsql.ini
echo "extension = posix.so"		> %{buildroot}%{_sysconfdir}/php.d/43_posix.ini
echo "extension = pspell.so"		> %{buildroot}%{_sysconfdir}/php.d/44_pspell.ini
echo "extension = readline.so"		> %{buildroot}%{_sysconfdir}/php.d/45_readline.ini
echo "extension = recode.so"		> %{buildroot}%{_sysconfdir}/php.d/46_recode.ini
echo "extension = session.so"		> %{buildroot}%{_sysconfdir}/php.d/47_session.ini
echo "extension = shmop.so"		> %{buildroot}%{_sysconfdir}/php.d/48_shmop.ini
echo "extension = snmp.so"		> %{buildroot}%{_sysconfdir}/php.d/50_snmp.ini
echo "extension = soap.so"		> %{buildroot}%{_sysconfdir}/php.d/51_soap.ini
echo "extension = sockets.so"		> %{buildroot}%{_sysconfdir}/php.d/52_sockets.ini
echo "extension = sqlite3.so"		> %{buildroot}%{_sysconfdir}/php.d/78_sqlite3.ini
echo "extension = sybase_ct.so"		> %{buildroot}%{_sysconfdir}/php.d/46_sybase_ct.ini
echo "extension = sysvmsg.so"		> %{buildroot}%{_sysconfdir}/php.d/56_sysvmsg.ini
echo "extension = sysvsem.so"		> %{buildroot}%{_sysconfdir}/php.d/57_sysvsem.ini
echo "extension = sysvshm.so"		> %{buildroot}%{_sysconfdir}/php.d/58_sysvshm.ini
echo "extension = tidy.so"		> %{buildroot}%{_sysconfdir}/php.d/59_tidy.ini
echo "extension = tokenizer.so"		> %{buildroot}%{_sysconfdir}/php.d/60_tokenizer.ini
echo "extension = xml.so"		> %{buildroot}%{_sysconfdir}/php.d/62_xml.ini
echo "extension = xmlreader.so"		> %{buildroot}%{_sysconfdir}/php.d/63_xmlreader.ini
echo "extension = xmlrpc.so"		> %{buildroot}%{_sysconfdir}/php.d/62_xmlrpc.ini
echo "extension = xmlwriter.so"		> %{buildroot}%{_sysconfdir}/php.d/64_xmlwriter.ini
echo "extension = xsl.so"		> %{buildroot}%{_sysconfdir}/php.d/63_xsl.ini
echo "extension = wddx.so"		> %{buildroot}%{_sysconfdir}/php.d/63_wddx.ini
echo "extension = json.so"		> %{buildroot}%{_sysconfdir}/php.d/82_json.ini
echo "extension = zip.so"		> %{buildroot}%{_sysconfdir}/php.d/83_zip.ini

install -m0755 maxlifetime %{buildroot}%{_libdir}/php/maxlifetime
install -m0644 php.crond %{buildroot}%{_sysconfdir}/cron.d/php

# fix docs
cp Zend/LICENSE Zend/ZEND_LICENSE
cp README.SELF-CONTAINED-EXTENSIONS SELF-CONTAINED-EXTENSIONS
cp ext/openssl/README README.openssl
cp ext/spl/README README.spl
cp ext/libxml/CREDITS CREDITS.libxml
cp ext/zlib/CREDITS CREDITS.zlib

# cgi docs
cp sapi/cgi/CREDITS CREDITS.cgi
cp sapi/cgi/README.FastCGI README.fcgi

# cli docs
cp sapi/cli/CREDITS CREDITS.cli
cp sapi/cli/README README.cli
cp sapi/cli/TODO TODO.cli

# house cleaning
rm -f %{buildroot}%{_bindir}/pear
rm -f %{buildroot}%{_libdir}/*.a

# don't pack useless stuff
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/bcmath
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/bz2
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/calendar
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/ctype
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/curl
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/dba
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/dom
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/enchant
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/ereg
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/exif
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/fileinfo
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/filter
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/ftp
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/gettext
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/gmp
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/hash
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/iconv
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/imap
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/intl
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/json
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/ldap
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/libxml
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/mbstring
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/mcrypt
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/mssql
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/mysql
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/mysqli
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/odbc
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/openssl
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pcntl
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pcre
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pdo
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pdo_dblib
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pdo_mysql
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pdo_odbc
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pdo_pgsql
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pdo_sqlite
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pgsql
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/phar
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/posix
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pspell
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/readline
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/recode
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/shmop
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/snmp
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/soap
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/sockets
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/spl
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/sqlite
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/sqlite3
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/standard
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/sybase-ct
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/sybase_ct zip
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/sysvmsg
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/sysvsem
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/sysvshm
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/tidy
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/tokenizer
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/wddx
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/xml
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/xmlreader
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/xmlrpc
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/xmlwriter
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/xsl
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/zlib

# php-devel.i586: E: zero-length /usr/src/php-devel/extensions/pdo_firebird/EXPERIMENTAL
find %{buildroot}%{_usrsrc}/php-devel -type f -size 0 -exec rm -f {} \;

# fix one strange weirdo
%{__perl} -pi -e "s|^libdir=.*|libdir='%{_libdir}'|g" %{buildroot}%{_libdir}/*.la

%multiarch_includes %{buildroot}%{_includedir}/php/main/build-defs.h
%multiarch_includes %{buildroot}%{_includedir}/php/main/php_config.h

%if %{build_test}
# do a make test
export NO_INTERACTION=1
export PHPRC="."
export REPORT_EXIT_STATUS=2
export TEST_PHP_DETAILED=0
export TEST_PHP_ERROR_STYLE=EMACS
export TEST_PHP_LOG_FORMAT=LEODC
export PHP_INI_SCAN_DIR=/dev/null

# FAILING TESTS:
# unknown errors with ext/date/tests/oo_002.phpt probably because of php-5.2.5-systzdata.patch
# http://bugs.php.net/bug.php?id=22414 (claimed to be fixed in 2003, but seems not)
# unknown errors with ext/standard/tests/general_functions/phpinfo.phpt
# unknown errors with ext/standard/tests/strings/setlocale_*
disable_tests="ext/date/tests/oo_002.phpt \
ext/standard/tests/file/bug22414.phpt \
ext/standard/tests/general_functions/phpinfo.phpt \
ext/standard/tests/strings/setlocale_basic1.phpt \
ext/standard/tests/strings/setlocale_basic2.phpt \
ext/standard/tests/strings/setlocale_basic3.phpt \
ext/standard/tests/strings/setlocale_variation1.phpt \
ext/standard/tests/strings/setlocale_variation3.phpt \
ext/standard/tests/strings/setlocale_variation4.phpt \
ext/standard/tests/strings/setlocale_variation5.phpt"

[[ -n "$disable_tests" ]] && \
for f in $disable_tests; do
  [[ -f "$f" ]] && mv $f $f.disabled
done

TEST_PHP_EXECUTABLE=sapi/cli/php sapi/cli/php -c ./php-test.ini run-tests.php
%endif

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%post cgi
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun cgi
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post bcmath
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun bcmath
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post bz2
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun bz2
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post calendar
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun calendar
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post ctype
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun ctype
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post curl
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun curl
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post dba
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun dba
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post dom
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun dom
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post enchant
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun enchant
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post exif
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun exif
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post fileinfo
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun fileinfo
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post filter
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun filter
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post ftp
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun ftp
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post gd
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun gd
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post gettext
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun gettext
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post gmp
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun gmp
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post hash
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun hash
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post iconv
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun iconv
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post intl
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun intl
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post imap
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun imap
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post json
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun json
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post ldap
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun ldap
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post mbstring
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun mbstring
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post mcrypt
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun mcrypt
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post mssql
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun mssql
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post mysql
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun mysql
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post mysqli
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun mysqli
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post odbc
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun odbc
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post openssl
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun openssl
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post pcntl
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun pcntl
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post pdo
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun pdo
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post pdo_dblib
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun pdo_dblib
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post pdo_mysql
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun pdo_mysql
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post pdo_odbc
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun pdo_odbc
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post pdo_pgsql
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun pdo_pgsql
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post pdo_sqlite
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun pdo_sqlite
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post pgsql
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun pgsql
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post posix
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun posix
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post pspell
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun pspell
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post readline
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun readline
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post recode
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun recode
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%pre session
%_pre_useradd apache /var/www /bin/sh

%post session
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun session
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post shmop
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun shmop
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post snmp
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun snmp
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post soap
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun soap
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post sockets
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun sockets
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post sqlite3
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun sqlite3
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post sybase_ct
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun sybase_ct
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post sysvmsg
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun sysvmsg
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post sysvsem
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun sysvsem
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post sysvshm
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun sysvshm
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post tidy
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun tidy
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post tokenizer
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun tokenizer
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post wddx
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun wddx
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post xml
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun xml
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post xmlreader
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun xmlreader
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post xmlrpc
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun xmlrpc
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post xmlwriter
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun xmlwriter
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post xsl
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun xsl
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post zlib
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun zlib
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post zip
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun zip
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files doc
%defattr(-,root,root,-)
%doc CREDITS INSTALL LICENSE NEWS Zend/ZEND_LICENSE 
%doc php.ini-production php.ini-development configure_command
%doc README.openssl README.spl CREDITS.libxml CREDITS.zlib
%doc README.PHP4-TO-PHP5-THIN-CHANGES
%doc README.EXTENSIONS README.EXT_SKEL README.input_filter
%doc README.PARAMETER_PARSING_API README.STREAMS

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/libphp5_common.so.%{php5_common_major}*

%files cli
%defattr(-,root,root)
%doc CREDITS.cli README.cli TODO.cli
%attr(0755,root,root) %{_bindir}/php
%attr(0644,root,root) %{_mandir}/man1/php.1*

%files cgi
%defattr(-,root,root)
%doc CREDITS.cgi README.fcgi
%attr(0755,root,root) %{_bindir}/php-cgi
%attr(0755,root,root) %{_bindir}/php-fcgi

%files devel
%defattr(-,root,root)
%doc SELF-CONTAINED-EXTENSIONS CODING_STANDARDS README.* TODO EXTENSIONS
%doc Zend/ZEND_* README.TESTING*
%attr(0755,root,root) %{_bindir}/php-config
%attr(0755,root,root) %{_bindir}/phpize
%attr(0755,root,root) %{_libdir}/libphp5_common.so
%attr(0755,root,root) %{_libdir}/libphp5_common.la
%{_libdir}/php/build
%{_usrsrc}/php-devel
%multiarch %{multiarch_includedir}/php/main/build-defs.h
%multiarch %{multiarch_includedir}/php/main/php_config.h
%{_includedir}/php
%attr(0644,root,root) %{_mandir}/man1/php-config.1*
%attr(0644,root,root) %{_mandir}/man1/phpize.1*

%files openssl
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/21_openssl.ini
%attr(0755,root,root) %{_libdir}/php/extensions/openssl.so

%files zlib
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/21_zlib.ini
%attr(0755,root,root) %{_libdir}/php/extensions/zlib.so

%files bcmath
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/66_bcmath.ini
%attr(0755,root,root) %{_libdir}/php/extensions/bcmath.so

%files bz2
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/10_bz2.ini
%attr(0755,root,root) %{_libdir}/php/extensions/bz2.so

%files calendar
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/11_calendar.ini
%attr(0755,root,root) %{_libdir}/php/extensions/calendar.so

%files ctype
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/12_ctype.ini
%attr(0755,root,root) %{_libdir}/php/extensions/ctype.so

%files curl
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/13_curl.ini
%attr(0755,root,root) %{_libdir}/php/extensions/curl.so

%files dba
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/14_dba.ini
%attr(0755,root,root) %{_libdir}/php/extensions/dba.so

%files dom
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/18_dom.ini
%attr(0755,root,root) %{_libdir}/php/extensions/dom.so

%files enchant
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/38_enchant.ini
%attr(0755,root,root) %{_libdir}/php/extensions/enchant.so

%files exif
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/19_exif.ini
%attr(0755,root,root) %{_libdir}/php/extensions/exif.so

%files fileinfo
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/32_fileinfo.ini
%attr(0755,root,root) %{_libdir}/php/extensions/fileinfo.so

%files filter
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/81_filter.ini
%attr(0755,root,root) %{_libdir}/php/extensions/filter.so

%files ftp
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/22_ftp.ini
%attr(0755,root,root) %{_libdir}/php/extensions/ftp.so

%files gd
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/23_gd.ini
%attr(0755,root,root) %{_libdir}/php/extensions/gd.so

%files gettext
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/24_gettext.ini
%attr(0755,root,root) %{_libdir}/php/extensions/gettext.so

%files gmp
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/25_gmp.ini
%attr(0755,root,root) %{_libdir}/php/extensions/gmp.so

%files hash
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/54_hash.ini
%attr(0755,root,root) %{_libdir}/php/extensions/hash.so

%files iconv
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/26_iconv.ini
%attr(0755,root,root) %{_libdir}/php/extensions/iconv.so

%files imap
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/27_imap.ini
%attr(0755,root,root) %{_libdir}/php/extensions/imap.so

%files intl
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/27_intl.ini
%attr(0755,root,root) %{_libdir}/php/extensions/intl.so

%files json
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/82_json.ini
%attr(0755,root,root) %{_libdir}/php/extensions/json.so

%files ldap
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/28_ldap.ini
%attr(0755,root,root) %{_libdir}/php/extensions/ldap.so

%files mbstring
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/29_mbstring.ini
%attr(0755,root,root) %{_libdir}/php/extensions/mbstring.so

%files mcrypt
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/30_mcrypt.ini
%attr(0755,root,root) %{_libdir}/php/extensions/mcrypt.so

%files mssql
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/35_mssql.ini
%attr(0755,root,root) %{_libdir}/php/extensions/mssql.so

%files mysql
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/36_mysql.ini
%attr(0755,root,root) %{_libdir}/php/extensions/mysql.so

%files mysqli
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/37_mysqli.ini
%attr(0755,root,root) %{_libdir}/php/extensions/mysqli.so

%files odbc
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/39_odbc.ini
%attr(0755,root,root) %{_libdir}/php/extensions/odbc.so

%files pcntl
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/40_pcntl.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pcntl.so

%files pdo
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/70_pdo.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pdo.so

%files pdo_dblib
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/71_pdo_dblib.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pdo_dblib.so

%files pdo_mysql
%defattr(-,root,root)
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/73_pdo_mysql.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pdo_mysql.so

%files pdo_odbc
%defattr(-,root,root)
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/75_pdo_odbc.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pdo_odbc.so

%files pdo_pgsql
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/76_pdo_pgsql.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pdo_pgsql.so

%files pdo_sqlite
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/77_pdo_sqlite.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pdo_sqlite.so

%files pgsql
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/42_pgsql.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pgsql.so

%files posix
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/43_posix.ini
%attr(0755,root,root) %{_libdir}/php/extensions/posix.so

%files pspell
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/44_pspell.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pspell.so

%files readline
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/45_readline.ini
%attr(0755,root,root) %{_libdir}/php/extensions/readline.so

%files recode
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/46_recode.ini
%attr(0755,root,root) %{_libdir}/php/extensions/recode.so

%files session
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/47_session.ini
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/cron.d/php
%attr(0755,root,root) %{_libdir}/php/extensions/session.so
%attr(0755,root,root) %{_libdir}/php/maxlifetime
%attr(01733,apache,apache) %dir /var/lib/php

%files shmop
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/48_shmop.ini
%attr(0755,root,root) %{_libdir}/php/extensions/shmop.so

%files snmp
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/50_snmp.ini
%attr(0755,root,root) %{_libdir}/php/extensions/snmp.so

%files soap
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/51_soap.ini
%attr(0755,root,root) %{_libdir}/php/extensions/soap.so

%files sockets
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/52_sockets.ini
%attr(0755,root,root) %{_libdir}/php/extensions/sockets.so

%files sqlite3
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/78_sqlite3.ini
%attr(0755,root,root) %{_libdir}/php/extensions/sqlite3.so

%files sybase_ct
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/46_sybase_ct.ini
%attr(0755,root,root) %{_libdir}/php/extensions/sybase_ct.so

%files sysvmsg
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/56_sysvmsg.ini
%attr(0755,root,root) %{_libdir}/php/extensions/sysvmsg.so

%files sysvsem
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/57_sysvsem.ini
%attr(0755,root,root) %{_libdir}/php/extensions/sysvsem.so

%files sysvshm
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/58_sysvshm.ini
%attr(0755,root,root) %{_libdir}/php/extensions/sysvshm.so

%files tidy
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/59_tidy.ini
%attr(0755,root,root) %{_libdir}/php/extensions/tidy.so

%files tokenizer
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/60_tokenizer.ini
%attr(0755,root,root) %{_libdir}/php/extensions/tokenizer.so

%files xml
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/62_xml.ini
%attr(0755,root,root) %{_libdir}/php/extensions/xml.so

%files xmlreader
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/63_xmlreader.ini
%attr(0755,root,root) %{_libdir}/php/extensions/xmlreader.so

%files xmlrpc
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/62_xmlrpc.ini
%attr(0755,root,root) %{_libdir}/php/extensions/xmlrpc.so

%files xmlwriter
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/64_xmlwriter.ini
%attr(0755,root,root) %{_libdir}/php/extensions/xmlwriter.so

%files xsl
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/63_xsl.ini
%attr(0755,root,root) %{_libdir}/php/extensions/xsl.so

%files wddx
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/63_wddx.ini
%attr(0755,root,root) %{_libdir}/php/extensions/wddx.so

%files zip
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/83_zip.ini
%attr(0755,root,root) %{_libdir}/php/extensions/zip.so


%changelog
* Mon Nov 30 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-2mdv2010.1
+ Revision: 471745
- suhosin-patch-5.3.1-0.9.8

* Fri Nov 20 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-1mdv2010.1
+ Revision: 467633
- 5.3.1

* Fri Nov 13 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-0.0.RC4.1mdv2010.1
+ Revision: 465708
- 5.3.1RC4

* Mon Nov 09 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-0.0.RC3.2mdv2010.1
+ Revision: 463584
- fix #54993 (With latest php-5.3.xx, it not needed build separated binary for FastCGI SAPI support)

* Fri Nov 06 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-0.0.RC3.1mdv2010.1
+ Revision: 461144
- 5.3.1RC3
- fix #55063 (Calling utf8_encode or utf8_decode functions stalls PHP)

* Wed Oct 21 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-0.0.RC2.1mdv2010.0
+ Revision: 458554
- dropped P229,P230,P231,P232 as these was implemented in 5.3.1RC2
- rediffed the suhosin patch (P301)

* Tue Oct 20 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-0.0.RC1.5mdv2010.0
+ Revision: 458451
- P230: security fix for a open_basedir bypass vulnerability (svn)
- P231: security fix for a safe_mode bypass vulnerability (svn)
- P232: security fix for CVE-2009-3546.diff (svn)
- P233: upstream fix for php bug 49224

* Thu Oct 15 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-0.0.RC1.4mdv2010.0
+ Revision: 457717
- rebuilt against new net-snmp libs

* Tue Sep 29 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-0.0.RC1.3mdv2010.0
+ Revision: 450934
- fix build
- re-add the suhosin patch (0.9.8)

* Sun Sep 27 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-0.0.RC1.2mdv2010.0
+ Revision: 449829
- P229: security fix for CVE-2009-3291

* Sat Sep 05 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-0.0.RC1.1mdv2010.0
+ Revision: 432063
- fix the libedit patch
- 5.3.1RC1
- rediffed one patch, dropped a redundant patch
- rebuilt against libtiff-3.9.1 and libpng-1.2.39
- previous changes cleaned out work arounds for old'ish problems...
- cleanups (#1)
- cleanups (#1)

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - use autoconf 2.13 for regenerating configure, upstream still use the old autotools set

* Wed Aug 19 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-7mdv2010.0
+ Revision: 417998
- re-add requires on php-suhosin

* Mon Aug 17 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-6mdv2010.0
+ Revision: 417285
- rebuilt against libjpeg v7 (php-gd)

* Thu Jul 30 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-5mdv2010.0
+ Revision: 404813
- fix the postgresql version macro, thanks anssi!
- don't require the php-suhosin package for now as it's broken
- fix deps (helio)
- try to solve problems with "undefined symbol : lo_import_with_oid"
  due to postgresql packaging mess

  + Helio Chissini de Castro <helio@mandriva.com>
    - Removed duplicated buildrequires
    - Removed pg_config for version release. Buildrequires aren't installed in createsrpm time, so pg_config was never present during srpm creation.
      Since mandriva rpm already provides an automatic depends for libpq, there's no need to push explicit depends on php-pgsql nahd php-pdo_pgsql.

* Wed Jul 29 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-3mdv2010.0
+ Revision: 403839
- rebuilt to avoid adding deps in 200+ other spec files...
- revert nuked deps

* Fri Jul 24 2009 Helio Chissini de Castro <helio@mandriva.com> 3:5.3.0-2mdv2010.0
+ Revision: 399144
- Small cleanup in php package
- Fixed xmlrpc_epi compilation putting proper header ( Patch16 ).
- Normalize epochs. Every subpackage had a different epoch and the cascading
  caracteristic of rpm are affecting the subsequent subpackages. Now all
  packages follow the uniq epoch set.
- Add unixODBC as main odbc for pdo.
- removed invalid ( non existent ) options in configure:
  --with-flatfile, --with-inifile, --enable-spl, --enable-track-vars
  --enable-trans-sid, --enable-memory-limit, --with-versioning
- php now uses system regex to avoid define conflicts
- devel package is now requiring only proper libs

* Fri Jul 17 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-1mdv2010.0
+ Revision: 396804
- rediffed one fuzzy patch
- drop the suhosin patch as it's seems dead

* Tue Jul 14 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-0.3mdv2010.0
+ Revision: 395957
- nuke the systzdata patch and reintroduce the php-timezonedb package

* Thu Jul 09 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-0.2mdv2010.0
+ Revision: 393921
- P106: new(er) systzdata patch from fedora

* Wed Jul 01 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-0.1mdv2010.0
+ Revision: 391195
- 5.3.0 (final)
- rediffed one patch

* Fri Jun 19 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-0.0.RC4.1mdv2010.0
+ Revision: 387295
- fix build (#1)
- 5.3.0RC4

* Fri Jun 12 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-0.0.RC3.1mdv2010.0
+ Revision: 385542
- 5.3.0RC3
- rediffed one patch
- fix deps

* Fri Jun 12 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-0.0.RC2.4mdv2010.0
+ Revision: 385425
- rebuild

* Thu Jun 11 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-0.0.RC2.3mdv2010.0
+ Revision: 385287
- fix linkage (xmlrpc-epi)

* Fri May 29 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-0.0.RC2.2mdv2010.0
+ Revision: 381106
- temporary disable the suhosin patch (and 2 others in sequence)

* Wed May 13 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-0.0.RC2.1mdv2010.0
+ Revision: 375295
- 5.3.0RC2 (first draft)
- rediffed a lot of patches
- dropped a lot of redundant patches
- merged a lot of private changes into the cooker package
- the following extensions is gone or moved to pecl:
  - mhash (replaced by internal code)
  - mime_magic (replaced by fileinfo)
  - ming
  - ncurses
  - sqlite (replaced by sqlite3)
  - dbase
  - sybase (replaced by sybase_ct)
- the following extensions is new or moved from pecl:
  - enchant
  - fileinfo (uses bundled libmagic (for now))
  - intl
  - sqlite3
  - sybase_ct

* Thu Mar 26 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-6mdv2009.1
+ Revision: 361334
- added two more upstream patches

* Tue Mar 17 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-5mdv2009.1
+ Revision: 356848
- merge external php-zip into this package as this code is newer
- added a bunch of upstream fixes (P230 - P240)

* Fri Mar 13 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-4mdv2009.1
+ Revision: 354600
- the fix for #43486 broke the wddx extension. the fix isn't needed anymore

* Mon Mar 09 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-3mdv2009.1
+ Revision: 353306
- suhosin-patch-5.2.9-0.9.7

* Sun Mar 08 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-2mdv2009.1
+ Revision: 352897
- backported changes from 5.3 to link against the system oniguruma library (-lonig)

* Sun Mar 01 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-1mdv2009.1
+ Revision: 346351
- 5.2.9

* Wed Feb 25 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-0.0.RC3.2mdv2009.1
+ Revision: 344879
- rebuilt against new readline

* Thu Feb 19 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-0.0.RC3.1mdv2009.1
+ Revision: 342988
- 5.2.9RC3

* Tue Feb 17 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-0.0.RC2.2mdv2009.1
+ Revision: 342247
- fix libtool mess (thanks fedora)

* Sat Feb 14 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-0.0.RC2.1mdv2009.1
+ Revision: 340240
- 5.2.9RC2

* Mon Feb 09 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-0.0.RC1.1mdv2009.1
+ Revision: 338903
- 5.2.9RC1
- rediff some patches
- drop upstream implemented patches
- fix #26274, #45864, and probably many others by using -O0 for compiler
  optimization. either the bug is in php and/or in gcc 4.3.2. the
  dispute goes on... i rather just make it work for now...

* Thu Jan 29 2009 Funda Wang <fwang@mandriva.org> 3:5.2.8-7mdv2009.1
+ Revision: 335080
- rebuild for new libtool

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix security issue ( CAN-2008-5498 )(Bug #46909)

* Wed Jan 14 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.8-6mdv2009.1
+ Revision: 329447
- relink rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.8-5mdv2009.1
+ Revision: 321721
- rebuild

* Tue Dec 16 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.8-4mdv2009.1
+ Revision: 314881
- added P11 to fix build with -Werror=format-security

* Mon Dec 15 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.8-3mdv2009.1
+ Revision: 314591
- rebuilt against db4.7

* Fri Dec 12 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.8-2mdv2009.1
+ Revision: 313611
- rediff some patches to meet the nofuzz criteria

* Tue Dec 09 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.8-1mdv2009.1
+ Revision: 312064
- 5.2.8
- drop the magic_quotes_gpc_fix patch (the only change in 5.2.8, heh...)

* Mon Dec 08 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.7-2mdv2009.1
+ Revision: 311794
- fix reason why 5.2.7 was pulled (P230)
- use lowercase mysql-devel

* Fri Dec 05 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.7-1mdv2009.1
+ Revision: 310189
- 5.2.7
- suhosin-patch-5.2.7-0.9.6.3

* Sat Nov 29 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.7-0.0.RC5.1mdv2009.1
+ Revision: 308022
- 5.2.7RC5 (fixes CVE-2008-3658, CVE-2008-3659)
- 5.2.7RC2 (fixes CVE-2008-2829)
- 5.2.7RC1 (fixes CVE-2008-2665, CVE-2008-2666, CVE-2008-3660)

* Fri Nov 21 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.7-0.0.RC4.1mdv2009.1
+ Revision: 305416
- 5.2.7RC4

* Thu Nov 20 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.7-0.0.RC3.2mdv2009.1
+ Revision: 305278
- fix #45864 (gcc over-optimization causes segv's in some x86_64 apps.)

* Fri Nov 07 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.7-0.0.RC3.1mdv2009.1
+ Revision: 300656
- 5.2.7RC3

* Sat Oct 25 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.7-0.0.RC2.1mdv2009.1
+ Revision: 297258
- 5.2.7RC2
- drop P230, another fix for CVE-2008-2829 is implemented

* Wed Oct 15 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.7-0.0.RC1.1mdv2009.1
+ Revision: 293842
- 5.2.7RC1
- drop obsolete patches; P16,P122,P226,P227,P231,P232
- fix deps
- drop all those buildconflicts thanks to the new PHP_INI_SCAN_DIR env

* Thu Sep 25 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-18mdv2009.0
+ Revision: 288082
- bump release
- fix #44202 (Php-cli should PreRequires update-alternatives)
- fix #44206 (undefined symbol: SWFDisplayItem_get_x)

* Thu Sep 11 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-17mdv2009.0
+ Revision: 283721
- rediffed the kolab2 patches and added one more (P52)

* Sat Sep 06 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-16mdv2009.0
+ Revision: 281822
- fix #43486 (XML parsing ignores encoded elements in character data (e.g. &gt; &lt; etc.))

* Tue Sep 02 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-15mdv2009.0
+ Revision: 278891
- rebuild

* Mon Aug 25 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-14mdv2009.0
+ Revision: 275761
- enable t1lib in php-gd
- rebuilt against new ming libs

* Fri Aug 22 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-13mdv2009.0
+ Revision: 275133
- rebuilt mbstring against external shared libmbfl libs

* Tue Aug 05 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-12mdv2009.0
+ Revision: 263959
- new P106

* Tue Jul 29 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-11mdv2009.0
+ Revision: 252143
- hardcode %%{_localstatedir}

* Sun Jul 27 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-10mdv2009.0
+ Revision: 250655
- bump release
- added P232 (fixed upstream bug 44712)
- added P231 (fixes CVE-2008-2665, CVE-2008-2666)
- added P230 (fixes CVE-2008-2829)

* Mon Jul 14 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-9mdv2009.0
+ Revision: 235415
- rebuild

* Thu Jul 10 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-8mdv2009.0
+ Revision: 233358
- fix deps and linkage with c-client

* Mon Jun 23 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-7mdv2009.0
+ Revision: 228147
- rebuilt due to PayloadIsLzma problems

* Sun Jun 22 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-6mdv2009.0
+ Revision: 227920
- merged sybase support

* Mon Jun 16 2008 Anssi Hannula <anssi@mandriva.org> 3:5.2.6-5mdv2009.0
+ Revision: 219517
- build with main freetds; it has equal functionality now
  (php-freetds_mssql.diff renamed to php-freetds.diff with renaming
   hunks removed)

* Mon Jun 16 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-4mdv2009.0
+ Revision: 219348
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Fri May 16 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-3mdv2009.0
+ Revision: 208087
- bump release
- fix the freetds_mssql stuff
- rebuild

* Fri May 02 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-1mdv2009.0
+ Revision: 200057
- 5.2.6
- drop numerous upstream patches
- suhosin-patch-5.2.6-0.9.6.2

* Sat Apr 19 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-14mdv2009.0
+ Revision: 195829
- fix #40229 by dropping P195 (Prepared statements and bound values in PHP PDO MySQL don't work)
- added autoconf-2.62 fixes (spec file hacks + P218)
- added patches from upstream:
 - P219 - bug44594
 - P220 - bug44603
 - P221 - bug44613
 - P222 - bug44663
 - P223 - fixes possible stack buffer overflow in FastCGI SAPI
 - P224 - bug32979
 - P225 - bug44591
 - P226 - bug44650
 - P227 - bug44667
 - P228 - fixes weird behavior in CGI parameter parsing
 - P229 - bug44673
- drop P195 (bug44200) was unessesary
- added a more complete fix for bug44189

* Tue Apr 01 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-13mdv2008.1
+ Revision: 191385
- bump release
- added more upstream fixes
- added even more patches...
- added a whole bunch of upstream patches, bug number
  designated its file name
- added P151 to fix upstream bug 42177
- added P150 to fix upstream bug 43559
- added P149 to fix upstream bug 44046 (better patch)
- added P149 to fix upstream bug 44046
- added P148 to fix upstream bug 43505
- added P147 to fix upstream bug 42850
- added P146 to fix upstream bug 43495
- added P145 to fix upstream bug 43482
- added P144 to fix upstream bug 43386
- added P143 to fix upstream bug 43373
- added P142 from upstream that adds missing Reflection API metadata for DOM classes
- added P141 to fix upstream bug 43364
- added P140 to plug an suspected sec hole
- added P139 to fix upstream bug 43092
- added P138 to fix upstream bug 43994
- added P137 to fix upstream bug 43301
- added P136 to fix upstream bugs 43808,43527,43003,42190,41599
- added P135 to fix upstream bug 43293
- added P134 to fix upstream bug 43276
- added P133 to fix upstream bug 43248
- added P132 to fix upstream bug 37076
- added P131 to fix upstream bug 43221
- added P130 to fix upstream bug 43216
- added P129 to fix upstream bug 43201
- added P128 to fix upstream bug 43182
- added P127 that fixes upstream bug 43128
- added P126 to fix upstream bug 43105
- added P125 to fix upstream bug 44191
- added P124 to fix upstream bug 42945
- added P123 to fix upstream bug 42838
- added P122 to fix upstream bug 42779
- added P119 to fix upstream mysql fixes
- added P120 to fix upstream mysqli fixes
- added P118 that fixes upstream bug 42369
- use the complete fix for upstream bug 42272 (new patch)
- added P117 to fix upstream bug 42272
- added P116 that fixes numerous upstream bugs for OCI8
- P211 fixes CVE-2008-1384
- added P211 - fix integer overflow in length calculation

* Fri Feb 29 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-12mdv2008.1
+ Revision: 176686
- fix CVE-2008-0599

* Tue Feb 12 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-11mdv2008.1
+ Revision: 166131
- fix some of the rpmlint errors
- add reference to upstream #42604 for the huge list of buildconflicts

* Fri Feb 01 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-10mdv2008.1
+ Revision: 161203
- fix deps
- attempt to make the test suite working again
- drop redundant patches

* Fri Feb 01 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-9mdv2008.1
+ Revision: 161123
- rebuild

  + Pixel <pixel@mandriva.com>
    - nicer fix for "Buggy float to string conversion" on ix86 (#37171)

* Thu Jan 31 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-8mdv2008.1
+ Revision: 160816
- use another approach using -fno-tree-vrp on 32bit machines after recieving info from peroyvind

* Thu Jan 31 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-7mdv2008.1
+ Revision: 160697
- fix deps
- added P106 from fc9 that makes php use system time zone info

* Wed Jan 30 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-6mdv2008.1
+ Revision: 160467
- fix #37171 (PHP : Buggy float to string conversion (ex "0.0:" instead of "0.1"))

* Wed Jan 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 3:5.2.5-5mdv2008.1
+ Revision: 157266
- rebuild with fixed %%serverbuild macro

* Fri Dec 21 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-4mdv2008.1
+ Revision: 136515
- rebuilt against new build deps
- make it possible to link against db-4.6

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Mon Nov 12 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-3mdv2008.1
+ Revision: 108219
- suhosin-patch-5.2.5-0.9.6.2

* Mon Nov 12 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-2mdv2008.1
+ Revision: 108177
- don't use %%post, %%postun for the debug and devel subpackages (whoops!)

* Sun Nov 11 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-1mdv2008.1
+ Revision: 107529
- 5.2.5
- restart apache if needed

* Fri Nov 02 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-0.RC2.3mdv2008.1
+ Revision: 105413
- bump release
- ship some needed code in the devel package (take #2)

* Fri Nov 02 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-0.RC2.2mdv2008.1
+ Revision: 105295
- ship some needed code in the devel package

* Fri Nov 02 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-0.RC2.1mdv2008.1
+ Revision: 105236
- 5.2.5RC2
- rediffed P300
- don't pack useless stuff (gained approx. 7mb)

* Fri Sep 14 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.4-2mdv2008.0
+ Revision: 85585
- suhosin-patch-5.2.4-0.9.6.2

* Sat Sep 01 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.4-1mdv2008.0
+ Revision: 77387
- 5.2.4 (check http://www.php.net/releases/5_2_4.php)
- dropped obsolete/implemented patches; P4,P19,P31,P103,P111
- rediffed patches; P1,P7,P8,P20
- rediffed the suhosin patch (P301)

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-10mdv2008.0
+ Revision: 64294
- rebuild

* Wed Aug 08 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-9mdv2008.0
+ Revision: 60315
- require the latest php-suhosin version
- use the bundled php-json code instead
- rebuilt against latest net-snmp-libs

* Sat Jun 23 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-8mdv2008.0
+ Revision: 43407
- use the new %%serverbuild macro

* Wed Jun 20 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-7mdv2008.0
+ Revision: 41861
- rediffed a lot of patches
- don't use curlwrappers
- fix deps
- use new P20 from pld, it also obsoletes P29

* Fri Jun 15 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-6mdv2008.0
+ Revision: 40071
- don't lie in the php-gd description, fixes #31410

* Wed Jun 13 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-5mdv2008.0
+ Revision: 38671
- fix naming of the ini files

* Tue Jun 12 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-4mdv2008.0
+ Revision: 38190
- bump release
- forgot to ship the source :)
- use distro conditional -fstack-protector
- major spec file rework, most bundled extensions are from now on build from this package
- added some patches that fixes different build problems
- use distro conditional -fstack-protector

* Sun Jun 03 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-2mdv2008.0
+ Revision: 34809
- suhosin-patch-5.2.3-0.9.6.2

* Fri Jun 01 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-1mdv2008.0
+ Revision: 33674
- 5.2.3 (fixes CVE-2007-1887 (improved), CVE-2007-1900, CVE-2007-2756, CVE-2007-2872)
- rediffed P25

* Sat May 26 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.2-2mdv2008.0
+ Revision: 31529
- updated the kolab2 patches (P11,P12)

* Mon May 07 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.2-1mdv2008.0
+ Revision: 24053
- 5.2.2
- suhosin-patch-5.2.2-0.9.6.2

* Tue May 01 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.2-0.RC2.0mdv2008.0
+ Revision: 19991
- 5.2.2RC2
- suhosin-patch-5.2.2rc2
- drop upstream patches; P106,P200,P210,P211,P,P212,P213,P214,P215

* Thu Apr 19 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.1-5mdv2008.0
+ Revision: 14941
- bump release

* Thu Apr 19 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.1-4mdv2008.0
+ Revision: 14938
- P211: security fix for CVE-2007-1001
- P212: security fix for CVE-2007-1285
- P213: security fix for CVE-2007-1583
- P214: security fix for CVE-2007-1718
- P215: security fix for CVE-2007-1454


* Fri Mar 09 2007 Oden Eriksson <oeriksson@mandriva.com> 5.2.1-4mdv2007.1
+ Revision: 139553
- add the new php-timezonedb package as a dep to solve future presumptive problems

* Wed Mar 07 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.1-3mdv2007.1
+ Revision: 134256
- fix deps

* Sun Mar 04 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.1-2mdv2007.1
+ Revision: 132333
- sync with fc (5.2.1-3)

* Fri Feb 09 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.1-1mdv2007.1
+ Revision: 118391
- use the gzip tar ball

* Wed Feb 07 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.1-0mdv2007.1
+ Revision: 117335
- 5.2.1
- suhosin-patch-5.2.1-0.9.6.2
- rediffed and dropped upstream patches

* Wed Feb 07 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.0-15mdv2007.1
+ Revision: 117063
- fix CVE-2007-0455

* Wed Dec 13 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.0-14mdv2007.1
+ Revision: 96376
- fix deps

* Fri Nov 24 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.0-13mdv2007.1
+ Revision: 87040
- fix build, sometimes it builds and sometimes not...
- rebuild
- added support for curl-7.16.0 (P209)

* Wed Nov 15 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.0-10mdv2007.1
+ Revision: 84539
- silly rabbit..., can't use "with" need to use "enable"

* Tue Nov 14 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.0-9mdv2007.1
+ Revision: 84165
- rebuild
- rebuild
- rebuild
- rebuild
- fix deps
- the pcre extension has to be compiled in statically
- broke out php-openssl and php-zlib into sub packages
- fix the long standing rpath issue

* Sun Nov 12 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.0-4mdv2007.0
+ Revision: 83488
- rebuild
- suhosin patch 0.9.6.2
- revert to the predictable automake version

* Thu Nov 09 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.0-2mdv2007.1
+ Revision: 79246
- suhosin patch 0.9.6.1

* Tue Nov 07 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.0-1mdv2007.0
+ Revision: 77319
- 5.2.0 (Major feature enhancements)
- suhosin-patch-5.2.0-0.9.6
- spec file cleansing
- rediffed patches; P1,P7,P23
- dropped obsolete/upstream patches; P22,P24,P26,P33,P209
- added P113 to make the php-imap build cleaner
- drop obsolete virtual provides
- use automake1.9 where needed instead of automake1.7
- use the bundled libtool
- require latest php-suhosin-0.9.10
- require php-filter and php-json (from pecl) to mimic a default php build
- fix better build after peeking at PLD again...

* Thu Nov 02 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.1.6-5mdv2007.1
+ Revision: 75149
- added fixes (P209) for latest imap c-client 2006 (andreas)

* Tue Oct 31 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.1.6-4mdv2007.1
+ Revision: 74298
- rebuild
- remove the "subrel" macro (duh!)

* Tue Oct 31 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.1.6-3.1mdv2007.1
+ Revision: 74289
- suhosin patch 0.9.6
- nuked the hardened-patch
- added the suhosin patch 0.9.5 and apply it per default (P300)
- rediffed patches; P7,P23
- P300 seems to address CVE-2006-4812, so no patching is needed
- force dependancy on the upcoming php-suhosin extension
- Import php

* Mon Aug 28 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.6-1
- 5.1.6 (Major security fixes)
- hardening-patch-5.1.5-0.4.14 (rediffed)
- deactivate upstream php-5.1.4-security-fix-5.patch (P203)

* Fri Aug 18 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.4-7mdv2007.0
- hardening-patch-5.1.4-0.4.14

* Thu Jul 27 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.4-6mdv2007.0
- hardening-patch-5.1.4-0.4.12
- drop the broken out patches P204,P205,P206,P207,P208 and use the full
  php-5.1.4-security-fix-5.patch (P203). those patches originates from
  that one. P203 fixes CVE-2006-2563,CVE-2006-2660,CVE-2006-1990,
  CVE-2006-3011 and some other security fixes. please read Changelog.secfix

* Wed Jul 19 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.4-5mdv2007.0
- P204: security fix for CVE-2006-2563
- P205: security fix for CVE-2006-2660
- P206: security fix - complete fix for CVE-2006-1990 on 64bit
- P207: security fix for CVE-2006-3011
- P208: check for open_basedir and safe_mode restrictions on imap_open
- P209: high characters fix for wddx
- rediffed the hardening-patch (P301)

* Tue Jun 06 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.4-4mdv2007.0
- rebuilt due to package loss

* Tue Jun 06 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.4-3mdv2007.0
- new tarball (contains the pear/install-pear-nozlib.phar file)
- hardening-patch-5.1.4-0.4.11
- added P203 (fixes open_basedir/safe_mode bypass via the realpath() cache)
- added S5 to keep a record of the licensing issues with the hardening-patch

* Sat May 06 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.4-2mdk
- added P30,P31,P32 from debian

* Sat May 06 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.4-1mdk
- 5.1.4
- hardening-patch-5.1.4-0.4.9

* Thu May 04 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.3-1mdk
- 5.1.3 (fixes CVE-2006-1490)
- rediffed P1,P7,P14

* Thu Apr 27 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.2-8mdk
- rebuild

* Wed Apr 26 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.2-7mdk
- added P29 to be able to track spam zombies

* Tue Apr 04 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.2-6mdk
- added P202 to fix CVE-2006-1490

* Wed Mar 22 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.2-5mdk
- fix deps

* Thu Feb 02 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.2-4mdk
- new group (Development/PHP) and iurt rebuild

* Mon Jan 30 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.2-3mdk
- added P24 from PLD (thanks!) to finally fix a nasty behaviour
  that loaded php.ini from current dir
- added P25,P26,P28,P28 from PLD

* Tue Jan 17 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.2-2mdk
- fix deps after reading how a default install works

* Sun Jan 15 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.2-1mdk
- 5.1.2
- rediffed P4,P8
- added P14 because some extensions stopped building
- added P15 do drop libedit in php-readline, it refused to build otherewise
- fix deps

* Mon Dec 26 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.1-4mdk
- added P13 (enables mod_php to manually add apache output filters)

* Sun Dec 18 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.1-3mdk
- added the Mandriva logo (P23) in phpinfo(); (after looking at pld)

* Tue Nov 29 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.1-2mdk
- hardening-patch-5.1.1-0.4.8

* Mon Nov 28 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.1-1mdk
- 5.1.1
- drop the php-yp dep as it is in pecl now

* Sun Nov 27 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0-2mdk
- hardening-patch-5.1.0-0.4.6

* Fri Nov 25 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0-1mdk
- 5.1.0

* Wed Nov 23 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0-0.RC6.1mdk
- 5.1.0RC6, includes fixes for CVE-2005-3054,CVE-2005-3319,CVE-2005-3353
  CVE-2005-3388,CVE-2005-3389,CVE-2005-3390,CVE-2005-3388
- drop upstream patches; P114
- added parts from the CVE-2005-3388 patch from updates (P202)

* Sun Nov 13 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0-0.RC4.2mdk
- rebuilt against openssl-0.9.8a

* Thu Nov 03 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0-0.RC4.1mdk
- 5.1.0RC4
- rediffed patches; P4, P9, P120
- drop obsolete patches; P5, P100
- hardening-patch-5.0.5-0.4.5

* Sun Oct 30 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0-0.RC1.2mdk
- rebuilt to provide a -debug package too

* Thu Sep 22 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0-0.RC1.1mdk
- 5.1.0RC1
- dropped upstream implemented and redundant patches
- rediffed P4,P8,P9,P10,P100,P101,P120,P121
- fix deps
- hardening-patch-5.0.5-0.4.3

* Wed Sep 07 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.5-1mdk
- 5.0.5 (Major security fixes and closes about 150+ bugs)
- rediffed P4,P8,P100,P120,P121
- dropped upstream implemented patches; P109,P110,P113 (P120 
  was partly applied)

* Wed Sep 07 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-9mdk
- hardening-patch-5.0.4-0.4.1

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-8mdk
- rule out pear auto deps

* Sat Jul 30 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-7mdk
- added work arounds for rpm bugs, "Requires(foo,bar)" don't work

* Tue Jul 12 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-6mdk
- hardening-patch-5.0.4-0.3.2
- reworked the --with/--without magic

* Thu Jul 07 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-5mdk
- added rediffed P11 and P12 from the openpkg kolab2 packages

* Sun Jun 05 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-4mdk
- fix deps (typo)

* Sun Jun 05 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-3mdk
- fix deps

* Sat Jun 04 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-2mdk
- rebuild

* Fri May 27 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-1mdk
- rename the package (php5/php)
- sync with fedora
- use better anti ^M stripper
- use new rpm-4.4.x pre,post magic
- reworked the test suite run, many tests fails. some are fixed
  in cvs, and some are not and simply fails.

* Sun Apr 17 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-1mdk
- 5.0.4
- rediff P4,P6,P8,P9.P100
- drop P59,P60,P60 as they are implemented upstream

* Sun Mar 20 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-8mdk
- use the %%mkrel macro

* Thu Feb 17 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-7mdk
- it wasn't possible to build it --with hardened, fixed

* Wed Feb 16 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-6mdk
- fix description
- strip away annoying ^M, better approach

* Sat Feb 12 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-5mdk
- hardened-php-0.2.6 is disabled as it totally breaks commercial 
  applications like Zend(tm) stuff... :(
- added P57-P67 from fedora
- fix a *lot* of wrong-script-end-of-line-encoding rpmlint errors...

* Mon Jan 31 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-4mdk
- fix deps and conditional %%multiarch

* Fri Jan 14 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-3mdk
- hardened-php-0.2.6

* Thu Dec 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-2mdk
- fix deps for the devel package
- drop S5, it's in the NEWS file anyhow

* Thu Dec 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-1mdk
- 5.0.3
- new hardened-php-0.2.4 patch (P11)
- rediffed P4
- drop P55
- new P56

* Thu Dec 09 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.2-3mdk
- misc spec file fixes
- make and run the tests
- more lib64 fixes (P4,P55)

* Mon Nov 08 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.2-2mdk
- added P11 (from www.hardened-php.net)

* Sat Sep 25 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.2-1mdk
- 5.0.2

* Sun Aug 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.1-1mdk
- 5.0.1

* Mon Jul 19 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.0-1mdk
- 5.0.0
- used pld magic to make the shared lib and the php binaries
- rediffed and added some patches
- used parts from my private spec files
- get rid of the php-devel/PHP_BUILD file
- broke out ftp, yp, pcre, gettext, posix, ctype, sysvsem, sysvshm
- drop the "extensions hack", use another way in the info
- had to enable libxml in order to build some xml related modules

* Thu Jul 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.8-1mdk
- security fixes release (CAN-2004-0594, CAN-2004-0595)

* Tue Jul 13 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.7-5mdk
- remove redundant provides

* Sat Jun 26 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.7-4mdk
- sync with fedora (P57,P58) (4.3.7-3)

* Sat Jun 12 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.7-3mdk
- fix deps

* Thu Jun 10 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.7-2mdk
- added P11 (fixes one minor annoyance while running the tests)
- added P56 (fedora)

* Sat Jun 05 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.7-1mdk
- 4.3.7

* Thu May 27 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.6-5mdk
- fixed P8 and P10
- added P11 (fixes from 4.3.7RC1)
- updated S5

* Sat May 22 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.6-4mdk
- fix P5, i messed it up...
- nuke some patch -b droplets because it pollutes the php-devel package

* Sat May 22 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.6-3mdk
- rediffed P5, P21, P22
- added P23 - P29 from PLD, slightly adjusted

* Fri May 21 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.6-2mdk
- added P21 - P25 from fedora
- use the %%configure2_5x macro
- added P10 to make phpize work
- fix deps
- move scandir to /etc/php.d
- misc spec file fixes

* Wed May 05 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.6-1mdk
- rediffed P1 and P20
- drop P40, it's included

* Sun Mar 21 2004 Jean-Michel Dault <jmdault@mandrakesoft.com> 4.3.4-4mdk
- fix PHP bug #25547
- fix bug22414.phpt


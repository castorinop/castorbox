How To Build A BBC

== Getting GAR ==

To build a bbc, first you must fetch the GAR tree.

=== By HTTP ===

<http://www.lnx-bbc.org/images/lnx-bbc-2.0.tar.gz clean GAR tree>:
Exactly equivalent to an anonymous checkout of the RELEASE_lnx-bbc_2_0
tag.  Approximately 700k.

<http://www.lnx-bbc.org/images/lnx-bbc-2.0-with-sources.tar.gz GAR tree with upstream sources>:
As above, but all upstream sources have been combined into the tree.
Approximately 250 MB.

When you unpack your tarball, you should have a directory called
"lnx-bbc-2.0" sitting in your current directory.  You can rename it if
you like.  We call it gar.

=== From CVS ===

The first step is to log into the CVS pserver.

----8<----
cvs -d:pserver:anonymous@cvs.lnx-bbc.org:/var/cvs login
----8<----

Just hit return when it asks you for a password.  You can now check
out the STABLE or HEAD branches of the tree.

==== STABLE ====

The STABLE branch is designed to compile on the current revision of
Debian Stable.  Our build system uses this, and our <chroot.html
published chroot environments> use it as well.  Typically our releases
come from this tree, and we try to fold in changes judiciously.

----8<----
cvs -z3 -d:pserver:anonymous@cvs.lnx-bbc.org:/var/cvs co -r STABLE gar
----8<----

==== HEAD ====

This is the unstable branch of the tree, and contains up-to-the-minute
updates of what our developers have been working on.  It typically
builds on a Debian testing or unstable distribution, and may break on
stable.  You may find this to build on your more recent Red Hat
distributions if the STABLE branch does not.  

----8<----
cvs -z3 -d:pserver:anonymous@cvs.lnx-bbc.org:/var/cvs co gar
----8<----

== Configuring GAR ==

You can either set environment variables or edit gar.conf.mk directly.
Setting them in your environment is recommended.  The instructions for
configuring the GAR sources distributed by the Free Software
Foundation or a CVS checkout from the RELEASE_lnx-bbc_2_0 tag or
earlier are different, please see the subsection at the end of this
chapter.

You'll want to set main_DESTDIR and build_prefix to point into someplace
with a lot of free disk space for the build.

main_DESTDIR is where the actual BBC filesystem is put, in preparation 
for compressing and making the .ISO.

build_prefix is a temporary dir where things needed during build are
placed.

If you don't have permission to write to /var/www/garchive, then
you'll want to set GARCHIVEROOT as well.

=== Configuring older versions of GAR ===

This section explains how to configure the version of GAR as
distributed by the Free Software Foundation, as checked out from CVS
using the RELEASE_lnx-bbc_2_0 tag, or any earlier version.

There are two variables which you should override, either by editting
the file gar.conf.mk or by exporting them in your shell's environment.
There must be a few gigabytes of space available at the locations
specified in these variables.

DESTDIR is where the contents of the BBC are built.  Set it to the
absolute path where there is adequate space.

BUILD_PREFIX is where various tools are installed that GAR uses over
the course of building an LNX-BBC.  Select a directory where these
tools should go, and set BUILD_PREFIX to that value prepended with the
literal string "$(ROOTFROMDEST)".

== Bulk Operations on all Packages ==

Running any target from the top-level dir (the one in which this README 
lives) will be performed on all packages.  

However, we have provided some custom make targets in the
gar/meta/lnx-bbc directory Makefile in order to make development life
much easier.  Using these is highly recommended.

For the bulleted commands below, choose only one, according to whether
you prefer to work from the top of the tree, or from gar/meta/lnx-bbc.

== Pre-fetching the source code ==

The LNX-BBC build process takes a few hundred megabytes of compressed
source code.  If you don't plan on having a constant network
connection during the build process, you can pre-fetch source code in
a couple of ways:

=== First, you can checksum the tree. =====

From the gar/meta/lnx-bbc directory, "make deep-checksums":
This has the advantage of downloading and verifying only those packages 
which are needed by the LNX-BBC itself.  This is how the "with sources" 
tarball above was created.

or, from the top-level directory, "make checksums": This may, however,
download a number of tarballs for packages that are not needed by the
BBC but are in the GAR tree nonetheless. 

=== Second, you can preserve a fetched source tree from doom and destruction. ===

The use of the checksum rule is not without its flaws, however.  If
you want these files to survive your efforts to repeat your build from
a clean slate, then they need to be garchived.

Either run "make deep-garchive" from the gar/meta/lnx-bbc directory or
"make garchive" from the top-level directory.  The downloaded sources
will be copied from their respective (package)/download areas and
placed in the directory referenced by GARCHIVEROOT.  See "Configuring
GAR" above.


== Building the ISO ==

If this is not your first time building and you wish to rebuild
everything, you have two choices.  From the top directory you can
"make clean" and it will propagate into every package.  However, this
will not clean out your DESTDIR or BUILD_PREFIX directories.  Drastic
changes and especially removals of extra parts (perhaps things that
take too much space?) will require a cleaner build to be properly
tested.  You can clear out those directories yourself, or take the
easy way out;  from gar/meta/lnx-bbc, run "make super-clean" and it
will clear both locations for you as well as cleaning the GAR tree.

Now cd into gar/meta/lnx-bbc and run "make build".  After several
hours, you should have a datestamped .iso file in the work/
subdirectory.  Just burn this to a CD-R or CD-RW and use it to boot.
It is generally not a good idea to run the "make build" as root.  We
make sure that the BBC can be built by a normal unprivileged user!
You may need special privilege to write to your CD-R device, however.  

== Bugs ==

To file a bug against the BBC, send mail to submit@bugs.lnx-bbc.org
with the first line of your message reading "Package: foo" where foo
is the name of the piece of software that's broken (such as gcc, or
glibc, or init).  Please be descriptive, and include output and error
messages where you can, and patches where you've solved things.

== Building in a chroot ==

Since not all distributions or installations match up with the
assumptions of the build tree, you may wish to follow <chroot.html
sneakums' chroot build instructions>.

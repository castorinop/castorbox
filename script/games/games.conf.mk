DESTDIR := $(mm_HOME)/images/games

games_rootdir	    ?= $(mm_HOME)/images/games
games_prefix         = $(games_rootdir)/usr
games_exec_prefix    = $(games_prefix)
games_ebindir        = $(games_rootdir)/bin
games_launcher       = $(games_ebindir)/launch
games_esbindir       = $(games_rootdir)/sbin
games_elibdir        = $(games_rootdir)/lib
games_sysconfdir     = $(games_rootdir)/etc
games_localstatedir  = $(games_rootdir)/var
games_bindir         = $(games_exec_prefix)/bin
games_sbindir        = $(games_exec_prefix)/sbin
games_libdir         = $(games_exec_prefix)/lib
games_libexecdir     = $(games_exec_prefix)/libexec
games_datadir        = $(games_prefix)/share
games_sharedstatedir = $(games_prefix)/share
games_infodir        = $(games_prefix)/info
games_lispdir        = $(games_prefix)/share/emacs/site-lisp
games_includedir     = $(games_prefix)/include
games_oldincludedir  = $(games_prefix)/include
games_mandir         = $(games_prefix)/man
games_docdir         = $(games_prefix)/share/doc
games_sourcedir      = $(games_prefix)/src
games_versiondir     = $(games_prefix)/versions
games_licensedir     = $(games_prefix)/licenses


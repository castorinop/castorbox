GCC_MAJOR_VERSION = 4
GCC_MINOR_VERSION = 7
GCC_TEENY_VERSION = 2
GCC_EXTRA_VERSION =

GCC_VERSION = $(strip $(if $(GCC_EXTRA_VERSION), \
	$(if $(filter RC-%,$(GCC_EXTRA_VERSION)), \
		$(GCC_MAJOR_VERSION).$(GCC_MINOR_VERSION).$(GCC_TEENY_VERSION)-$(GCC_EXTRA_VERSION), \
		$(GCC_MAJOR_VERSION).$(GCC_MINOR_VERSION)-$(GCC_EXTRA_VERSION)                       ), \
	$(GCC_MAJOR_VERSION).$(GCC_MINOR_VERSION).$(GCC_TEENY_VERSION)  ))

CROSS_GCC_DIR = \
	$(build_DESTDIR)$(build_libdir)/gcc/$(GARTARGET)
CROSS_GCC_LIBDIR = \
	$(CROSS_GCC_DIR)/$(GCC_MAJOR_VERSION).$(GCC_MINOR_VERSION).$(GCC_TEENY_VERSION)
CROSS_GCC_INCLUDEDIR = \
	$(CROSS_GCC_LIBDIR)/include
CROSS_GCC_LIBEXECDIR = \
	$(build_DESTDIR)$(build_libexecdir)/gcc/$(GARTARGET)/$(GCC_MAJOR_VERSION).$(GCC_MINOR_VERSION).$(GCC_TEENY_VERSION)

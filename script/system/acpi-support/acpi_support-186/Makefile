all: acpi_fakekey

acpi_fakekey: acpi_fakekey.c
	gcc -g -Wall -o acpi_fakekey acpi_fakekey.c
	strip acpi_fakekey

# Keep this manually generated so that it doesn't build-dep on
# 'linux-headers' and stays predictable.

key-constants: /usr/include/linux/input.h aliased-keys
	test -f $<
	echo -n '# Generated from $< dated ' > $@
	date -r $< >> $@
	awk '/#define  *KEY_/{if(strtonum($$3) <= 255) print $$2"="strtonum($$3)}' $< | sort -nt'=' -k2 >> $@
	test -f aliased-keys && cat aliased-keys >> $@

clean:
	rm -f acpi_fakekey

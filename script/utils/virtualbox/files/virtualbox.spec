%define ver	2.0.2
%define rel	2
#define svndate	20070209
%define version	%{ver}%{?svndate:.%{svndate}}
%define release	%mkrel %{rel}
%define kname	vboxdrv
%define oname	VirtualBox
%define srcname	%{oname}-%{version}-OSE
%define distname	%{oname}-%{version}
%define dirname vbox-ose
%define pkgver	%{ver}%{?svndate:-%{svndate}}

%define vboxdir	%{_libdir}/%{name}

%define build_additions 1

%ifarch %{ix86}
%define vbox_platform linux.x86
%endif
%ifarch x86_64
%define vbox_platform linux.amd64
%endif

# remove me for versions > 1.6.4
%define broken_tunctl 0

# nuke vbox-specific dependencies
%define _provides_exceptions ^VBox
%define _requires_exceptions ^VBox

Summary:	A general-purpose full virtualizer for x86 hardware
Name:		virtualbox
Version:	%{version}
Release:	%{release}
Source0:	http://virtualbox.org/download/%ver/%{srcname}.tar.bz2
Source2:	virtualbox.init
Source3:	98vboxadd-xclient
Source4:	60-vboxadd.perms
Source10:	virtualbox.png
Source11:	virtualbox.16.png
Source12:	virtualbox.48.png
Patch0:		VirtualBox-1.6.2-mdvconfig.patch
Patch1:		VirtualBox-1.5.4_OSE-libpath.patch
Patch2:		VirtualBox-1.5.6_OSE-kernelrelease.patch
Patch4:		VirtualBox-1.6.0_OSE-futex.patch
Patch5:		VirtualBox-1.6.2_OSE-fix-timesync-req.patch
# (fc) 1.6.0-2mdv fix initscript name in VBox.sh script
Patch6:		VirtualBox-1.6.0_OSE-initscriptname.patch
# (fc) 2.0.0-2mdv fix QT4 detection on x86-64 on Mdv 2008.1
Patch7:		VirtualBox-2.0.0-mdv20081.patch
# (fc) 2.0.2-2mdv disable version check at startup
Patch8:		VirtualBox-2.0.0-disableversioncheck.patch
License:	GPL
Group:		Emulators
Url:		http://www.virtualbox.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
ExclusiveArch:	%{ix86} x86_64
Requires(post):   rpm-helper
Requires(preun):  rpm-helper
Requires(postun): rpm-helper
%if %{mdkversion} >= 200800
Requires:	kmod(vboxdrv) = %{version}
%else
Requires:	dkms-%{name} = %{version}-%{release}
%endif
%if %{broken_tunctl}
Requires:	tunctl
%endif
Conflicts:	dkms-%{name} <= 1.5.0-%{mkrel 4}
BuildRequires:	dev86, iasl
BuildRequires:	zlib-devel
%if %{mdkversion} >= 200700
BuildRequires:	libxcursor-devel
BuildRequires:	libxmu-devel
%else
BuildRequires:	X11-devel
%endif
BuildRequires:	SDL-devel, libqt4-devel
BuildRequires:  qt4-linguist
BuildRequires:	libIDL-devel, libext2fs-devel
BuildRequires:	libxslt-proc, libxslt-devel, libxerces-c-devel, libxalan-c-devel >= 1.10
BuildRequires:	hal-devel, libxt-devel, libstdc++-static-devel
BuildRequires:  python-devel
%if %{mdkversion} >= 200810
BuildRequires:	pulseaudio-devel
%endif
%if %{mdkversion} >= 200800
BuildRequires:	kernel-devel-latest
%else
BuildRequires:	kernel-source
%endif
%if %{mdkversion} >= 200900
BuildRequires:	gcc4.2
%endif

%description
VirtualBox Open Source Edition (OSE) is a general-purpose full
virtualizer for x86 hardware.

%package -n	dkms-%{name}
Summary:	VirtualBox OSE kernel module
Group:		System/Kernel and hardware
Requires(post):	  dkms
Requires(preun):  dkms

%description -n dkms-%{name}
Kernel support for VirtualBox OSE.

%if %{build_additions}
%package 	guest-additions
Summary:	Additions for VirtualBox OSE guest systems
Group:		Emulators
%if %{mdkversion} >= 200800
Requires:	kmod(vboxadd)
Requires:	kmod(vboxvfs)
%else
Requires:	dkms-vboxadd = %{version}-%{release}
Requires:	dkms-vboxvfs = %{version}-%{release}
%endif
Requires:	x11-driver-input-vboxmouse
Requires:	x11-driver-video-vboxvideo
Requires(post):   rpm-helper
Requires(preun):  rpm-helper

%description    guest-additions
This packages contains additions for VirtualBox OSE guest systems.
It allows to share files with the host system, copy/paste between
guest and host, and sync time with host.

%package -n	dkms-vboxadd
Summary:	Kernel module for VirtualBox OSE additions
Group:		System/Kernel and hardware
Requires(post):	  dkms
Requires(preun):  dkms

%description -n dkms-vboxadd
Kernel module for VirtualBox OSE additions.

%package -n	dkms-vboxvfs
Summary:	Kernel module for VirtualBox OSE VFS
Group:		System/Kernel and hardware
Requires(post):	  dkms
Requires(preun):  dkms

%description -n dkms-vboxvfs
Kernel module for VirtualBox OSE VFS.

%package -n	x11-driver-input-vboxmouse
Summary:	The X.org driver for mouse in VirtualBox guests
Group:		System/X11
Suggests:	virtualbox-guest-additions

%description -n x11-driver-input-vboxmouse
The X.org driver for mouse in VirtualBox guests

%package -n	x11-driver-video-vboxvideo
Summary:	The X.org driver for video in VirtualBox guests
Group:		System/X11
Suggests:	virtualbox-guest-additions

%description -n x11-driver-video-vboxvideo
The X.org driver for video in VirtualBox guests
%endif

%prep
%setup -q -n %{distname}
%patch0 -p1 -b .mdvconfig
%patch1 -p1 -b .libpath
%patch2 -p1 -b .kernelrelease
%patch4 -p1 -b .futex
%patch5 -p1 -b .fix-timesync-req
%patch6 -p1 -b .initscriptname
%if %{mdkversion} < 200900
%patch7 -p1 -b .mdv20081
%endif
%patch8 -p1 -b .versioncheck

%if %{broken_tunctl}
# 1.6.4 build fix (OSE tarball is missing Makefile.kmk files)
# by building tunctl:
#   svn cat http://virtualbox.org/svn/vbox/trunk/src/apps/Makefile.kmk > src/apps/Makefile.kmk
#   svn cat http://virtualbox.org/svn/vbox/trunk/src/apps/tunctl/Makefile.kmk > src/apps/tunctl/Makefile.kmk
#   sed -ie s/SUB_DEPTH/DEPTH/ src/apps/Makefile.kmk
# by removing tunctl
if [ -e src/apps ]; then
   [ -e src/apps/Makefile.kmk ] && exit 1
   rm -rf src/apps
fi
# remove this block and broken_tunctl hack when updating to > 1.6.4
%endif

rm -rf fake-linux/
cp -a $(ls -1dtr /usr/src/linux-* | tail -n 1) fake-linux

%build
make -C fake-linux prepare
export LIBPATH_LIB="%{_lib}"
./configure --disable-qt3 \
%if %{mdkversion} >= 200900
 --with-gcc-compat=gcc4.2 \
%endif
 --with-linux=$PWD/fake-linux \
%if %{mdkversion} <= 200800 
 --disable-pulse
%endif

%if !%{build_additions}
sed -rie 's/(VBOX_WITH_LINUX_ADDITIONS\s+:=\s+).*/\1/' AutoConfig.kmk
echo VBOX_WITHOUT_ADDITIONS=1 > LocalConfig.kmk
%endif

. ./env.sh
kmk %_smp_mflags all

%install
rm -rf %{buildroot}

# install vbox components
mkdir -p %{buildroot}%{vboxdir}
(cd out/%{vbox_platform}/release/bin && tar cf - --exclude=additions .) | \
(cd %{buildroot}%{vboxdir} && tar xf -)

# install service
mkdir -p %{buildroot}%{_initrddir}
install -m755 %{SOURCE2} %{buildroot}%{_initrddir}/%{name}

# install wrappers
mkdir -p %{buildroot}%{_sysconfdir}/vbox
cat > %{buildroot}%{_sysconfdir}/vbox/vbox.cfg << EOF
# VirtualBox installation directory
INSTALL_DIR="%{vboxdir}"
EOF
mkdir -p %{buildroot}%{_bindir}
ln -s %{vboxdir}/VBox.sh %{buildroot}%{_bindir}/%{oname}
ln -s %{vboxdir}/VBox.sh %{buildroot}%{_bindir}/VBoxManage
ln -s %{vboxdir}/VBox.sh %{buildroot}%{_bindir}/VBoxSDL
ln -s %{vboxdir}/VBox.sh %{buildroot}%{_bindir}/VBoxHeadless

%if %{broken_tunctl}
ln -sf tunctl %{buildroot}%{_bindir}/VBoxTunctl
%else
# move VBoxTunctl to bindir
mv %{buildroot}%{vboxdir}/VBoxTunctl %{buildroot}%{_bindir}/
%endif

# install VBoxAddIF / VBoxDeleteIF
install -m755 ./src/VBox/Installer/linux/VBoxAddIF.sh %{buildroot}%{_bindir}/VBoxTAP
ln -s VBoxTAP %{buildroot}/%{_bindir}/VBoxAddIF
ln -s VBoxTAP %{buildroot}/%{_bindir}/VBoxDeleteIF

install -d %{buildroot}/var/run/%{oname}

# install dkms sources
mkdir -p %{buildroot}%{_usr}/src/%{name}-%{version}-%{release}
mv %{buildroot}%{vboxdir}/src/* %{buildroot}%{_usr}/src/%{name}-%{version}-%{release}/
cat > %{buildroot}%{_usr}/src/%{name}-%{version}-%{release}/dkms.conf << EOF
PACKAGE_NAME=%{name}
PACKAGE_VERSION=%{version}-%{release}
DEST_MODULE_LOCATION[0]=/kernel/3rdparty/vbox
BUILT_MODULE_NAME[0]=%{kname}
AUTOINSTALL=yes
EOF

# install udev rules
mkdir -p %{buildroot}%{_sysconfdir}/udev/rules.d/
cat > %{buildroot}%{_sysconfdir}/udev/rules.d/%{name}.rules << EOF
KERNEL=="%{kname}", MODE="0666"
EOF

# install additions
%if %{build_additions}
install -m755 src/VBox/Additions/linux/installer/vboxadd-timesync.sh %{buildroot}%{_initrddir}/vboxadd-timesync
install -m755 src/VBox/Additions/x11/installer/VBoxRandR.sh %{buildroot}%{_bindir}/VBoxRandR

pushd out/%{vbox_platform}/release/bin/additions
  install -d %{buildroot}/sbin %{buildroot}%{_sbindir}
  install -m755 mountvboxsf %{buildroot}/sbin/mount.vboxsf
  install -m755 vboxadd-timesync %{buildroot}%{_sbindir}

  install -d %{buildroot}%{_sysconfdir}/security/console.perms.d/
  install -m644 %{SOURCE4} %{buildroot}%{_sysconfdir}/security/console.perms.d/

  install -d %{buildroot}%{_sysconfdir}/X11/xinit.d
  install -m755 VBoxClient %{buildroot}%{_bindir}
  install -m755 %{SOURCE3} %{buildroot}%{_sysconfdir}/X11/xinit.d

  install -d %{buildroot}%{_sysconfdir}/modprobe.preload.d
  cat > %{buildroot}%{_sysconfdir}/modprobe.preload.d/vbox-guest-additions << EOF
vboxadd
vboxvfs
EOF
  install -d %{buildroot}%{_libdir}/xorg/modules/{input,drivers}
%if %{mdkversion} >= 200810
  install vboxmouse_drv_14.so %{buildroot}%{_libdir}/xorg/modules/input/vboxmouse_drv.so
  install vboxvideo_drv_14.so %{buildroot}%{_libdir}/xorg/modules/drivers/vboxvideo_drv.so
%else
  install vboxmouse_drv_71.so %{buildroot}%{_libdir}/xorg/modules/input/vboxmouse_drv.so
 %if %{mdkversion} >= 200800
  install vboxvideo_drv_13.so %{buildroot}%{_libdir}/xorg/modules/drivers/vboxvideo_drv.so
 %else
  install vboxvideo_drv_71.so %{buildroot}%{_libdir}/xorg/modules/drivers/vboxvideo_drv.so
 %endif
%endif
  for kmod in vboxadd vboxvfs; do
    mkdir -p %{buildroot}%{_usr}/src/$kmod-%{version}-%{release}
    cp -a src/$kmod/* %{buildroot}%{_usr}/src/$kmod-%{version}-%{release}/
    cat > %{buildroot}%{_usr}/src/$kmod-%{version}-%{release}/dkms.conf << EOF
PACKAGE_NAME=$kmod
PACKAGE_VERSION=%{version}-%{release}
DEST_MODULE_LOCATION[0]=/kernel/3rdparty/vbox
AUTOINSTALL=yes
EOF
  done
popd
%endif

# install icons
mkdir -p %{buildroot}%{_iconsdir}
install -m644 %{SOURCE10} %{buildroot}%{_iconsdir}/%{name}.png
mkdir -p %{buildroot}%{_miconsdir}
install -m644 %{SOURCE11} %{buildroot}%{_miconsdir}/%{name}.png
mkdir -p %{buildroot}%{_liconsdir}
install -m644 %{SOURCE12} %{buildroot}%{_liconsdir}/%{name}.png

# install menu entries

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=VirtualBox OSE
Comment=Full virtualizer for x86 hardware
Exec=%{_bindir}/%{oname}
Icon=%{name}
Type=Application
Terminal=false
Categories=X-MandrivaLinux-MoreApplications-Emulators;Emulator;
EOF

# add missing makefile for kernel module
install -m644 src/VBox/HostDrivers/Support/linux/Makefile %{buildroot}%{_usr}/src/%{name}-%{version}-%{release}/

# remove unpackaged files
rm -rf %{buildroot}%{vboxdir}/{src,sdk,testcase}
rm  -f %{buildroot}%{vboxdir}/tst*

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 200900
%update_menus
%endif
%_post_service %{name}

%postun
%if %mdkversion < 200900
%clean_menus
%endif
if [ "$1" -ge "1" ]; then
  /sbin/service %{name} condrestart > /dev/null 2>&1 || :
fi

%preun
%_preun_service %{name}

%post -n dkms-%{name}
set -x
/usr/sbin/dkms --rpm_safe_upgrade add -m %{name} -v %{version}-%{release}
/usr/sbin/dkms --rpm_safe_upgrade build -m %{name} -v %{version}-%{release}
/usr/sbin/dkms --rpm_safe_upgrade install -m %{name} -v %{version}-%{release}
/sbin/modprobe %{kname} >/dev/null 2>&1 || :

%preun -n dkms-%{name}
# rmmod can fail
/sbin/rmmod %{kname} >/dev/null 2>&1
set -x
/usr/sbin/dkms --rpm_safe_upgrade remove -m %{name} -v %{version}-%{release} --all || :

%if %{build_additions}
%post guest-additions
%_post_service vboxadd-timesync

%preun guest-additions
%_preun_service vboxadd-timesync

%post -n dkms-vboxadd
set -x
/usr/sbin/dkms --rpm_safe_upgrade add -m vboxadd -v %{version}-%{release}
/usr/sbin/dkms --rpm_safe_upgrade build -m vboxadd -v %{version}-%{release}
/usr/sbin/dkms --rpm_safe_upgrade install -m vboxadd -v %{version}-%{release}
:

%preun -n dkms-vboxadd
set -x
/usr/sbin/dkms --rpm_safe_upgrade remove -m vboxadd -v %{version}-%{release} --all
:

%post -n dkms-vboxvfs
set -x
/usr/sbin/dkms --rpm_safe_upgrade add -m vboxvfs -v %{version}-%{release}
/usr/sbin/dkms --rpm_safe_upgrade build -m vboxvfs -v %{version}-%{release}
/usr/sbin/dkms --rpm_safe_upgrade install -m vboxvfs -v %{version}-%{release}
:

%preun -n dkms-vboxvfs
set -x
/usr/sbin/dkms --rpm_safe_upgrade remove -m vboxvfs -v %{version}-%{release} --all
:
%endif

%files
%defattr(-,root,root)
%config %{_sysconfdir}/vbox/vbox.cfg
%{_bindir}/%{oname}
%{_bindir}/VBoxManage
%{_bindir}/VBoxSDL
%{_bindir}/VBoxHeadless
%{_bindir}/VBoxAddIF
%{_bindir}/VBoxDeleteIF
%{_bindir}/VBoxTAP
%{_bindir}/VBoxTunctl
%dir %{vboxdir}
%{vboxdir}/*
%attr(4711,root,root) %{vboxdir}/VBoxHeadless
%attr(4711,root,root) %{vboxdir}/VBoxSDL
%attr(4711,root,root) %{vboxdir}/VirtualBox
# initscripts integration
%{_initrddir}/%{name}
%config %{_sysconfdir}/udev/rules.d/%{name}.rules
%dir /var/run/%{oname}
# desktop integration
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png
%{_datadir}/applications/mandriva-%{name}.desktop

%files -n dkms-%{name}
%defattr(-,root,root)
%dir %{_usr}/src/%{name}-%{version}-%{release}
%{_usr}/src/%{name}-%{version}-%{release}/*

%if %{build_additions}
%files guest-additions
%defattr(-,root,root)
/sbin/mount.vboxsf
%{_initrddir}/vboxadd-timesync
%{_sbindir}/vboxadd-timesync
%{_bindir}/VBoxClient
%{_bindir}/VBoxRandR
%{_sysconfdir}/security/console.perms.d/60-vboxadd.perms
%{_sysconfdir}/X11/xinit.d/98vboxadd-xclient
%{_sysconfdir}/modprobe.preload.d/vbox-guest-additions

%files -n x11-driver-input-vboxmouse
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/vboxmouse_drv.so

%files -n x11-driver-video-vboxvideo
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/vboxvideo_drv.so

%files -n dkms-vboxadd
%defattr(-,root,root)
%dir %{_usr}/src/vboxadd-%{version}-%{release}
%{_usr}/src/vboxadd-%{version}-%{release}/*

%files -n dkms-vboxvfs
%defattr(-,root,root)
%dir %{_usr}/src/vboxvfs-%{version}-%{release}
%{_usr}/src/vboxvfs-%{version}-%{release}/*
%endif


%changelog
* Mon Sep 15 2008 Frederic Crozat <fcrozat@mandriva.com> 2.0.2-2mdv2009.0
+ Revision: 284854
- Patch8: disable version check at startup

* Sat Sep 13 2008 Frederik Himpe <fhimpe@mandriva.org> 2.0.2-1mdv2009.0
+ Revision: 284544
- Update to bugfix update 2.0.2

* Tue Sep 09 2008 Olivier Blin <oblin@mandriva.com> 2.0.0-3mdv2009.0
+ Revision: 283015
- build guest additions on x86_64 too (#43593)

  + Frederic Crozat <fcrozat@mandriva.com>
    - Patch7: fix QT4 detection on x86-64 on Mandriva 2008.1

* Thu Sep 04 2008 Frederic Crozat <fcrozat@mandriva.com> 2.0.0-1mdv2009.0
+ Revision: 280850
- Fix BuildRequires
- Release 2.0.0
- Remove patches 3, 7 (merged upstream)

* Mon Sep 01 2008 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.6.4-4mdv2009.0
+ Revision: 278071
- Added patch to allow VirtualBox kernel module to build with
  Linux 2.6.27

  + Pixel <pixel@mandriva.com>
    - increase release number
    - use gcc4.2 to build the recompiler (not ported to gcc 4.3 yet)

* Wed Aug 06 2008 Olivier Blin <oblin@mandriva.com> 1.6.4-2mdv2009.0
+ Revision: 264273
- create /var/run/VirtualBox (#41963)
- use tunctl from the tunctl package while VBoxTunctl does not build

* Tue Aug 05 2008 Olivier Blin <oblin@mandriva.com> 1.6.4-1mdv2009.0
+ Revision: 264016
- do not include VBoxTunctl for now (build is broken in upstream tarball)
- rediff misc_register patch (the register part has been implemented upstream, I should submit the deregister hunks)
- fix 1.6.4 build by not building tunctl (some Makefile.kmk are missing)
- 1.6.4

* Tue Jul 29 2008 Frederic Crozat <fcrozat@mandriva.com> 1.6.2-2mdv2009.0
+ Revision: 252777
- Don't use gcc 3.3 for build on 2008.1 or earlier

* Wed Jul 09 2008 Olivier Blin <oblin@mandriva.com> 1.6.2-1mdv2009.0
+ Revision: 232889
- set again linux sources path in configure
- use gcc 3.3 to build the recompiler (not ported to gcc 4.3 yet)
- use kernel-devel-latest instead of kernel-source-latest
- use a prepared copy of the linux tree (for linux/bounds.h)

  + Frederic Crozat <fcrozat@mandriva.com>
    - Release 1.6.2
    - Regenerate patch5
    - Fix duplicated line in specfile

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri May 16 2008 Frederic Crozat <fcrozat@mandriva.com> 1.6.0-4mdv2009.0
+ Revision: 208160
- Fix seamless mode in guest additions subpackage

* Thu May 15 2008 Anssi Hannula <anssi@mandriva.org> 1.6.0-3mdv2009.0
+ Revision: 207692
- rename VBoxAddIF.sh and VBoxDeleteIF.sh to VBoxAddIF and VBoxDeleteIF
  to match original names and documentation

* Wed May 14 2008 Frederic Crozat <fcrozat@mandriva.com> 1.6.0-2mdv2009.0
+ Revision: 207235
- Replace source1 with patch 6 (use up to date VBox.sh script)
- Ensure VBoxAddIF/VBoxDeleteIF scripts are packaged, as well as VBoxTunctl (Mdv bug #40769)
- package VBoxHeadless (Mdv bug #40771)

* Fri May 09 2008 Olivier Blin <oblin@mandriva.com> 1.6.0-1mdv2009.0
+ Revision: 205313
- try harder to disable additions on x86_64
- buildrequire libxslt-devel
- adapt to vboxadd-xclient being renamed as VBoxClient
- rediff futex patch
- rediff misc_register patch
- 1.6.0
- revert BUILT_MODULE_NAME addition, the bug is fixed in dkms

  + Anssi Hannula <anssi@mandriva.org>
    - add BUILT_MODULE_NAME to dkms.conf of vboxadd and vboxvfs (fixes DKMS
      error)

* Tue Feb 26 2008 Olivier Blin <oblin@mandriva.com> 1.5.6-1mdv2008.1
+ Revision: 175619
- 1.5.6
- rediff KERNELRELEASE patch

* Tue Feb 26 2008 Olivier Blin <oblin@mandriva.com> 1.5.4-5mdv2008.1
+ Revision: 175610
- try to start dkms instead of vboxadd in vboxadd-timesync service (since modules are loaded from modprobe.preload.d, #36728)

* Fri Feb 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.5.4-4mdv2008.1
+ Revision: 163970
- drop old menu

  + Frederic Crozat <fcrozat@mandriva.com>
    - Really disable pulseaudio support on 2008.0 or older

* Thu Jan 10 2008 Frederic Crozat <fcrozat@mandriva.com> 1.5.4-3mdv2008.1
+ Revision: 147602
- Use correct version of x11 mouse and video additional driver when used on 2008.1 (xorg 1.4) and 2008.0
- Only build pulseaudio support for 2008.1

* Wed Jan 09 2008 Olivier Blin <oblin@mandriva.com> 1.5.4-2mdv2008.1
+ Revision: 147006
- fix dkms build for kernels different from running kernel

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 1.5.4-1mdv2008.1
+ Revision: 142711
- buildrequire pulseaudio-devel
- rediff libpath patch
- remove 2.6.24 build fix, fixed upstream
- 1.5.4
- restore BuildRoot

  + Pascal Terjan <pterjan@mandriva.org>
    - Switch to Debian patch for 2.6.24
    - Re-create the 2.6.24 patch, some bits got lost

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - kill explicit icon extension

  + Giuseppe Ghibò <ghibo@mandriva.com>
    - Use kernel-source-latest in BuildRequires as conditional.
    - Add conditional build flags for older release.
    - Let Patch5 conditional.

* Fri Nov 30 2007 Pascal Terjan <pterjan@mandriva.org> 1.5.2-3mdv2008.1
+ Revision: 114076
- Improve 2.6.24 patch so that it should still build with older kernels

* Fri Nov 30 2007 Pascal Terjan <pterjan@mandriva.org> 1.5.2-2mdv2008.1
+ Revision: 114047
- Fix other parts to build with 2.6.24
- Fix vboxdrv for 2.6.24

* Tue Nov 13 2007 Olivier Blin <oblin@mandriva.com> 1.5.2-1mdv2008.1
+ Revision: 108363
- remove keyboards patch (was from upstream svn)
- rediff kernelrelease patch
- rediff libpath patch
- 1.5.2

* Thu Oct 04 2007 Olivier Blin <oblin@mandriva.com> 1.5.0-6mdv2008.0
+ Revision: 95447
- really apply misc_register patch (so that vboxadd devices are automatically created)
- add release in dkms PACKAGE_VERSION to ease upgrades

* Sat Sep 29 2007 Olivier Blin <oblin@mandriva.com> 1.5.0-5mdv2008.0
+ Revision: 93837
- require kmod(vboxdrv) instead of dkms package
- do not mark initscript as config file
- move initscripts and udev rules out of dkms package (so that it works when using dkms prebuilt modules)

* Sat Sep 29 2007 Olivier Blin <oblin@mandriva.com> 1.5.0-4mdv2008.0
+ Revision: 93812
- add vboxadd-timesync service
- add pam_console perms file to assign vboxadd device to console user
- use misc_register() to register vboxadd device so that /dev/vboxadd gets created automatically by udev

* Fri Sep 28 2007 Olivier Blin <oblin@mandriva.com> 1.5.0-3mdv2008.0
+ Revision: 93770
- add vboxadd-xclient xinit.d script
- release new additions, but we still need to fix mknod for vboxadd
  (or use device_create() in kernel module), set console perms for
  vboxadd in console.perms.d, and add timesync initscript
- make guest additions package require X11 drivers
- make x11 driver packages suggest virtualbox-guest-additions
- add virtualbox-guest-additions package (with xclient, timesync, mount.vboxsf)
- add dkms-vboxadd and dkms-vboxvfs packages

* Fri Sep 28 2007 Olivier Blin <oblin@mandriva.com> 1.5.0-2mdv2008.0
+ Revision: 93534
- build additions on ix86 only
- fix support for Brazilian, Belgian, US intl and US dvorak keyboards and add support for multimedia keys (from upstream SVN)
- buildrequire libstdc++-static-devel
- buildrequire libxt-devel
- buildrequire kernel-source-latest, since iurt/urpmi don't install latest kernel-source automatically
- buildrequire kernel-source
- package mouse guest addition in x11-driver-input-vboxmouse
- package video guest addition in x11-driver-video-vboxvideo
- build VirtualBox additions

* Mon Sep 03 2007 Olivier Blin <oblin@mandriva.com> 1.5.0-1mdv2008.0
+ Revision: 78607
- drop libstdc++5 BuildRequires
- drop unapplied x86_64 NMI watchdog disabling patch (merged upstream)
- 1.5.0
- rediff mdvconfig patch

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Fri Jun 08 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.4.0-1mdv2008.0
+ Revision: 37085
- from Jos?\195?\169 Melo <mmodem00@gmail.com>:
  	o 1.4.0
  	o update patch:2 since is needed to load (modprobe) vbox driver in kernel-2.6.17
  	o remove patch1 since is becomes obsolete with this new version,and continues installing and running stable no matter if is kernel-2.6.17 or greater
  	o add missing buildrequire hal-devel


* Thu Mar 15 2007 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.3.8-1mdv2007.1
+ Revision: 144313
- add should-start: dkms to initscript (#29523)
- 1.3.8
  * hard reset network device on reboot
  * fix issues with IBM JVM 1.4.2 in Linux guests
  * add support for X.org 7.2.x in Linux guest additions

* Fri Mar 02 2007 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.3.6-1mdv2007.1
+ Revision: 131492
- disable NMIs on Core 2 platforms too
- 1.3.6
  * fix some GUI issues
  * fix OpenBSD 4.0 support
  * fix CD/DVD-ROM detection in Windows Vista guests
  * fix networking issues with Windows NT 4.0 guests
  * fix some ALSA problems that could cause system reboots

* Mon Feb 12 2007 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.3.4-1mdv2007.1
+ Revision: 119895
- 1.3.4

* Mon Feb 12 2007 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.3.3.20070209-1mdv2007.1
+ Revision: 119017
- SVN updates (2007/02/09):
  * additional 64-bit fixes
  * asynchronous packets transmission in NIC code

* Sat Feb 03 2007 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.3.3.20070202-1mdv2007.1
+ Revision: 116064
- various 64-bit fixes
- updates from SVN (2007/02/02):
  * initial 64-bit host support
  * fix IDE for Open Solaris 10
  * add VDI compacting to the GUI

* Sat Jan 27 2007 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.3.3-1mdv2007.1
+ Revision: 114276
- initial mandriva linux package


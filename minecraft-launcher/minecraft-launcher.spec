Name:           minecraft-launcher
Summary:        Official Minecraft Launcher (bootstrap)
License:        LicenseRef-Proprietary=https://www.minecraft.net/en-us/eula
URL:            https://www.minecraft.net/
#		https://www.minecraft.net/en-us/download

# this version was released on "2022-03-23T23:03:04+00:00
Version:        1.0.1221
Release:        1%{?dist}

%global         debug_package   %{nil}

Source0:        https://launcher.mojang.com/download/linux/x86_64/minecraft-launcher_%{version}.tar.gz
Nosource:       0
Source1:        https://launcher.mojang.com/download/minecraft-launcher.svg
Nosource:       1
Source2:        minecraft-launcher.desktop
Source3:        minecraft-launcher.metainfo.xml
Source4:        https://www.minecraft.net/en-us/eula#/EULA.html
Nosource:       4


BuildArch:      x86_64
ExclusiveArch:  x86_64

# Based on ldd of the minecraft_launcher
Requires: atk
Requires: at-spi2-atk
Requires: at-spi2-core
Requires: bzip2-libs
Requires: cairo
Requires: cairo-gobject
Requires: dbus-libs
Requires: fontconfig
Requires: freetype
Requires: fribidi
Requires: gdk-pixbuf2
Requires: glib2
Requires: glibc
Requires: graphite2
Requires: gtk3
Requires: harfbuzz
Requires: json-glib
Requires: libblkid
Requires: libbrotli
Requires: libcap
Requires: libcloudproviders
Requires: libdatrie
Requires: libepoxy
Requires: libffi
Requires: libgcc
Requires: libjpeg-turbo
Requires: libmount
Requires: libpng
Requires: libselinux
Requires: libstdc++
Requires: libthai
Requires: libtracker-sparql
Requires: libwayland-client
Requires: libwayland-cursor
Requires: libwayland-egl
Requires: libX11
Requires: libXau
Requires: libxcb
Requires: libXcomposite
Requires: libXcursor
Requires: libXdamage
Requires: libXext
Requires: libXfixes
Requires: libXi
Requires: libXinerama
Requires: libxkbcommon
Requires: libxml2
Requires: libXrandr
Requires: libXrender
Requires: libzstd
Requires: lz4-libs
Requires: pango
Requires: pcre2
Requires: pixman
Requires: sqlite-libs
Requires: systemd-libs
Requires: xz-libs
Requires: zlib-ng-compat

# Based on : /usr/bin/strings minecraft-launcher | grep -e '"libraries"' | \
# jq '.libraries[].url'

# https://github.com/HowardHinnant/date
# License: MIT
Provides:       bundled(HowardHinnant-date)

# https://github.com/martinmoene/string-view-lite/
# License: Boost Software License v1
Provides:       bundled(string-view-lite)

# https://github.com/jarro2783/cxxopts
Provides:       bundled(cxxopts)

# https://github.com/mvorbrodt/blog/blob/master/src/base64.hpp
Provides:       bundled(base64)

# https://www.7-zip.org/sdk.html
# License: public domain
Provides:       bundled(lzma)

# https://github.com/open-source-parsers/jsoncpp/
Provides:       bundled(jsoncpp)

# https://github.com/catchorg/Catch2
Provides:       bundled(Catch2)

# https://github.com/martinmoene/optional-lite
Provides:       bundled(optional-lite)

# https://github.com/scottt/debugbreak/
Provides:       bundled(debugbreak)

# https://github.com/jedisct1/libhydrogen/
# License: ISC
Provides:       bundled(libhydrogen)

# https://sourceforge.net/projects/utfcpp/
Provides:       bundled(utfcpp)


%description
This package delivers the bootstrap version of the launcher,
the minimum client to update, maintain and run the actuall
game launcher and game content from Mojang / Microsoft.
The updated version of the launcher is after login and
and license check downloaded to user's home directory
to ~/.minecraft folder.

Playing the game requires a valid game license
to connect to online resources of Mojang/Microsoft.
For more information check the
https://www.minecraft.net/en-us/eula


%prep
# ======================= prep =======================================
%autosetup -n minecraft-launcher
# These files are not in the minecraft-launcher.tar.gz distribution for other Linux
# Hopefully one day it will be added there
# SVG icon
cp -f %{SOURCE1} ./
# *.desktop file is missing in the tar.gz distribution for other Linux
cp -f %{SOURCE2} ./
# appdata metainfo
cp -f %{SOURCE3} ./
# EULA.html license from https://www.minecraft.net/en-us/eula
cp -f %{SOURCE4} ./


%build
# ======================= build ======================================
echo Do nothing for the build

%install
# ======================= install ====================================
# Install binary
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 minecraft-launcher %{buildroot}%{_bindir}/minecraft-launcher
ln -s minecraft-launcher %{buildroot}%{_bindir}/minecraft

# Install application launcher icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m 0644 minecraft-launcher.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/minecraft-launcher.svg

# Install application launcher desktop file
mkdir -p %{buildroot}%{_datadir}/applications/
install -p -m 0644 minecraft-launcher.desktop %{buildroot}%{_datadir}/applications/minecraft-launcher.desktop

# Install metadata for Gnome Software
mkdir -p %{buildroot}%{_datadir}/metainfo/
install -p -m 0644 minecraft-launcher.metainfo.xml %{buildroot}%{_datadir}/metainfo/minecraft-launcher.metainfo.xml

%post
update-desktop-database &> /dev/null ||:
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :



%postun
update-desktop-database &> /dev/null ||:
if [ $1 -eq 0 ] ; then
        touch --no-create %{_datadir}/icons/hicolor &>/dev/null
        gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi



%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/minecraft-launcher.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/minecraft-launcher.desktop





%files
# ======================= files ======================================
#%doc
%license EULA.html
%{_bindir}/minecraft
%{_bindir}/minecraft-launcher
%{_datadir}/applications/minecraft-launcher.desktop
%{_datadir}/icons/hicolor/scalable/apps/minecraft-launcher.svg
%{_datadir}/metainfo/minecraft-launcher.metainfo.xml

%changelog
* Wed Mar 23 2022 Mojang <info@mojang.com> - 1.0.1221-1
- initial minecraft launcher 1.0.1221 for Other linux


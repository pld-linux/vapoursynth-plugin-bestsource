#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Vapoursynth plugin to access audio and video via FFmpeg library
Summary(pl.UTF-8):	Wtyczka Vapoursynth pozwalająca na dostęp do dźwięku i obrazu poprzez bibliotekę FFmpeg
Name:		vapoursynth-plugin-bestsource
# >= 9 requires ffmpeg 7+
Version:	8
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/vapoursynth/bestsource/releases
Source0:	https://github.com/vapoursynth/bestsource/archive/R%{version}/bestsource-R%{version}.tar.gz
# Source0-md5:	827740eaa706533f587e154b37d509aa
Patch0:		bestsource-system-libp2p.patch
Patch1:		bestsource-system-AviSynthPlus.patch
URL:		https://github.com/vapoursynth/bestsource
BuildRequires:	AviSynthPlus-devel
# libavcodec >= 60.31.0, libavformat >= 60.16.0, libavutil >= 58.29.0
BuildRequires:	ffmpeg-devel >= 6.0
BuildRequires:	libp2p-devel >= 0-0.20240415
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	meson >= 0.53.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	vapoursynth-devel >= 55
BuildRequires:	xxHash-devel
Requires:	bestsource = %{version}-%{release}
Requires:	vapoursynth >= 55
Obsoletes:	vapoursynth-plugin-bestaudiosource < 2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vapoursynth plugin to access audio and video via FFmpeg library.

%description -l pl.UTF-8
Wtyczka Vapoursynth pozwalająca na dostęp do dźwięku i obrazu poprzez
bibliotekę FFmpeg.

%package -n bestsource
Summary:	Super great audio/video source and FFmpeg wrapper
Summary(pl.UTF-8):	Bardzo uniwersalne źródło dźwięku/obrazu i opakowanie FFmpeg
Group:		Libraries
Requires:	ffmpeg-libs >= 6.0.0
Requires:	libp2p >= 0-0.20240415

%description -n bestsource
Super great audio/video source and FFmpeg wrapper.

%description -n bestsource -l pl.UTF-8
Bardzo uniwersalne źródło dźwięku/obrazu i opakowanie FFmpeg.

%package -n bestsource-devel
Summary:	Header files for bestsource library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki bestsource
Group:		Development/Libraries
Requires:	bestsource = %{version}-%{release}
Requires:	ffmpeg-devel >= 6.0
Requires:	xxHash-devel

%description -n bestsource-devel
Header files for bestsource library.

%description -n bestsource-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki bestsource.

%package -n bestsource-static
Summary:	Static bestsource library
Summary(pl.UTF-8):	Statyczna biblioteka bestsource
Group:		Development/Libraries
Requires:	bestsource-devel = %{version}-%{release}

%description -n bestsource-static
Static bestsource library.

%description -n bestsource-static -l pl.UTF-8
Statyczna biblioteka bestsource.

%prep
%setup -q -n bestsource-R%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%meson \
	%{!?with_static_libs:--default-library=shared}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_libdir}/vapoursynth/bestsource.so

%files -n bestsource
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbestsource.so

%files -n bestsource-devel
%defattr(644,root,root,755)
%{_includedir}/bestsource
%{_pkgconfigdir}/bestsource.pc

%if %{with static_libs}
%files -n bestsource-static
%defattr(644,root,root,755)
%{_libdir}/libbestsource.a
%endif

Summary:	Vapoursynth plugin to access audio and video via FFmpeg library
Summary(pl.UTF-8):	Wtyczka Vapoursynth pozwalająca na dostęp do dźwięku i obrazu poprzez bibliotekę FFmpeg
Name:		vapoursynth-plugin-bestsource
# src/version.h says 0.9?
Version:	0
%define	snap	20230419
%define	gitref	d917b26767c41851c50ccad29d8d126e139a7822
%define	rel	2
Release:	0.%{snap}.%{rel}
License:	MIT
Group:		Libraries
Source0:	https://github.com/vapoursynth/bestsource/archive/%{gitref}/bestsource-%{gitref}.tar.gz
# Source0-md5:	b3afb3b36ed0a7ab457bd1d44927b1a0
Patch0:		bestsource-system-libp2p.patch
# remove after switching to ffmpeg 5.x, bump BR then
Patch1:		bestsource-ffmpeg4.patch
URL:		https://github.com/vapoursynth/bestsource
# libavcodec >= 58.18.0, libavformat >= 58.12.0
BuildRequires:	ffmpeg-devel >= 4.1
BuildRequires:	jansson-devel >= 2.7
BuildRequires:	libp2p-devel
BuildRequires:	libstdc++-devel
BuildRequires:	meson >= 0.48.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	vapoursynth-devel >= 55
Requires:	ffmpeg-libs >= 4.1
Requires:	jansson >= 2.7
Requires:	vapoursynth >= 55
Obsoletes:	vapoursynth-plugin-bestaudiosource < 2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vapoursynth plugin to access audio and video via FFmpeg library.

%description -l pl.UTF-8
Wtyczka Vapoursynth pozwalająca na dostęp do dźwięku i obrazu poprzez
bibliotekę FFmpeg.

%prep
%setup -q -n bestsource-%{gitref}
%patch0 -p1
%patch1 -p1

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_libdir}/vapoursynth/libbestsource.so

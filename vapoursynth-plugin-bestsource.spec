#
# Conditional build:
%bcond_with	vulkan	# Vulkan+glslang for GPU decoding (ffmpeg 9.1)

Summary:	Vapoursynth plugin to access audio and video via FFmpeg library
Summary(pl.UTF-8):	Wtyczka Vapoursynth pozwalająca na dostęp do dźwięku i obrazu poprzez bibliotekę FFmpeg
Name:		vapoursynth-plugin-bestsource
Version:	23
Release:	2
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/vapoursynth/bestsource/releases
Source0:	https://github.com/vapoursynth/bestsource/archive/R%{version}/bestsource-R%{version}.tar.gz
# Source0-md5:	d8078bad01ad4d4bdceb7231f0c87a6d
Patch0:		bestsource-system-libp2p.patch
Patch1:		bestsource-system-AviSynthPlus.patch
URL:		https://github.com/vapoursynth/bestsource
BuildRequires:	AviSynthPlus-devel
%{?with_vulkan:BuildRequires:	Vulkan-Headers >= 1.4}
# libavcodec >= 63.1.0, libavformat >= 63.1.0, libavutil >= 61.1.0 [61.6.0 for GPU]
BuildRequires:	ffmpeg-devel >= 9.0
%{?with_vulkan:BuildRequires:	ffmpeg-devel >= 9.1}
# glslangValidator
%{?with_vulkan:BuildRequires:	glslang}
BuildRequires:	libp2p-devel >= 0-0.20240415
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	meson >= 1.2.3
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.12
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	vapoursynth-devel >= 80
BuildRequires:	xxHash-devel
Requires:	vapoursynth%{?_isa} >= 80
Obsoletes:	vapoursynth-plugin-bestaudiosource < 2
Obsoletes:	bestsource < 23
Obsoletes:	bestsource-devel < 23
Obsoletes:	bestsource-static < 23
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vapoursynth plugin to access audio and video via FFmpeg library.

%description -l pl.UTF-8
Wtyczka Vapoursynth pozwalająca na dostęp do dźwięku i obrazu poprzez
bibliotekę FFmpeg.

%prep
%setup -q -n bestsource-R%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%meson \
	--default-library=shared \
	-Denable_gpu=%{__enabled_disabled vulkan}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitedir}/vapoursynth/plugins/libbestsource.so

%global tl_name quran-de
%global tl_revision 74874

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.21
Release:	%{tl_revision}.1
Summary:	German translations to the quran package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/quran-de
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/quran-de.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/quran-de.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is prepared for typesetting some German translations of the
Holy Quran. It adds three more German translations to the quran package.


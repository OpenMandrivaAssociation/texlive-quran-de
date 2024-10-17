Name:		texlive-quran-de
Version:	54191
Release:	2
Summary:	German translations to the quran package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/quran-de
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quran-de.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quran-de.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is prepared for typesetting some German
translations of the Holy Quran. It adds three more German
translations to the quran package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/quran-de
%doc %{_texmfdistdir}/doc/xelatex/quran-de

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

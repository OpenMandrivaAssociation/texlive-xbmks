Name:		texlive-xbmks
Version:	53448
Release:	1
Summary:	Create a cross-document bookmark tree
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xbmks
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xbmks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xbmks.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xbmks.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines the concept of a document bundle, which is
a collection of documents that are to be built separately, but
have a common bookmark tree. The only options are driver
options, these are dvips (Acrobat Distiller or ps2pdf these can
be used as the PDF creator), pdfLaTeX (and LuaLaTeX, which is
treated the same as pdfLaTeX), and XeLaTeX. The package
auto-detects pdfLaTeX and XeLaTeX, and dvips is the default, so
there is actually no need to pass the driver option.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/xbmks
%{_texmfdistdir}/tex/latex/xbmks
%doc %{_texmfdistdir}/doc/latex/xbmks

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

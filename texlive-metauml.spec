Name:		texlive-metauml
Version:	49923
Release:	1
Summary:	MetaPost library for typesetting UML diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/metauml
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metauml.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metauml.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
MetaUML is a MetaPost library for typesetting UML diagrams,
which provides a usable, human-friendly textual notation for
UML, offering now support for class, package, activity, state,
and use case diagrams.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/metauml
%doc %{_texmfdistdir}/doc/metapost/metauml

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}

%global tl_name metauml
%global tl_revision 49923

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2.6
Release:	%{tl_revision}.1
Summary:	MetaPost library for typesetting UML diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/metauml
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metauml.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metauml.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
MetaUML is a MetaPost library for typesetting UML diagrams, which
provides a usable, human-friendly textual notation for UML, offering now
support for class, package, activity, state, and use case diagrams.


# revision 19692
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/metauml
# catalog-date 2010-07-30 13:14:18 +0200
# catalog-license gpl
# catalog-version 0.2.5
Name:		texlive-metauml
Version:	0.2.5
Release:	12
Summary:	MetaPost library for typesetting UML diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/metauml
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metauml.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metauml.doc.tar.xz
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
%{_texmfdistdir}/metapost/metauml/metauml.mp
%{_texmfdistdir}/metapost/metauml/metauml_activity.mp
%{_texmfdistdir}/metapost/metauml/metauml_base.mp
%{_texmfdistdir}/metapost/metauml/metauml_behavioral_common.mp
%{_texmfdistdir}/metapost/metauml/metauml_class.mp
%{_texmfdistdir}/metapost/metauml/metauml_class_assoc.mp
%{_texmfdistdir}/metapost/metauml/metauml_class_clipart.mp
%{_texmfdistdir}/metapost/metauml/metauml_class_relations.mp
%{_texmfdistdir}/metapost/metauml/metauml_component.mp
%{_texmfdistdir}/metapost/metauml/metauml_component_relations.mp
%{_texmfdistdir}/metapost/metauml/metauml_defaults.mp
%{_texmfdistdir}/metapost/metauml/metauml_instance.mp
%{_texmfdistdir}/metapost/metauml/metauml_links.mp
%{_texmfdistdir}/metapost/metauml/metauml_note.mp
%{_texmfdistdir}/metapost/metauml/metauml_package.mp
%{_texmfdistdir}/metapost/metauml/metauml_package_relations.mp
%{_texmfdistdir}/metapost/metauml/metauml_paths.mp
%{_texmfdistdir}/metapost/metauml/metauml_skin_simple.mp
%{_texmfdistdir}/metapost/metauml/metauml_state.mp
%{_texmfdistdir}/metapost/metauml/metauml_stereotype.mp
%{_texmfdistdir}/metapost/metauml/metauml_templates.mp
%{_texmfdistdir}/metapost/metauml/metauml_usecase.mp
%{_texmfdistdir}/metapost/metauml/metauml_usecase_clipart.mp
%{_texmfdistdir}/metapost/metauml/util_commons.mp
%{_texmfdistdir}/metapost/metauml/util_group.mp
%{_texmfdistdir}/metapost/metauml/util_infrastructure.mp
%{_texmfdistdir}/metapost/metauml/util_log.mp
%{_texmfdistdir}/metapost/metauml/util_margins.mp
%{_texmfdistdir}/metapost/metauml/util_object.mp
%{_texmfdistdir}/metapost/metauml/util_picture.mp
%{_texmfdistdir}/metapost/metauml/util_picture_stack.mp
%{_texmfdistdir}/metapost/metauml/util_positioning.mp
%{_texmfdistdir}/metapost/metauml/util_shade.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/README
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/activity.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/activity_diagrams.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/appetizer.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/boxes_vs_util.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/class.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/class_association.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/class_customization.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/class_customization2.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/class_diagrams.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/class_templates.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/cliparts.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/component.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/group.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/how-links-work.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/instance.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/mptextmp.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/mptrace.tmp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/note.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/object_stack.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/package.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/paths.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/paths_man.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/picture_info.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/picture_stack.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/positioning.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/properties.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/state.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/statemachine_diagrams.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_activity.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_class.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_class_qual_assoc.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_class_templates.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_component.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_font.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_group.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_instance.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_lars_issues.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_lowlevel.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_note.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_package.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_paths.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_picture.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_picture_stack.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_picture_tex_rendering.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_positioning.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_skins.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_skins_global_defaults.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_state.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/test_usecase.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/usecase.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/fig/usecase_diagrams.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/gnu-fdl.tex
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/macro.tex
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/metauml_manual.tex
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/my-bib.bib
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/test.mp
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual/test_suite.tex
%doc %{_texmfdistdir}/doc/metapost/metauml/metauml_manual_0.2.5.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2.5-2
+ Revision: 753930
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2.5-1
+ Revision: 719003
- texlive-metauml
- texlive-metauml
- texlive-metauml
- texlive-metauml


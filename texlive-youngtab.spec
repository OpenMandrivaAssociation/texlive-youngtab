%global tl_name youngtab
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Typeset Young-Tableaux
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/youngtab
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/youngtab.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/youngtab.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/youngtab.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package for typesetting Young-Tableaux, mathematical symbols for the
representations of groups, providing two macros, \yng(1) and \young(1)
to generate the whole Young-Tableau.


Name:		texlive-youngtab
Version:	56500
Release:	2
Summary:	Typeset Young-Tableaux
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/youngtab
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/youngtab.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/youngtab.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/youngtab.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package for typesetting Young-Tableaux, mathematical symbols
for the representations of groups, providing two macros,
\yng(1) and \young(1) to generate the whole Young-Tableaux.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/youngtab
%doc %{_texmfdistdir}/doc/generic/youngtab
#- source
%doc %{_texmfdistdir}/source/generic/youngtab

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

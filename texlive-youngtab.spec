# revision 17635
# category Package
# catalog-ctan /macros/latex/contrib/youngtab
# catalog-date 2010-03-30 14:47:00 +0200
# catalog-license lppl1
# catalog-version 1.1
Name:		texlive-youngtab
Version:	1.1
Release:	1
Summary:	Typeset Young-Tableaux
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/youngtab
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/youngtab.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/youngtab.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/youngtab.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A package for typesetting Young-Tableaux, mathematical symbols
for the representations of groups, providing two macros,
\yng(1) and \young(1) to generate the whole Young-Tableaux.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/youngtab/youngtab.sty
%doc %{_texmfdistdir}/doc/latex/youngtab/README
%doc %{_texmfdistdir}/doc/latex/youngtab/makeydoc
%doc %{_texmfdistdir}/doc/latex/youngtab/makeydoc.bat
%doc %{_texmfdistdir}/doc/latex/youngtab/youngtab.el
%doc %{_texmfdistdir}/doc/latex/youngtab/youngtab.pdf
%doc %{_texmfdistdir}/doc/latex/youngtab/youngtab.tex
#- source
%doc %{_texmfdistdir}/source/latex/youngtab/youngtab.dtx
%doc %{_texmfdistdir}/source/latex/youngtab/youngtab.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

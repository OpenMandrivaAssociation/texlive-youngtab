# revision 17635
# category Package
# catalog-ctan /macros/latex/contrib/youngtab
# catalog-date 2010-03-30 14:47:00 +0200
# catalog-license lppl1
# catalog-version 1.1
Name:		texlive-youngtab
Version:	1.1
Release:	7
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 757746
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 719967
- texlive-youngtab
- texlive-youngtab
- texlive-youngtab


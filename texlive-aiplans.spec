%global tl_name aiplans
%global tl_revision 74462

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0
Release:	%{tl_revision}.1
Summary:	A TikZ-based library for drawing POCL plans
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/aiplans
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aiplans.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aiplans.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This TikZ library is designed for generating diagrams related to
Automated Planning, a subdiscipline of Artificial Intelligence. It
allows users to define a "domain model" for actions, similar to PDDL and
HDDL used in hierarchical planning. The package is useful for
researchers and students to create diagrams that represent sequential
action sequences or partially ordered plans, including causal links and
ordering constraints (e.g., POCL plans). It is particularly suited for
presentations and scientific publications.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/aiplans
%dir %{_datadir}/texmf-dist/tex/latex/aiplans
%doc %{_datadir}/texmf-dist/doc/latex/aiplans/LICENSE.txt
%doc %{_datadir}/texmf-dist/doc/latex/aiplans/README.md
%doc %{_datadir}/texmf-dist/doc/latex/aiplans/README.pdf
%doc %{_datadir}/texmf-dist/doc/latex/aiplans/aiplans-Introduction.md
%doc %{_datadir}/texmf-dist/doc/latex/aiplans/aiplans-Introduction.pdf
%doc %{_datadir}/texmf-dist/doc/latex/aiplans/example-blocksworld.png
%{_datadir}/texmf-dist/tex/latex/aiplans/tikzlibraryaiplans.code.tex

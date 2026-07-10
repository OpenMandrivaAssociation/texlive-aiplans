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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
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


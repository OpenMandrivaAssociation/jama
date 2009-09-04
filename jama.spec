Name:		jama
Summary:	A Java Matrix Package
Version:	1.0.2
Release:	%mkrel 4
Source:		http://math.nist.gov/javanumerics/jama/Jama-%{version}.tar.gz
License:	Public Domain
URL:		http://math.nist.gov/javanumerics/jama/
Group:		Development/Java
BuildRoot:	%{_tmppath}/%{_basename}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	java-devel ant jpackage-utils java-rpmbuild
%description
JAMA is a basic linear algebra package for Java. It provides user-level
classes for constructing and manipulating real, dense matrices. It is
meant to provide sufficient functionality for routine problems, packaged
in a way that is natural and understandable to non-experts.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
%description javadoc
Javadoc for %{name}

%prep
%setup -q -c jama
find Jama -name '*.class' -exec rm -f {} \;

%{__mkdir} build

%{__cat} > build.xml <<EOF
<project name="Jama" basedir="." default="build-jar">
        <target name="build-jar">
                <javac srcdir="Jama" destdir="build" />
                <jar basedir="build" destfile="%{name}-%{version}.jar">
                        <fileset dir="build" includes="*/*.*"/>
                </jar>
        </target>
</project>
EOF

%{__cat} > LICENSE <<EOF
Downloaded from http://math.nist.gov/javanumerics/jama/Jama-%{version}.tar.gz
No license info in the archive, but we can read this on their website :

Copyright Notice  This software is a cooperative product of The
MathWorks and the National Institute of Standards and Technology (NIST)
which has been released to the public domain. Neither The MathWorks
nor NIST assumes any responsibility whatsoever for its use by other
parties, and makes no guarantees, expressed or implied, about its
quality, reliability, or any other characteristic.  
EOF

%build
%ant

%install
%{__rm} -Rf %{buildroot}
%{__install} -d %{buildroot}%{_javadir}
%{__install} -m 644 %{name}-%{version}.jar %{buildroot}%{_javadir}
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%{__install} -d %{buildroot}%{_javadocdir}
%{__cp} -a Jama/doc %{buildroot}%{_javadocdir}/%{name}-%{version}


%files
%doc LICENSE Jama/ChangeLog Jama/examples/MagicSquareExample.java
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}


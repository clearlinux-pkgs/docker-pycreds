#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : docker-pycreds
Version  : 0.4.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/c5/e6/d1f6c00b7221e2d7c4b470132c931325c8b22c51ca62417e300f5ce16009/docker-pycreds-0.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c5/e6/d1f6c00b7221e2d7c4b470132c931325c8b22c51ca62417e300f5ce16009/docker-pycreds-0.4.0.tar.gz
Summary  : Python bindings for the docker credentials store API
Group    : Development/Tools
License  : Apache-2.0
Requires: docker-pycreds-license = %{version}-%{release}
Requires: docker-pycreds-python = %{version}-%{release}
Requires: docker-pycreds-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3

%description
# docker-pycreds
[![CircleCI](https://circleci.com/gh/shin-/dockerpy-creds/tree/master.svg?style=svg)](https://circleci.com/gh/shin-/dockerpy-creds/tree/master)

%package license
Summary: license components for the docker-pycreds package.
Group: Default

%description license
license components for the docker-pycreds package.


%package python
Summary: python components for the docker-pycreds package.
Group: Default
Requires: docker-pycreds-python3 = %{version}-%{release}

%description python
python components for the docker-pycreds package.


%package python3
Summary: python3 components for the docker-pycreds package.
Group: Default
Requires: python3-core

%description python3
python3 components for the docker-pycreds package.


%prep
%setup -q -n docker-pycreds-0.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549922534
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/docker-pycreds
cp LICENSE %{buildroot}/usr/share/package-licenses/docker-pycreds/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/docker-pycreds/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

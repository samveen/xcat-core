%define version     2.13
Version: %{?version:%{version}}%{!?version:%(cat Version)}
Release: %{?release:%{release}}%{!?release:snap%(date +"%Y%m%d%H%M")}
%ifarch i386 i586 i686 x86
%define tarch x86
%endif
%ifarch x86_64
%define tarch x86_64
%endif
%ifarch ppc ppc64 ppc64le
%define tarch ppc64
%endif
BuildArch: noarch
%define name	xCAT-genesis-overlay-%{tarch}
%define __spec_install_post :
%define debug_package %{nil}
%define __prelink_undo_cmd %{nil}
# To fix the issue error: Arch dependent binaries in noarch package, the following line is needed on Fedora 23 ppc64
%define _binaries_in_noarch_packages_terminate_build   0
Epoch: 2
AutoReq: false
Prefix: /opt/xcat
AutoProv: false

Name:	 %{name}
Group: System/Utilities
License: Various (see individual packages for details)
Vendor: IBM Corp.
Summary: xCAT Genesis netboot image custom overlay
URL:	 https://xcat.org/
Source1: xCAT-genesis-overlay-%{tarch}.tar.bz2

Buildroot: %{_localstatedir}/tmp/xCAT-genesis
Packager: IBM Corp.
Requires: xCAT-genesis-base-%{tarch} >= %{version}

%Description
This package provides a custom overlay for extending the upstream xCAT genesis base package.

%Prep

%Build

%Install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
cd $RPM_BUILD_ROOT
tar jxf %{SOURCE1}
cd -

%post
echo "You are installing/updating xCAT-genesis-overlay package, so you'll probably need to run 'mknb <arch>' manually"

%postun
echo "If you are uninstalling just the xCAT-genesis-overlay package, then you should run 'mknb <arch>' to update the genesis image"

%Files
%defattr(-,root,root)
/opt/xcat/share/xcat/netboot/genesis/%{tarch}

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : neutron
Version  : 14.0.1
Release  : 82
URL      : http://tarballs.openstack.org/neutron/neutron-14.0.1.tar.gz
Source0  : http://tarballs.openstack.org/neutron/neutron-14.0.1.tar.gz
Source1  : neutron-dhcp-agent.service
Source2  : neutron-l3-agent.service
Source3  : neutron-linuxbridge-agent.service
Source4  : neutron-metadata-agent.service
Source5  : neutron-openvswitch-agent.service
Source6  : neutron-server.service
Source7  : neutron.tmpfiles
Source99 : http://tarballs.openstack.org/neutron/neutron-14.0.1.tar.gz.asc
Summary  : OpenStack Networking
Group    : Development/Tools
License  : Apache-2.0
Requires: neutron-bin = %{version}-%{release}
Requires: neutron-config = %{version}-%{release}
Requires: neutron-data = %{version}-%{release}
Requires: neutron-license = %{version}-%{release}
Requires: neutron-python = %{version}-%{release}
Requires: neutron-python3 = %{version}-%{release}
Requires: neutron-services = %{version}-%{release}
Requires: Jinja2
Requires: Paste
Requires: PasteDeploy
Requires: Routes
Requires: SQLAlchemy
Requires: WebOb
Requires: alembic
Requires: debtcollector
Requires: eventlet
Requires: httplib2
Requires: keystoneauth1
Requires: keystonemiddleware
Requires: netaddr
Requires: netifaces
Requires: neutron-lib
Requires: os-ken
Requires: os-xenapi
Requires: oslo.cache
Requires: oslo.concurrency
Requires: oslo.config
Requires: oslo.context
Requires: oslo.db
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.messaging
Requires: oslo.middleware
Requires: oslo.policy
Requires: oslo.privsep
Requires: oslo.reports
Requires: oslo.rootwrap
Requires: oslo.serialization
Requires: oslo.service
Requires: oslo.upgradecheck
Requires: oslo.utils
Requires: oslo.versionedobjects
Requires: osprofiler
Requires: ovs
Requires: ovsdbapp
Requires: pbr
Requires: pecan
Requires: psutil
Requires: pyroute2
Requires: python-designateclient
Requires: python-neutronclient
Requires: python-novaclient
Requires: requests
Requires: six
Requires: stevedore
Requires: tenacity
Requires: weakrefmethod
BuildRequires : Jinja2
BuildRequires : Paste
BuildRequires : PasteDeploy
BuildRequires : Routes
BuildRequires : SQLAlchemy
BuildRequires : WebOb
BuildRequires : alembic
BuildRequires : buildreq-distutils3
BuildRequires : debtcollector
BuildRequires : eventlet
BuildRequires : httplib2
BuildRequires : keystoneauth1
BuildRequires : keystonemiddleware
BuildRequires : netaddr
BuildRequires : netifaces
BuildRequires : neutron-lib
BuildRequires : os-ken
BuildRequires : os-xenapi
BuildRequires : oslo.cache
BuildRequires : oslo.concurrency
BuildRequires : oslo.config
BuildRequires : oslo.context
BuildRequires : oslo.db
BuildRequires : oslo.i18n
BuildRequires : oslo.log
BuildRequires : oslo.messaging
BuildRequires : oslo.middleware
BuildRequires : oslo.policy
BuildRequires : oslo.privsep
BuildRequires : oslo.reports
BuildRequires : oslo.rootwrap
BuildRequires : oslo.serialization
BuildRequires : oslo.service
BuildRequires : oslo.upgradecheck
BuildRequires : oslo.utils
BuildRequires : oslo.versionedobjects
BuildRequires : osprofiler
BuildRequires : ovs
BuildRequires : ovsdbapp
BuildRequires : pbr
BuildRequires : pecan
BuildRequires : psutil
BuildRequires : pyroute2
BuildRequires : python-designateclient
BuildRequires : python-neutronclient
BuildRequires : python-novaclient
BuildRequires : requests
BuildRequires : six
BuildRequires : stevedore
BuildRequires : tenacity
BuildRequires : weakrefmethod

%description
The Modular Layer 2 (ML2) plugin is a framework allowing OpenStack
Networking to simultaneously utilize the variety of layer 2 networking
technologies found in complex real-world data centers. It supports the
Open vSwitch, Linux bridge, and Hyper-V L2 agents, replacing and
deprecating the monolithic plugins previously associated with those
agents, and can also support hardware devices and SDN controllers. The
ML2 framework is intended to greatly simplify adding support for new
L2 networking technologies, requiring much less initial and ongoing
effort than would be required for an additional monolithic core
plugin. It is also intended to foster innovation through its
organization as optional driver modules.

%package bin
Summary: bin components for the neutron package.
Group: Binaries
Requires: neutron-data = %{version}-%{release}
Requires: neutron-config = %{version}-%{release}
Requires: neutron-license = %{version}-%{release}
Requires: neutron-services = %{version}-%{release}

%description bin
bin components for the neutron package.


%package config
Summary: config components for the neutron package.
Group: Default

%description config
config components for the neutron package.


%package data
Summary: data components for the neutron package.
Group: Data

%description data
data components for the neutron package.


%package license
Summary: license components for the neutron package.
Group: Default

%description license
license components for the neutron package.


%package python
Summary: python components for the neutron package.
Group: Default
Requires: neutron-python3 = %{version}-%{release}

%description python
python components for the neutron package.


%package python3
Summary: python3 components for the neutron package.
Group: Default
Requires: python3-core

%description python3
python3 components for the neutron package.


%package services
Summary: services components for the neutron package.
Group: Systemd services

%description services
services components for the neutron package.


%prep
%setup -q -n neutron-14.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559832993
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/neutron
cp LICENSE %{buildroot}/usr/share/package-licenses/neutron/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/neutron-dhcp-agent.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/neutron-l3-agent.service
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/neutron-linuxbridge-agent.service
install -m 0644 %{SOURCE4} %{buildroot}/usr/lib/systemd/system/neutron-metadata-agent.service
install -m 0644 %{SOURCE5} %{buildroot}/usr/lib/systemd/system/neutron-openvswitch-agent.service
install -m 0644 %{SOURCE6} %{buildroot}/usr/lib/systemd/system/neutron-server.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE7} %{buildroot}/usr/lib/tmpfiles.d/neutron.conf
## install_append content
install -d -m 755 %{buildroot}/usr/share/defaults/neutron
mv %{buildroot}/usr/etc/neutron/* %{buildroot}/usr/share/defaults/neutron
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/neutron-api
/usr/bin/neutron-db-manage
/usr/bin/neutron-debug
/usr/bin/neutron-dhcp-agent
/usr/bin/neutron-ipset-cleanup
/usr/bin/neutron-keepalived-state-change
/usr/bin/neutron-l3-agent
/usr/bin/neutron-linuxbridge-agent
/usr/bin/neutron-linuxbridge-cleanup
/usr/bin/neutron-macvtap-agent
/usr/bin/neutron-metadata-agent
/usr/bin/neutron-metering-agent
/usr/bin/neutron-netns-cleanup
/usr/bin/neutron-openvswitch-agent
/usr/bin/neutron-ovs-cleanup
/usr/bin/neutron-pd-notify
/usr/bin/neutron-rootwrap
/usr/bin/neutron-rootwrap-daemon
/usr/bin/neutron-rootwrap-xen-dom0
/usr/bin/neutron-rpc-server
/usr/bin/neutron-sanity-check
/usr/bin/neutron-server
/usr/bin/neutron-sriov-nic-agent
/usr/bin/neutron-status
/usr/bin/neutron-usage-audit

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/neutron.conf

%files data
%defattr(-,root,root,-)
/usr/share/defaults/neutron/api-paste.ini
/usr/share/defaults/neutron/rootwrap.conf
/usr/share/defaults/neutron/rootwrap.d/debug.filters
/usr/share/defaults/neutron/rootwrap.d/dhcp.filters
/usr/share/defaults/neutron/rootwrap.d/dibbler.filters
/usr/share/defaults/neutron/rootwrap.d/ebtables.filters
/usr/share/defaults/neutron/rootwrap.d/ipset-firewall.filters
/usr/share/defaults/neutron/rootwrap.d/iptables-firewall.filters
/usr/share/defaults/neutron/rootwrap.d/l3.filters
/usr/share/defaults/neutron/rootwrap.d/linuxbridge-plugin.filters
/usr/share/defaults/neutron/rootwrap.d/netns-cleanup.filters
/usr/share/defaults/neutron/rootwrap.d/openvswitch-plugin.filters
/usr/share/defaults/neutron/rootwrap.d/privsep.filters

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/neutron/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/neutron-dhcp-agent.service
/usr/lib/systemd/system/neutron-l3-agent.service
/usr/lib/systemd/system/neutron-linuxbridge-agent.service
/usr/lib/systemd/system/neutron-metadata-agent.service
/usr/lib/systemd/system/neutron-openvswitch-agent.service
/usr/lib/systemd/system/neutron-server.service

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : neutron
Version  : 8.0.0
Release  : 60
URL      : http://tarballs.openstack.org/neutron/neutron-8.0.0.tar.gz
Source0  : http://tarballs.openstack.org/neutron/neutron-8.0.0.tar.gz
Source1  : neutron-dhcp-agent.service
Source2  : neutron-l3-agent.service
Source3  : neutron-linuxbridge-agent.service
Source4  : neutron-metadata-agent.service
Source5  : neutron-openvswitch-agent.service
Source6  : neutron-server.service
Source7  : neutron.tmpfiles
Summary  : OpenStack Networking
Group    : Development/Tools
License  : Apache-2.0
Requires: neutron-bin
Requires: neutron-python
Requires: neutron-config
Requires: neutron-data
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: 0001-neutron-sudoers-entry.patch
Patch2: 0002-move-rootwrap-location.patch
Patch3: 0003-default-config.patch
Patch4: 0004-change-dnsmasq-location.patch
Patch5: 0005-fix-linuxbridge-service-for-python3.patch

%description
This package contains files that are required for XenAPI support for Neutron.

%package bin
Summary: bin components for the neutron package.
Group: Binaries
Requires: neutron-data
Requires: neutron-config

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


%package python
Summary: python components for the neutron package.
Group: Default

%description python
python components for the neutron package.


%prep
%setup -q -n neutron-8.0.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/neutron-dhcp-agent.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/neutron-l3-agent.service
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/neutron-linuxbridge-agent.service
install -m 0644 %{SOURCE4} %{buildroot}/usr/lib/systemd/system/neutron-metadata-agent.service
install -m 0644 %{SOURCE5} %{buildroot}/usr/lib/systemd/system/neutron-openvswitch-agent.service
install -m 0644 %{SOURCE6} %{buildroot}/usr/lib/systemd/system/neutron-server.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE7} %{buildroot}/usr/lib/tmpfiles.d/neutron.conf
## make_install_append content
rm -rf %{buildroot}/usr/etc
install -d -m 755 %{buildroot}/usr/share/defaults/neutron
install -d -m 755 %{buildroot}/usr/share/defaults/neutron/conf.d
install -p -D -m 644 etc/*.conf %{buildroot}/usr/share/defaults/neutron/
install -p -D -m 644 etc/*.ini %{buildroot}/usr/share/defaults/neutron/
install -p -D -m 644 etc/*.json %{buildroot}/usr/share/defaults/neutron/
install -d -m 755 %{buildroot}/usr/share/neutron/rootwrap.d
mv %{buildroot}/usr/share/defaults/neutron/rootwrap.conf %{buildroot}/usr/share/neutron/
install -p -D -m 640 etc/neutron/rootwrap.d/*.filters %{buildroot}/usr/share/neutron/rootwrap.d/
install -d -m 755 %{buildroot}/usr/share/neutron/plugins
mv etc/neutron/plugins/* %{buildroot}/usr/share/neutron/plugins/
install -d -m 750 %{buildroot}/usr/share/defaults/sudo/sudoers.d
install -p -D -m 440 neutron.sudoers %{buildroot}/usr/share/defaults/sudo/sudoers.d/neutron
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/neutron-bgp-dragent
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
/usr/bin/neutron-ns-metadata-proxy
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
/usr/bin/neutron-usage-audit

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/neutron-dhcp-agent.service
/usr/lib/systemd/system/neutron-l3-agent.service
/usr/lib/systemd/system/neutron-linuxbridge-agent.service
/usr/lib/systemd/system/neutron-metadata-agent.service
/usr/lib/systemd/system/neutron-openvswitch-agent.service
/usr/lib/systemd/system/neutron-server.service
/usr/lib/tmpfiles.d/neutron.conf

%files data
%defattr(-,root,root,-)
/usr/share/defaults/neutron/api-paste.ini
/usr/share/defaults/neutron/bgp_dragent.ini
/usr/share/defaults/neutron/dhcp_agent.ini
/usr/share/defaults/neutron/l3_agent.ini
/usr/share/defaults/neutron/metadata_agent.ini
/usr/share/defaults/neutron/metering_agent.ini
/usr/share/defaults/neutron/neutron.conf
/usr/share/defaults/neutron/policy.json
/usr/share/defaults/sudo/sudoers.d/neutron
/usr/share/neutron/plugins/ml2/.placeholder
/usr/share/neutron/rootwrap.conf
/usr/share/neutron/rootwrap.d/debug.filters
/usr/share/neutron/rootwrap.d/dhcp.filters
/usr/share/neutron/rootwrap.d/dibbler.filters
/usr/share/neutron/rootwrap.d/ebtables.filters
/usr/share/neutron/rootwrap.d/ipset-firewall.filters
/usr/share/neutron/rootwrap.d/iptables-firewall.filters
/usr/share/neutron/rootwrap.d/l3.filters
/usr/share/neutron/rootwrap.d/linuxbridge-plugin.filters
/usr/share/neutron/rootwrap.d/openvswitch-plugin.filters

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

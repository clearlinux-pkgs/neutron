#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC12B8E73B30F2FC8 (infra-root@openstack.org)
#
Name     : neutron
Version  : 16.1.0
Release  : 94
URL      : http://tarballs.openstack.org/neutron/neutron-16.1.0.tar.gz
Source0  : http://tarballs.openstack.org/neutron/neutron-16.1.0.tar.gz
Source1  : neutron-dhcp-agent.service
Source2  : neutron-l3-agent.service
Source3  : neutron-linuxbridge-agent.service
Source4  : neutron-metadata-agent.service
Source5  : neutron-openvswitch-agent.service
Source6  : neutron-server.service
Source7  : neutron.tmpfiles
Source8  : http://tarballs.openstack.org/neutron/neutron-16.1.0.tar.gz.asc
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
Requires: click
Requires: debtcollector
Requires: decorator
Requires: eventlet
Requires: futurist
Requires: httplib2
Requires: keystoneauth1
Requires: keystonemiddleware
Requires: netaddr
Requires: netifaces
Requires: neutron-lib
Requires: openstacksdk
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
Requires: pyOpenSSL
Requires: pyroute2
Requires: python-designateclient
Requires: python-neutronclient
Requires: python-novaclient
Requires: requests
Requires: six
Requires: stevedore
Requires: tenacity
Requires: tooz
BuildRequires : Jinja2
BuildRequires : Paste
BuildRequires : PasteDeploy
BuildRequires : Routes
BuildRequires : SQLAlchemy
BuildRequires : WebOb
BuildRequires : alembic
BuildRequires : buildreq-distutils3
BuildRequires : click
BuildRequires : debtcollector
BuildRequires : decorator
BuildRequires : eventlet
BuildRequires : futurist
BuildRequires : httplib2
BuildRequires : keystoneauth1
BuildRequires : keystonemiddleware
BuildRequires : netaddr
BuildRequires : netifaces
BuildRequires : neutron-lib
BuildRequires : openstacksdk
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
BuildRequires : pyOpenSSL
BuildRequires : pyroute2
BuildRequires : python-designateclient
BuildRequires : python-neutronclient
BuildRequires : python-novaclient
BuildRequires : requests
BuildRequires : six
BuildRequires : stevedore
BuildRequires : tenacity
BuildRequires : tooz

%description
OpenStack Neutron
        =================

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
Provides: pypi(neutron)
Requires: pypi(alembic)
Requires: pypi(debtcollector)
Requires: pypi(decorator)
Requires: pypi(eventlet)
Requires: pypi(futurist)
Requires: pypi(httplib2)
Requires: pypi(jinja2)
Requires: pypi(keystoneauth1)
Requires: pypi(keystonemiddleware)
Requires: pypi(netaddr)
Requires: pypi(netifaces)
Requires: pypi(neutron_lib)
Requires: pypi(openstacksdk)
Requires: pypi(os_ken)
Requires: pypi(os_vif)
Requires: pypi(os_xenapi)
Requires: pypi(oslo.cache)
Requires: pypi(oslo.concurrency)
Requires: pypi(oslo.config)
Requires: pypi(oslo.context)
Requires: pypi(oslo.db)
Requires: pypi(oslo.i18n)
Requires: pypi(oslo.log)
Requires: pypi(oslo.messaging)
Requires: pypi(oslo.middleware)
Requires: pypi(oslo.policy)
Requires: pypi(oslo.privsep)
Requires: pypi(oslo.reports)
Requires: pypi(oslo.rootwrap)
Requires: pypi(oslo.serialization)
Requires: pypi(oslo.service)
Requires: pypi(oslo.upgradecheck)
Requires: pypi(oslo.utils)
Requires: pypi(oslo.versionedobjects)
Requires: pypi(osprofiler)
Requires: pypi(ovs)
Requires: pypi(ovsdbapp)
Requires: pypi(paste)
Requires: pypi(pastedeploy)
Requires: pypi(pbr)
Requires: pypi(pecan)
Requires: pypi(psutil)
Requires: pypi(pyopenssl)
Requires: pypi(pyroute2)
Requires: pypi(python_designateclient)
Requires: pypi(python_neutronclient)
Requires: pypi(python_novaclient)
Requires: pypi(requests)
Requires: pypi(routes)
Requires: pypi(six)
Requires: pypi(sqlalchemy)
Requires: pypi(stevedore)
Requires: pypi(tenacity)
Requires: pypi(tooz)
Requires: pypi(webob)

%description python3
python3 components for the neutron package.


%package services
Summary: services components for the neutron package.
Group: Systemd services

%description services
services components for the neutron package.


%prep
%setup -q -n neutron-16.1.0
cd %{_builddir}/neutron-16.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598910201
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/neutron
cp %{_builddir}/neutron-16.1.0/LICENSE %{buildroot}/usr/share/package-licenses/neutron/294b43b2cec9919063be1a3b49e8722648424779
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
## Remove excluded files
rm -f %{buildroot}/etc/init.d/neutron-server
## install_append content
#rm -rf %{buildroot}/usr/etc

install -d -m 755 %{buildroot}/usr/share/defaults/neutron
mv %{buildroot}/usr/etc/neutron/* %{buildroot}/usr/share/defaults/neutron
#install -d -m 755 %{buildroot}/usr/share/defaults/neutron/conf.d
#install -p -D -m 644 etc/*.conf %{buildroot}/usr/share/defaults/neutron/
#install -p -D -m 644 etc/*.ini %{buildroot}/usr/share/defaults/neutron/
#install -p -D -m 644 etc/*.json %{buildroot}/usr/share/defaults/neutron/

#install -d -m 755 %{buildroot}/usr/share/neutron/rootwrap.d
#mv %{buildroot}/usr/share/defaults/neutron/rootwrap.conf %{buildroot}/usr/share/neutron/
#install -p -D -m 640 etc/neutron/rootwrap.d/*.filters %{buildroot}/usr/share/neutron/rootwrap.d/

#install -d -m 755 %{buildroot}/usr/share/neutron/plugins
#mv etc/neutron/plugins/* %{buildroot}/usr/share/neutron/plugins/

#install -d -m 750 %{buildroot}/usr/share/defaults/sudo/sudoers.d
#install -p -D -m 440 neutron.sudoers %{buildroot}/usr/share/defaults/sudo/sudoers.d/neutron
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
/usr/bin/neutron-ovn-db-sync-util
/usr/bin/neutron-ovn-metadata-agent
/usr/bin/neutron-ovn-migration-mtu
/usr/bin/neutron-ovs-cleanup
/usr/bin/neutron-pd-notify
/usr/bin/neutron-rootwrap
/usr/bin/neutron-rootwrap-daemon
/usr/bin/neutron-rpc-server
/usr/bin/neutron-sanity-check
/usr/bin/neutron-server
/usr/bin/neutron-sriov-nic-agent
/usr/bin/neutron-status
/usr/bin/neutron-usage-audit
/usr/bin/ovn_migration.sh

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/neutron.conf

%files data
%defattr(-,root,root,-)
/usr/share/ansible/neutron-ovn-migration/playbooks/ovn-migration.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/reduce-dhcp-renewal-time.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/backup/tasks/main.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/delete-neutron-resources/defaults/main.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/delete-neutron-resources/tasks/main.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/delete-neutron-resources/templates/delete-neutron-resources.sh.j2
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/migration/defaults/main.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/migration/tasks/activate-ovn.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/migration/tasks/cleanup-dataplane.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/migration/tasks/clone-dataplane.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/migration/tasks/main.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/migration/tasks/sync-dbs.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/migration/templates/activate-ovn.sh.j2
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/migration/templates/clone-br-int.sh.j2
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/post-migration/defaults/main.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/post-migration/tasks/main.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/pre-migration/tasks/main.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/resources/cleanup/defaults/main.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/resources/cleanup/tasks/main.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/resources/cleanup/templates/cleanup-resources.sh.j2
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/resources/create/defaults/main.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/resources/create/tasks/main.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/resources/create/templates/create-resources.sh.j2
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/resources/validate/defaults/main.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/resources/validate/tasks/main.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/resources/validate/templates/validate-resources.sh.j2
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/stop-agents/defaults/main.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/stop-agents/tasks/cleanup.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/stop-agents/tasks/main.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/stop-agents/vars/main.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/tripleo-update/defaults/main.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/tripleo-update/tasks/main.yml
/usr/share/ansible/neutron-ovn-migration/playbooks/roles/tripleo-update/templates/generate-ovn-extras.sh.j2
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
/usr/share/package-licenses/neutron/294b43b2cec9919063be1a3b49e8722648424779

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

SELinux Utils
=============

[![Build Status](https://travis-ci.org/ome/ansible-role-selinux-utils.svg)](https://travis-ci.org/ome/ansible-role-selinux-utils)
[![Ansible Role](https://img.shields.io/ansible/role/41124.svg)](https://galaxy.ansible.com/ome/selinux_utils/)

Sets a host variable indicating whether SELinux is enabled or not.
Installs utilities for interacting with SELinux if it is.

These utilities may be required by some Ansible modules when SELinux is enabled, and are not always present in CentOS 7 base images.

This role will set the host variable `selinux_enabled: {True,False}` which can be used in later roles.

Ideally this role should be included as a dependency in `meta/main.yml` of any roles that need to know whether SELinux is enabled.


Example Playbook
----------------

    - hosts: localhost
      roles:
      - ome.selinux_utils
      tasks:
        debug:
          msg: "SELinux is enabled or permissive"
        when: selinux_enabled


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk

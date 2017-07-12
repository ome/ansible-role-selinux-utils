import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


# The behaviour of this test depends on whether it's running with a docker
# container or full VM
def test_selinux_utils(Command, Package, TestinfraBackend):
    # We could do this by having separate test_files, but by keeping it
    # in one we can guarantee we always match one of the test conditions
    host = TestinfraBackend.get_hostname()

    if host == 'selinux-utils-docker':
        assert not Command.exists('/usr/sbin/getenforce')
        assert not Package('policycoreutils-python').is_installed
    else:
        getenforce = Command.check_output('/usr/sbin/getenforce')
        assert getenforce == 'Enforcing'
        assert Package('policycoreutils-python').is_installed

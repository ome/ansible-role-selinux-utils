import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


# The behaviour of this test depends on whether it's running with a docker
# container or full VM
def test_selinux_utils(Command, Package):
    if Command.exists('getenforce'):
        getenforce = Command.check_output('getenforce')
    else:
        getenforce = None

    if getenforce == 'Disabled':
        assert not Package('policycoreutils-python')
    else:
        assert Package('policycoreutils-python')

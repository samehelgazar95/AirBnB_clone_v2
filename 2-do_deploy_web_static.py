#!/usr/bin/python3
""" distributes an archive to your web server """
from fabric.api import env, put, run
from os.path import isfile

env.hosts = ['100.25.152.65', '52.3.242.252']
env.user = ['ubuntu', 'ubuntu']


def do_deploy(archive_path):
    """ Do some Sha2labzat and make the deploy """
    if archive_path is None:
        return Flase

    if isfile(archive_path) is False:
        return False

    arch_file = archive_path.split('/')[-1]
    arch_name = arch_file.split('.')[0]

    # First: Upload the archive to the server
    if put(archive_path, '/tmp/').failed:
        return False

    # Second: Uncompress the archive
    remote_arch_path = '/tmp/{}'.format(arch_file)
    remote_uncompress_path = '/data/web_static/releases/{}/'.format(
            arch_name)

    if run('mkdir -p {}'.format(uncompress_path)).failed:
        return False

    if run('tar -xvzf {} -C {}'.format(
            remote_arch_path, remote_uncompress_path)).failed:
        return False

    # Third: Delete remote archive & recreate symbolic link
    if run('rm -rf {}'.format(remote_arch_path)).failed:
        return False

    if run('rm -rf /data/web_static/current').failed:
        return False

    if run('ln -sf {} /data/web_static/current'.format(
            remote_uncompress_path)).failed:
        return False

    return True

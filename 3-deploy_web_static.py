#!/usr/bin/python3
""" Hn3mel full deploy """
from fabric.api import env, local, put, run
from datetime import datetime
from os.path import isfile


env.hosts = ['100.25.152.65', '52.3.242.252']
env.user = 'ubuntu'


def do_pack():
    """
        Tab ya 3am yl3an abo el fabric3==1.14.post1
        we mesh hakteb ay arguments
    """
    versions_dir = local("mkdir -p versions")
    if versions_dir.failed:
        return None

    n = datetime.utcnow()
    tgz_file = "web_static_{}{}{}{}{}{}.tgz".format(
            n.year, n.month, n.day, n.hour, n.minute, n.second)

    tgz_cmd = "tar -czf versions/{} web_static".format(tgz_file)

    compress = local(tgz_cmd)
    if compress.failed:
        return None

    return tgz_file


def do_deploy(archive_path):
    """ Do some Sha2labzat and make the deploy """
    if archive_path is None:
        return False

    if isfile(archive_path) is False:
        return False

    arch_file = archive_path.split('/')[-1]
    arch_name = arch_file.split('.')[0]

    # First: Upload the archive to the server
    if put(archive_path, '/tmp/').failed:
        return False

    # Second: Uncompress the archive
    if run('mkdir -p /data/web_static/releases/{}'.format(arch_name)).failed:
        return False

    if run('tar -xvzf /tmp/{} -C /data/web_static/releases/{}'.
            format(arch_file, arch_name)).failed:
        return False

    # Third: Delete remote archive & recreate symbolic link
    if run('rm /tmp/{}'.format(arch_file)).failed:
        return False

    if run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(
                arch_name, arch_name)).failed:
        return False

    if run('rm -rf /data/web_static/releases/{}/web_static'.
            format(arch_name)).failed:
        return False

    if run('rm -rf /data/web_static/current').failed:
        return False

    if run('ln -sf /data/web_static/releases/{}/ /data/web_static/current'.
            format(arch_name)).failed:
        return False

    return True


def deploy():
    """ Temp Temp Temp Temp"""
    # Archiving the web_static files
    pack = do_pack()
    if pack is None:
        return False

    # Deploying the files to servers
    full_path = 'versions/{}'.format(pack)
    deploy = do_deploy(full_path)
    return deploy

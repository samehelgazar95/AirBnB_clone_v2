#!/usr/bin/python3
""" Deploy Module for Web Static Content """
from os.path import exists
from fabric.api import env, put, run


env.hosts = ['100.25.152.65', '52.3.242.252']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if exists(archive_path) is False:
        return False

    _file = archive_path.split('/')[-1]
    _name = _file.split('.')[0]
    path = '/data/web_static/releases/'

    try:
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, _name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(_file, path, _name))
        run('rm /tmp/{}'.format(_file))

        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, _name))

        run('rm -rf {}{}/web_static'.format(path, _name))
        run('rm -rf /data/web_static/current')

        run('sudo ln -s {}{}/ /data/web_static/current'.format(path, _name))
        return True
    except Exception:
        return False

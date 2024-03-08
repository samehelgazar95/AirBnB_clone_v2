#!/usr/bin/python3
""" Do packing and deploying in one step """
from os.path import exists
from fabric.api import env, local, put, run
from datetime import datetime


env.hosts = ['100.25.152.65', '52.3.242.252']
env.user = 'ubuntu'


def do_pack():
    """Create a compressed archive of the web static content.

    Returns:
        str: The file path of the created archive, or None if an error occurs.
    """
    try:
        n = datetime.utcnow()
        tgz_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
                n.year, n.month, n.day, n.hour, n.minute, n.second)

        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(tgz_file))
        return tgz_file
    except Exception:
        return None


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
        run('sudo mkdir -p {}{}/'.format(path, _name))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(_file, path, _name))
        run('sudo rm /tmp/{}'.format(_file))

        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, _name))

        run('sudo rm -rf {}{}/web_static'.format(path, _name))
        run('sudo rm -rf /data/web_static/current')

        run('sudo ln -s {}{}/ /data/web_static/current'.format(path, _name))
        return True
    except Exception:
        return False


def deploy():
    """Deploy the web static content to remote servers.

    Returns:
        bool: True if deployment succeeds, False otherwise.
    """
    arch_file = do_pack()
    if arch_file is None:
        return False
    else:
        do_deploy(arch_file)

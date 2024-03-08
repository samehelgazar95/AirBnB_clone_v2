#!/usr/bin/python3
"""
hn3mel deploy in sha2 allah
"""
from os.path import isfile
from fabric.api import env, put, run


env.hosts = ['100.25.152.65', '52.3.242.252']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ Do some Sha2labzat and make the deploy """
    if isfile(archive_path) is False:
        return False

    _file = archive_path.split('/')[-1]
    _name = _file.split('.')[0]

    try:
        put(archive_path, '/tmp/{}'.format(_file))
        run('sudo mkdir -p /data/web_static/releases/{}/'.format(_name))
        run('sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.
            format(_file, _name))

        run('sudo mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'.format(_name, _name))

        run('sudo rm /tmp/{}'.format(_file))
        run('sudo rm -rf /data/web_static/releases/{}/web_static'.format(
            _name))
        run('sudo rm -rf /data/web_static/current')

        run('sudo ln -sf /data/web_static/releases/{}/'
            '/data/web_static/current'.format(_name))
        retun True
    except Exception:
        return False

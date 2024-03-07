#!/usr/bin/python3
""" Hn3mel full deploy """
from fabric.api import local


def deploy():
    """ Temp Temp Temp Temp"""
    # Archiving the web_static files
    pack = local('fab -f 1-pack_web_static.py do_pack')
    if pack is None:
        return False

    # Deploying the files to servers
    d = '2-do_deploy_web_static.py'
    dep_code = 'fab -f {} do_deploy:archive_path=versions/{}'.format(d, pack)
    deploy = local(dep_code)
    return deploy

#!/usr/bin/python3
"""Yel3an abo el Fabric3==1.14.post1 tany"""
from fabric.api import local
from datetime import datetime


def do_pack():
    versions_dir = local("mkdir -p versions")
    if versions_dir.failed:
        return None

    n = datetime.utcnow()
    tgz_file = "web_static_{}{}{}{}{}{}.tgz".format(
            n.year, n.month, n.day, n.hour, n.minute, n.second)

    tgz_cmd = "tar -cvzf versions/{} web_static".format(tgz_file)

    compress = local(tgz_cmd)
    if compress.failed:
        return None

    return tgz_file

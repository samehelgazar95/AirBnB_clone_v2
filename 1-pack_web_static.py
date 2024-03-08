#!/usr/bin/python3
"""Yel3an abo el Fabric3==1.14.post1 tany"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
        Tab ya 3am yl3an abo el fabric3==1.14.post1
        we mesh hakteb ay arguments
    """
    try:
        n = datetime.utcnow()
        tgz_file = "web_static_{}{}{}{}{}{}.tgz".format(
                n.year, n.month, n.day, n.hour, n.minute, n.second)

        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(tgz_file))
        return tgz_file
    except Exception:
        return None

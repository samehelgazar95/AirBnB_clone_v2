#!/usr/bin/python3
"""This module provides functions for deploying
and packing a web application using Fabric."""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Create a compressed archive of the web static content.

    Returns:
        str: The file path of the created archive, or None if an error occurs.
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

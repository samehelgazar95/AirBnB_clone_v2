#!/usr/bin/python3
""" """
from fabric.api import env, put, run


env.hosts = ['100.25.152.65', '52.3.242.252']

def do_deploy(archive_path):

    if archive_path is None:
        return Flase

    

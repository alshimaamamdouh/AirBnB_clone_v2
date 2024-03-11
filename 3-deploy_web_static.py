#!/usr/bin/python3
""" Script """

from fabric.api import local
from datetime import datetime
import os
from fabric.api import env, put, run, sudo
from os.path import exists


env.user = 'ubuntu'
env.hosts = ['54.164.241.47', '54.234.43.47']

def do_pack():
    """ generates a .tgz archive from the contents of the web_static"""
    local("sudo mkdir -p versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "web_static_{}.tgz".format(time)
    path = os.path.join("versions", name)
    result = local("sudo tar -cvzf {} web_static".format(path))

    if result.succeeded:
        return path

    else:
        return None


def do_deploy(archive_path):
    """ Distributes an archive to web servers """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        archive_filename = archive_path.split('/')[-1]
        release_path = "/data/web_static/releases/{}".format(archive_filename.split('.')[0])
        sudo("mkdir -p {}".format(release_path))
        sudo("tar -xzf /tmp/{} -C {}".format(archive_filename, release_path))
        sudo("rm /tmp/{}".format(archive_filename))
        sudo("mv {}/web_static/* {}".format(release_path, release_path))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {} /data/web_static/current".format(release_path))
        return True
    except:
        return False

def deploy():
    """ Deploy """
    archive_path_final = do_pack()

    if not archive_path_final:
        return False

    return do_deploy(archive_path_final)

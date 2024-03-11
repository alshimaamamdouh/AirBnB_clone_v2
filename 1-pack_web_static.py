#!/usr/bin/python3
""" do_pack """


from fabric.api import local
from datetime import datetime
import os


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

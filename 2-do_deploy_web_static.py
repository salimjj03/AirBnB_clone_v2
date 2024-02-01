#!/usr/bin/python3
""" This modle generates a .tgz archive from the
contents of the web_static folder of your
AirBnB Clone repo, using the function do_pack. """

from fabric.api import env, put, sudo
from os.path import exists


env.hosts = ["100.26.11.71", "54.237.217.229"]


def do_deploy(archive_path):
    """ This modle generates a .tgz archive from the
    contents. """

    if not exists(archive_path):
        return False

    c_file = archive_path.split("/")[-1]
    file = c_file.split(".")[0]
    if put(archive_path, "/tmp").failed is True:
        return False
    if sudo("mkdir -p /data/web_static/releases/{}".
            format(file)).failed is True:
        return False
    if sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(c_file, file)).failed is True:
        return False
    if sudo("cp -r  /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}".format(file, file)).failed is True:
        return False
    if sudo("rm -rf /data/web_static/releases/{}/web_static".
            format(file)).failed is True:
        return False
    if sudo("rm /tmp/{}".format(c_file)).failed is True:
        return False
    if sudo("rm -r /data/web_static/current").failed is True:
        return False
    if sudo("ln -s /data/web_static/releases/{}/ "
            "/data/web_static/current".format(file)).failed is True:
        return False
    return True

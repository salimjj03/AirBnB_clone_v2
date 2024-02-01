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
    put(archive_path, "/tmp")
    sudo("mkdir -p /data/web_static/releases/{}".format(file))
    sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
         format(c_file, file))
    sudo("cp -r  /data/web_static/releases/{}/web_static/* "
         "/data/web_static/releases/{}".format(file, file))
    sudo("rm -rf /data/web_static/releases/{}/web_static".format(file))
    sudo("rm /tmp/{}".format(c_file))
    sudo("rm -r /data/web_static/current")
    sudo("ln -s /data/web_static/releases/{}/ "
         "/data/web_static/current".format(file))
    return True

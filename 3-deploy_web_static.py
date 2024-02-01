#!/usr/bin/python3
""" This modle generates a .tgz archive from the
contents of the web_static folder of your
AirBnB Clone repo, using the function do_pack. """

from fabric.api import env, put, sudo
from os.path import exists
do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy


env.hosts = ["100.26.11.71", "54.237.217.229"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def deploy():
    """ This modle generates a .tgz archive from the
    contents. """

    file = do_pack()
    if file is None:
        return False
    fath = "versions/{}".format(file)
    return do_deploy(fath)

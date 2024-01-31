#!/usr/bin/python3
""" This modle generates a .tgz archive from the
contents of the web_static folder of your
AirBnB Clone repo, using the function do_pack. """

from fabric.api import local
from datetime import datetime


def do_pack():
    """ generates a .tgz archive from the
    contents of the web_static folder. """

    date = datetime.utcnow()
    file = "web_static_{}{}{}{}{}{}.tgz".format(
            date.year,
            date.month,
            date.day,
            date.hour,
            date.minute,
            date.second
            )

    name = local("date +'%Y%m%d%H%M%S'")
    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(file))
    local("mv {} versions".format(file))
    return file

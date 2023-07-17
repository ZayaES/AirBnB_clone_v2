#!/usr/bin/python3
""" a fab script to generate an archive on local"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """ packs a folder in archive"""

    dt = datetime.now()
    new_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                             dt.month,
                                                             dt.day,
                                                             dt.hour,
                                                             dt.minute,
                                                             dt.second)

    result = local("mkdir -p versions")

    if (result.failed is True):
        return None
    ch_own = local("sudo chown -R $USER:$USER versions")
    if (ch_own.failed is True):
        return None
    archive = local("tar -cvzf {} web_static".format(new_file))
    if (archive.failed is True):
        return None
    return new_file


def do_deploy(archive_path):
    """ deploys file on both web servers"""

    if local("ls -l {}".format(archive_path)).failed is True:
        return False
    res = put("versions/{}.tgz".format(new_file), "/tmp/")
    if res.failed is True:
        return False
    res2 = run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".format(new_file))
    if res2.failed is True:
        return False
    res3 = sudo("rm -rf /tmp/{}".format(new_file))
    if res3.failed is True:
        return False
    res4=run("rm -rf /data/web_static/current")
    if res4.failed is True:
        return False
    res5 = run("ln -s  /data/web_static/releases/{}/".format(ned))

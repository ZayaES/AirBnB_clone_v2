#!/usr/bin/python3
""" a fab script to generate an archive on local"""
from datetime import datetime
from fabric.operations import local, sudo, env, put, run
from fabric.context_managers import cd


env.hosts = ['54.236.41.129', '3.85.41.144']
env.user = 'ubuntu'


def do_pack():
    """ packs a folder in archive"""

    dt = datetime.now()
    new_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                             dt.month,
                                                             dt.day,
                                                             t.hour,
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
    file_path = archive_path.split(".")
    file_path = file_path[0]
    file_name = file_path.split("/")
    file_name = file_name[-1]
    print(file_name)
    if local("ls -l {}".format(archive_path)).failed is True:
        print("yes")
        return False

    res = put("{}".format(archive_path), "/tmp/")
    if res.failed is True:
        return False
    
    with cd("/tmp/"):
        run("mkdir -p /data/web_static/releases/{}".format(file_name))
        res2 = run("tar -xzf {}.tgz \
                    -C /data/web_static/releases/{}/".format(
                    file_name, file_name))
    if res2.failed is True:
        return False
    res3 = sudo("rm -rf /tmp/{}".format(file_name))
    if res3.failed is True:
        return False
    res4=run("rm -rf /data/web_static/current")
    if res4.failed is True:
        return False
    res5 = run("ln -s  /data/web_static/releases/{}/ \
                /data/web_static/current".format(file_name))

"""
do_deploy("/arhive/version/no_way/yes.tgz")
"""

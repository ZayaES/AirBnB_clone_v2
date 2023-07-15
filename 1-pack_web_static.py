#!/usr/bin/python3
""" a fab script to generate an archive on local"""
from datetime import datetime
from fabric.operations import local, sudo


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

	if (result.failed == True):
		return None
	ch_own = local("sudo chown -R $USER:$USER versions")
	if (ch_own.failed == True):
		return None
	archive = local("tar -cvzf {} web_static".format(new_file))
	if (archive.failed == True):
		print(archive.failed)
		return None
	return new_file

#!/usr/bin/python3
""" a Fabric script (based on file 1-pack_web_static.py, it distributes..
    ..an archive to web servers, using do_deploy: """


from fabric.api import *
from datetime import datetime
from os.path import exists


env.hosts = ['35.237.166.125', '54.167.61.201']

def do_deploy(archive_path):
    """ distributes the archive to web servers
    """
    if exists(archive_path) is False:
        return False
    file = archive_path.split('/')[-1]
    no_tgz = '/data/web_static/releases/' + "{}".format(file.split('.')[0])
    tmp = "/tmp/" + file

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(no_tgz))
        run("tar -xzf {} -C {}/".format(tmp, no_tgz))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(no_tgz, no_tgz))
        run("rm -rf {}/web_static".format(no_tgz))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(no_tgz))

        return True
    except:
        return False
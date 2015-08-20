#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import shutil
import sys

def Filegen(fname):
    with open(fname,'w') as f:
        f.write("内容")

def InsNginx(name):
    subprocess.check_call(['/usr/bin/lxc-attach','-n',name,'--','/usr/bin/apt-get','install','nginx'])

def CopyFile(name,fname):
    shutil.copy(fname,"/var/lib/lxc/{}/rootfs/home/ubuntu/{}".format(name,fname))

def NginxConfigtest(name,fname):
    subprocess.check_output(['/usr/bin/lxc-attach','-n',name,'--','/etc/init.d/nginx','configtest'])

def NginxStart(name):
    subprocess.check_output(['/usr/bin/lxc-attach','-n',name,'--','service','nginx','start'])

def NginxRestart(name):
    subprocess.check_output(['/usr/bin/lxc-attach','-n',name,'--','service','nginx','restart'])

def main():

    name="ubuntu-nginx"
    


    InsNginx(name)

    (name)


if __name__ == '__main__':
    main()


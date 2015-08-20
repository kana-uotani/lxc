#!/usr/bin/python
# -*- coding: utf-8 -*-

#引数start,restart,stopでそれぞれnginxが起動、再起動、停止をします。

import subprocess
import sys
import shutil

def InsNginx(name):
    subprocess.check_call(['/usr/bin/lxc-attach','-n',name,'--','/usr/bin/apt-get','install','nginx'])

def NginxConfigtest(name):
    subprocess.check_output(['/usr/bin/lxc-attach','-n',name,'--','/etc/init.d/nginx','configtest'])

def NginxStart(name):
    subprocess.check_output(['/usr/bin/lxc-attach','-n',name,'--','service','nginx','start'])

def NginxRestart(name):
    subprocess.check_output(['/usr/bin/lxc-attach','-n',name,'--','service','nginx','restart'])

def NginxStop(name):
    subprocess.check_output(['/usr/bin/lxc-attach','-n',name,'--','service','nginx','stop'])

def NginxConfCopy(text):
    shutil.copyfile(text,'/var/lib/lxc/ubuntu-nginx/rootfs/etc/nginx/sites-available/default')

def main():

    argvs=sys.argv
    print argvs
    name="ubuntu-nginx"

    text="/home/kana/lxc/default.new"

    InsNginx(name)
    
    if argvs[1]=="restart":
        NginxRestart(name)
        print argvs[1]
    elif argvs[1]=="stop":
        NginxStop(name)
        print argvs[1]
    elif argvs[1]=="start":
        NginxStart(name)
        print argvs[1]

    NginxConfigtest(name)

    NginxConfCopy(text)

if __name__ == '__main__':
    main()


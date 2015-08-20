#!/usr/bin/python
# -*- coding: utf-8 -*-

#引数restart、stopでそれぞれnginxが再起動と停止をします。

import subprocess
import shutil
import sys

def Filegen(fname):
    with open(fname,'w') as f:
        f.write("内容")

def InsNginx(name):
    subprocess.check_call(['/usr/bin/lxc-attach','-n',name,'--','/usr/bin/apt-get','install','nginx'])

def NginxConfigtest(name,fname):
    subprocess.check_output(['/usr/bin/lxc-attach','-n',name,'--','/etc/init.d/nginx','configtest'])

def NginxStart(name):
    subprocess.check_output(['/usr/bin/lxc-attach','-n',name,'--','service','nginx','start'])

def NginxRestart(name):
    subprocess.check_output(['/usr/bin/lxc-attach','-n',name,'--','service','nginx','restart'])

def NginxStop(name):
    subprocess.check_output(['/usr/bin/lxc-attach','-n',name,'--','service','nginx','stop'])

def NginxConfGen(text):
    subprocess.check_output(['cat','/var/lib/lxc/ubuntu-nginx/rootfs/etc/nginx/sites-enabled/default',text,'>','/var/lib/lxc/ubuntu-nginx/rootfs/etc/nginx/sites-enabled/default'])

def main():

    argvs=sys.argv
    print argvs
    name="ubuntu-nginx"

    text="/home/kana/lxc/app_conf.txt"

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

    NginxConfGen(text)

if __name__ == '__main__':
    main()


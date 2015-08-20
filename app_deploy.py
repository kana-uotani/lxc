#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import shutil

def Filegen(fname):
    with open(fname,'w') as f:
        f.write("内容")

def InsPython(name):
    subprocess.check_call(['/usr/bin/lxc-attach','-n',name,'--','/usr/bin/apt-get','install','python'])

def CopyFile(name,fname):
    shutil.copy(fname,"/var/lib/lxc/{}/rootfs/home/ubuntu/{}".format(name,fname))

def SrtScat(name,fname):
    print name
    print fname

    subprocess.check_call(['/usr/bin/lxc-attach','-n',name,'--','chmod','+x','home/ubuntu/{}'.format(fname)])
    subprocess.check_call(['/usr/bin/lxc-attach','-n',name,'--','sh','-c','/usr/bin/socat TCP-LISTEN:8080,fork,reuseaddr EXEC:/home/ubuntu/{} &'.format(fname)])

def main():

    fname = "web_test.py"

    #Filegen(fname)

    InsPython('ubuntu-ap1')
    InsPython('ubuntu-ap2')
    InsPython('ubuntu-nginx')

    CopyFile('ubuntu-ap1',fname)
    CopyFile('ubuntu-ap2',fname)
    CopyFile('ubuntu-nginx',fname)

    SrtScat('ubuntu-ap1',fname)
    SrtScat('ubuntu-ap2',fname)

if __name__ == '__main__':
    main()


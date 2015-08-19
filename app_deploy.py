#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import sys


def Filegen(fname):
    with open(fname) as f:
        f.write("内容")

def InsPython(name):
    check = subprocess.check_call(['/usr/bin/lxc-attach','-n',name,'--','/usr/bin/apt-get','install','python'])
    CheckOut(check)

def CopyFile(name,fname):
    check = subprocess.check_call(['cp',fname,'/var/lib/lxc/%s/rootfs/home/ubuntu/%s'(name,fname),])
    CheckOut(check)

def SrtScat(name,fname):
    subprocess.check_call(['/usr/bin/lxc-attach','-n',name,'--','chmod','+x','home/ubuntu/%s'(fname)])
    check = subprocess.check_call(['/usr/bin/lxc-attach','-n',name,'--','sh','-c','/usr/bin/socat TCP4-LISTEN:8000,fork,reuseaddr EXEC:./%s &'(fname)])
    CheckOut(check)

def CheckOut(check):
    if check != 0 :
        sys.exit()

def main():

    fname = "web-test.py"

    #Filegen(fname)

    InsPython('ubuntu-ap1')
    InsPython('ubuntu-ap2')
    InsPython('ubuntu-nginx')

    CopyFile('ubuntu-ap1',fname)
    CopyFile('ubuntu-ap2',fname)
    CopyFile('ubuntu-nginx',fname)

    SrtScat('ubuntu-ap1',fname)
    SrtScat('ubuntu-ap2',fname)
    SrtScat('ubuntu-nginx',fname)

if __name__ == '__main__':
    main()


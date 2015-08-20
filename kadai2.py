#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess

def CrtContainer(name):
    subprocess.check_call(['/usr/bin/lxc-create','-t','ubuntu','-n',name])

def SrtContainer(name):
    subprocess.check_call(['/usr/bin/lxc-start','-n',name,'-d'])

def InsSocat(name):
    subprocess.check_call(['/usr/bin/lxc-attach','-n',name,'--','/usr/bin/apt-get','install','socat'])

def SrtScat(name):
    subprocess.check_call(['/usr/bin/lxc-attach','-n',name,'--','sh','-c','/usr/bin/socat TCP4-LISTEN:8000,fork,reuseaddr EXEC:"hostname" &'])

def main():

#    CrtContainer('ubuntu-ap1')
#    CrtContainer('ubuntu-ap2')
#    CrtContainer('ubuntu-nginx')
    
    SrtContainer('ubuntu-ap1')
    SrtContainer('ubuntu-ap2')
    SrtContainer('ubuntu-nginx')

    InsSocat('ubuntu-ap1')
    InsSocat('ubuntu-ap2')

    SrtScat('ubuntu-ap1')
    SrtScat('ubuntu-ap2')
    
    print "End"

if __name__ == '__main__':
    main()


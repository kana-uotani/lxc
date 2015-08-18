#!/usr/bin/python
# -*- coding: utf-8 -*-

import commands

def main():

    print commands.getoutput("lxc-create -t ubuntu -n ubuntu-ap1")
    print commands.getoutput("lxc-create -t ubuntu -n ubuntu-ap2")
    print commands.getoutput("lxc-create -t ubuntu -n ubuntu-nginx")

    print commands.getoutput("lxc-start -n ubuntu-ap1 -d")
    print commands.getoutput("lxc-start -n ubuntu-ap2 -d")
    print commands.getoutput("lxc-start -n ubuntu-nginx -d")

    print commands.getoutput("lxc-attach -n ubuntu-ap1 -- apt-get install socat")
    print commands.getoutput("lxc-attach -n ubuntu-ap2 -- apt-get install socat")

    print commands.getoutput("lxc-attach -n ubuntu-ap1 -- sh -c 'socat TCP4-LISTEN:8000,fork,reuseaddr EXEC:\"hostname\" &'")
    print commands.getoutput("lxc-attach -n ubuntu-ap2 -- sh -c 'socat TCP4-LISTEN:8000,fork,reuseaddr EXEC:\"hostname\" &'")

if __name__ == '__main__':
    main()


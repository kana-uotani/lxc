#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import sys


def main():

    argvs=sys.argv

    output = subprocess.check_output(['/bin/ls','/etc/'])
    outputs = output.split()


    for x in outputs:
        if argvs[1] in x:
            print x

if __name__ == '__main__':
    main()
	

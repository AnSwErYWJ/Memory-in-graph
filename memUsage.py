#!/usr/bin/env python
# coding=utf-8

import numpy as np
import pylab as pl
import sys

# check argvs
if len(sys.argv) != 3 :
    print "Usage: sh memUsage.py <filepath> <graphpath>"
    sys.exit(-1)

# load file
data = np.loadtxt(sys.argv[1])

pl.plot(data[:,0],data[:,1],'r')

# set title
pl.title('Memory usage of xxx')
pl.xlabel('time')
pl.ylabel('mem')

# x,y limits
#pl.xlim(0.0000,23.0000)
pl.ylim(0.0,30.)

pl.savefig(sys.argv[2], format='png')

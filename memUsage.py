#!/usr/bin/env python
# coding=utf-8

#import matplotlib as mpl
import numpy as np
import pylab as pl
import sys

# check argvs
if len(sys.argv) != 3 :
    print "Usage: sh memUsage.py <filepath> <graphpath>"
    sys.exit(-1)

#mpl.rcParams['font.sans-serif']=['SimHei'] # display chinese
#mpl.rcParams['axes.unicode_minus']=False # display '-'

# load file
data = np.loadtxt(sys.argv[1])

# draw
pl.plot(data[:,0],data[:,1],'r')

# set title
pl.title('memory of xxx')
pl.xlabel('time')
pl.ylabel('mem')

# x,y limits
#pl.xlim(0.0000,23.0000) # depends on usage.txt
pl.ylim(0.0,30.)

pl.savefig(sys.argv[2], format='png')

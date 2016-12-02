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
pl.plot(data[:,0],data[:,1],color='r',linewidth=2.5,linestyle="-",label="memery")
pl.legend(loc='upper left')

# x,y limits
#pl.xlim(0.0000,23.0000) # depends on usage.txt
pl.ylim(0.0,30.)

# set title
pl.title('memory of xxx')
pl.xlabel('time')
pl.ylabel('mem')

# set text , position:(x,y)
pl.text(17,25,"This is text")
# set note,xy is note point,xytext is text point
pl.annotate('This is start', xy=(16.9275, 22), xytext=(17,15),arrowprops=dict(facecolor='black', shrink=0.05),)

# save pic
pl.savefig(sys.argv[2], format='png')

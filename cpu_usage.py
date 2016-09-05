#!/usr/bin/env python
# coding=utf-8

import numpy as np
import pylab as pl

data = np.loadtxt('usage.txt')

pl.plot(data[:,0],data[:,1])

pl.title('cpu usage of xxx')
pl.xlabel('time')
pl.ylabel('mem')

# x,y limits
#pl.xlim(0.0000,23.0000)
#pl.ylim(0.0,30.)

pl.savefig('result.png', format='png')

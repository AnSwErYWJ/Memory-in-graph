#!/usr/bin/env python
# coding=utf-8

import numpy as np
import pylab as pl

x = [1,2,3,4,5]
y = [1,4,9,16,25]

pl.plot(x,y)

pl.title('Plot of y vs. x')
pl.xlabel('x axis')
pl.ylabel('y axis')

# x,y limits
#pl.xlim(0.0,7.0)
#pl.ylim(0.0,30.)

pl.savefig('linegraph.png', format='png')

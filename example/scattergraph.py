#!/usr/bin/env python
# coding=utf-8

import pylab as pl

x = [1,2,3,4,5]
y = [1,4,9,16,25]

pl.plot(x,y,'o')

pl.savefig('scattergraph.png', format='png')

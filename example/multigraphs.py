#!/usr/bin/env python
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

plt.figure(1) # create graph 1
plt.figure(2) # create graph 2

ax1 = plt.subplot(211) # create subgraph1 in graph 2
ax2 = plt.subplot(212) # create subgraph2 in graph 2

x = np.linspace(0,3,100)
for i in xrange(5):
    plt.figure(1) # choose graph 1
    plt.plot(x,np.exp(i*x/3))
    plt.sca(ax1) # choose subgraph1 in graph 2
    plt.plot(x,np.sin(i*x))
    plt.sca(ax2) # choose subgraph2 in graph 2
    plt.plot(x,np.cos(i*x))

plt.figure(1) # choose graph 1
plt.savefig('multigraph1.png', format='png')

plt.figure(2) # choose graph 2
plt.savefig('multigraph2.png', format='png')

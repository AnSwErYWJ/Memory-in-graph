#!/usr/bin/env python
# coding=utf-8

import matplotlib.pyplot as plt

for idx,color in enumerate("rgbyck"):
    plt.subplot(321+idx,axisbg=color)
#plt.show()
plt.savefig('subgraphs.png', format='png')

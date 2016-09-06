# matplotlib
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badge/)
[![stable](http://badges.github.io/stability-badges/dist/stable.svg)](http://github.com/badges/stability-badges)

## Introduction
Production line graph memory usage statistics(制作内存使用统计折线图).

## Environment
+ Linux Bash Shell
+ Python

## Installation
Install [numpy](https://sourceforge.net/projects/numpy/files/NumPy/), you can download latest version:
```
$ tar –xf numpy-1.6.2.tar.gz
$ cd numpy-1.6.2
$ python setup.py build
$ python setup.py install
$ python
Python 2.7.9 (default, Mar 28 2016, 18:11:56)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>>
```
Install [libpng](https://sourceforge.net/projects/libpng/) :
```
$ tar –xf libpng-1.6.24.tar.gz
$ cd libpng-1.6.24
$ ./configure
$ make
$ sudo make install
```
Install [matplotlib](https://sourceforge.net/projects/matplotlib/files/matplotlib/), you can download latest version:
```
$ tar –xf matplotlib-1.1.1_notests.tar.gz
$ cd matplotlib-1.1.1_notests
$ python setup.py build
$ python setup.py install
$ python
Python 2.7.9 (default, Mar 28 2016, 18:11:56)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import pylab as pl
>>>
```


Download project :
```
$ git clone git@github.com:AnSwErYWJ/Memory-in-graph.git
```

## Usage
Count memory usage, generate ``usage.txt`` :
```
$ sh countRes.sh <program-name>
```
Then, generate ``result.png`` :
```
$ ./memUsage.py
```

## Reference
+ [matplotlib安装](http://www.cnblogs.com/ouzi/archive/2012/09/29/2708442.html)
+ [Python图表绘制：matplotlib绘图库入门](http://www.cnblogs.com/wei-li/archive/2012/05/23/2506940.html)
+ [Shell脚本浮点运算](http://answerywj.com/2016/09/05/Shell%E8%84%9A%E6%9C%AC%E6%B5%AE%E7%82%B9%E8%BF%90%E7%AE%97/)

## About me
[![forthebadge](http://forthebadge.com/images/badges/ages-20-30.svg)](http://forthebadge.com)
- WebSite：[http://www.answerywj.com](http://www.answerywj.com)
- Email：[yuanweijie1993@gmail.com](https://mail.google.com)
- GitHub：[AnSwErYWJ](https://github.com/AnSwErYWJ)
- Blog：[AnSwEr不是答案的专栏](http://blog.csdn.net/u011192270)
- Weibo：[@AnSwEr不是答案](http://weibo.com/1783591593)

## Copyright and License
**The MIT License (MIT)**
Copyright (c) 2016 AnSwErYWJ

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

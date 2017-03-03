# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 22:34:02 2017

@author: Sn0wbreeze
"""

import matplotlib.pyplot as plt
import numpy as np

ran=["1001","101","11","2"]
a = 0
colour = ['b','g','r','y']
shape = ['o','x','s','D']
plt.figure(figsize=(8,9))
for i in ran:
    x, y, y_err = np.loadtxt("{0}.txt".format(i),delimiter=",",unpack=True)
    xlog = np.log10(x)
    ylog = np.log10(y)
    y_errlog = np.log10(y_err)
    #plt.scatter(xlog,ylog,c=color[a],label="Theoritcal Gain = {0}".format(i),marker='o')
    plt.errorbar(xlog ,ylog, yerr=y_errlog,fmt=shape[a],c=colour[a],label="Theoritcal Gain = {0}".format(i))
    a = a+1
plt.title("Plot of Experimental Gain in an op amp")
plt.xlabel("Log(frequency)")
plt.ylabel("Log(experimental gain)")
plt.legend(loc="best")
plt.xlim(1.5,7)
plt.ylim(-0.5)
plt.grid()
plt.savefig("Plot_op_amp")
plt.show()
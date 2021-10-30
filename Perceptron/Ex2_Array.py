# -*- coding: utf-8 -*-
import numpy as np 

def h(X):
    w = np.array([20,50])
    b = -1000
    a = np.dot(X,w) + b
    return (a>=0).astype(int)

X = np.array([
    [10,15],
    [10,18],
    [22,15]
])
print(h(X)) # ได้ [0 1 1]

import matplotlib.pyplot as plt

mx,my = np.meshgrid(np.linspace(0,60,200),np.linspace(0,30,200))
mX = np.array([mx.ravel(),my.ravel()]).T
mz = h(mX).reshape(200,-1)
plt.gca()
plt.contourf(mx,my,mz,cmap='hot')
plt.xlabel(u'๒๐ บาท',family='Tahoma',size=14)
plt.ylabel(u'๕๐ บาท',family='Tahoma',size=14)
plt.show()
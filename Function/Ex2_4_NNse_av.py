# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

def ha_entropy(z,h):
    return -(z*np.log(h)+(1-z)*np.log(1-h))

X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])
z = np.array([0,0,0,1])

n = len(z) # จำนวนข้อมูล

w = np.array([0,0.])
b = 0
eta = 0.8
thamsam = 1000
entropy = []
for o in range(thamsam):
    dw = 0
    db = 0
    J = 0
    for i in range(n):
        ai = np.dot(X[i],w) + b
        hi = sigmoid(ai)
        gai = hi-z[i]
        gwi = gai*X[i]
        gbi = gai
        dw -= eta*gwi
        db -= eta*gbi
        J += ha_entropy(z[i],hi)
    w += dw/n
    b += db/n
    entropy.append(J)

plt.figure()
plt.plot(entropy,'r')
plt.xlabel(u'จำนวนรอบ',family='tahoma',size=14)
plt.ylabel(u'ค่าเสียหาย',family='tahoma',size=14)
plt.show()
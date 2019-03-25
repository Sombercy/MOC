#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

def f (x):
    return np.sin(x/5.0) * np.exp(x/10.0) + 5 * np.exp(-x/2.0)
def h (x):
    return f(x).astype(int) # приведение в целый тип
#print (f(6))
x = 2
#print (optimize.minimize(f, x))
#print ('----------------------------------')
#print (optimize.minimize(f, 30, method='BFGS')) градиентный метод
"""lst = [(1.0, 30.0)]
print (optimize.differential_evolution(f, lst))""" # дифференциальная эволюция
x = np.arange(1, 30, 1) # от 1 до 30 с шагом 1
plt.plot(f(x))
plt.plot(h(x))
print (optimize.minimize(h, 30, method='BFGS')) # 30
lst = [(1.0, 30.0)]
print (optimize.differential_evolution(h, lst)) # 25.25
plt.show()
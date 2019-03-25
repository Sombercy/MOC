import numpy as np
from scipy import linalg
from matplotlib import pylab as plt
# f(x) = sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)
a = np.array([[0.22, 3.03], [0.23, 0.41]])
b = np.array([3.25, 0.64])
x = linalg.solve(a, b)
print (x)
x = np.arange(1, 15, 0.5)
y = np.sin(x/5) * np.exp(x/10) + 5 * np.exp(-x/2)
plt.plot(x, y)
plt.show()
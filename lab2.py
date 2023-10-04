import matplotlib.pyplot as plt
import numpy as np
from numpy import append

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = []
a = 0

for i in range(10):
    a = np.sin(i)
    y.append(a)

plt.plot(x, y)

x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = []
a = 0

for i in range(10):
    a = np.cos(i)
    y1.append(a)

plt.plot(x1, y1)

x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y2 = []
a = 0

for i in range(10):
    a = np.tan(i)
    y2.append(a)

plt.plot(x2, y2)

x3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y3 = []
a = 0.5

for i in range(10):
    a = 1 / np.tan(i)
    y3.append(a)

plt.plot(x3, y3)

x4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y4 = []
a = 0.5

for i in range(10):
    a = np.arcsin(i)
    y4.append(a)

plt.plot(x4, y4)

x5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y5 = []
a = 0.5

for i in range(10):
    a = np.arccos(i)
    y5.append(a)

plt.plot(x5, y5)

x6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y6 = []
a = 0.5

for i in range(10):
    a = np.arctan(i)
    y6.append(a)

plt.plot(x6, y6)

plt.show()


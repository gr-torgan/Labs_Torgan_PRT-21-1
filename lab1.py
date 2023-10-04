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
    a = np.sin(2*(i))
    y1.append(a)

plt.plot(x1, y1)

x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y2 = []
a = 0

for i in range(10):
    a = np.sin(i*3)
    y2.append(a)

plt.plot(x2, y2)

x3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y3 = []
a = 0

for i in range(10):
    a = np.sin(i*4)
    y3.append(a)

plt.plot(x3, y3)

plt.show()

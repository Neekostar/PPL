import pylab as pl
import random
import numpy as np
import matplotlib.pyplot as plt

a = random.randint(1, 20)
cinema = np.random.random(a)
cinema *= 10

b = random.randint(1, 10)
cafe = np.random.random(b)
cafe *= 10

width = 0.3

x1 = range(len(cinema))
x2 = range(len(cafe))

array1 = [len(x1)]
array2 = [len(x2)]

fig, ax = plt.subplots()
rects1 = ax.bar(1 - width / 2, array1, width, label="cinema")
rects2 = ax.bar(1 + width / 2, array2, width, label="cafe")
ax.set_title("Карта")
ax.legend()
plt.show()

pl.plot(x1, cinema, "go")
pl.plot(x2, cafe, "bo")
pl.title("Карта")
pl.legend(("cinema", "cafe",))
pl.show()

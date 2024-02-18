# Matplotlib
# we have to use this Matplotlib and another lib called pylot for drawing

import matplotlib.pyplot as plt

years = [1950, 1970,1990, 2010, 2023]
pops = [2.5,3.4,4.6,6.7, 7.3]

plt.scatter(years,pops, c="red")
plt.plot(years,pops)
plt.xlabel("years")
plt.ylabel("pops")
plt.title("world Population")
plt.show()
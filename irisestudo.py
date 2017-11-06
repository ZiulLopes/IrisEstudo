"""
    Estudo Iris Data Set
    by: Luiz
"""

# import libs
import numpy as np
import pandas as pd
from collections import OrderedDict
from matplotlib import pyplot as plt

iris_ds = pd.read_csv("iris.csv")

speciesiris = list(OrderedDict.fromkeys(iris_ds["species"]))

print(speciesiris)

N = 50
g1 = (0.6 + 0.6 * np.random.rand(N), np.random.rand(N))
g2 = (0.4+0.3 * np.random.rand(N), 0.5*np.random.rand(N))
g3 = (0.3*np.random.rand(N),0.3*np.random.rand(N))

print("g1: {}\ng2: {}\ng3: {}\n".format(g1, g2, g3))
 
data = (g1, g2, g3)
colors = ("red", "green", "blue")
groups = ("coffee", "tea", "water") 
 
# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, axisbg="1.0")
 
for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
 
plt.title('Matplot scatter plot')
plt.legend(loc=2)
plt.show()

"""
    Estudo Iris Data Set
    by: Luiz
"""

# import libs
import pandas as pd
from collections import OrderedDict

iris_ds = pd.read_csv("iris.csv")

speciesiris = list(OrderedDict.fromkeys(iris_ds["species"]))

print(speciesiris)

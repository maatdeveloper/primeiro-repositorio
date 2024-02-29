import pandas as pd
import numpy as np

dataframe = pd.read_csv("dados/Credit.csv")
arrey = np.array(dataframe["duration"])
print(arrey)

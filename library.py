import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('ODI data.csv')
a=df.head(5)

plt.figure(figsize=(3,2))
plt.xticks(rotation=75)
plt.bar(a.Player,a.Mat)
plt.show()


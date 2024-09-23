import pandas  as pd
import numpy as np
import matplotlib.pyplot as plt
import random
df = pd.read_csv("digits.csv")
num201 = df.loc[200]
num202 = df.loc[201]
df = df.drop(201)
df = df.drop(200)
for i in range(df.shape[0]):
    for j in range(1, df.shape[1]):
        if df.iat[i, j]  > 127 : df.iat[i, j] = 1
        else: df.iat[i, j] = 0
rand_row = random.randint(0, len(df) - 1)
row = df.loc[rand_row]
row = np.reshape(row[1:], (28, 28))
plt.imshow(row)
plt.show()
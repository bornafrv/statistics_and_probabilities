import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as ss
import numpy as np
df = pd.read_csv("Tarbiat.csv")
metro = list(df.loc[:, "metro"])
brt = list(df.loc[:, "BRT"])
plt.hist(metro)
plt.hist(brt)
plt.show()
landa_metro = sum(metro) / len(metro)
landa_brt = sum(brt) / len(brt)
poisson_metro = ss.poisson.pmf(list(range(0, 15)), landa_metro)
plt.plot(poisson_metro)
plt.hist(metro, density = True)
plt.show()
landa_z = landa_metro + landa_brt
poisson_z = ss.poisson.pmf(list(range(0, 15)), landa_z)
plt.plot(poisson_z)
plt.hist(metro + brt, density = True)
plt.show()
n = 8
p = landa_metro / landa_z
w_binomial = ss.binom.pmf(list(range(0, 15)), n, p)
plt.plot(w_binomial)
plt.show()
sum_of_metro_brt  = np.array(metro) + np.array(brt)
index = np.where(sum_of_metro_brt == 8)
index_metro = list(np.take(metro, index))
plt.hist(index_metro, density = True)
plt.plot(w_binomial)
plt.show()
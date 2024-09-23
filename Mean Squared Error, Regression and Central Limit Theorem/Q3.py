import numpy as np, random
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm 
#import pylab as py 
import scipy.stats as stats

df = pd.read_csv('FIFA2020.csv', encoding = "ISO-8859-1")
def set_seed(seed):
    np.random.seed(seed)
    random.seed(seed)
set_seed(810109203)

pace_mean, dribbling_mean = df[['pace', 'dribbling']].mean(numeric_only=True)
df['dribbling'] = df['dribbling'].fillna(dribbling_mean)
df['pace'] = df['pace'].fillna(pace_mean)
box = df.boxplot(column='age')
box.plot()
plt.show()

minage = df['age'].min()
maxage = df['age'].max()
Q1 = df['age'].quantile(0.25)
Q2 = df['age'].quantile(0.5)
Q3 = df['age'].quantile(0.75)
print(minage, maxage, Q1, Q2, Q3)


def main_func(n3):
  sample = np.random.choice(df['weight'].to_numpy(), n3)

  def get_mean(list):
    mean = 0
    for l in list:
      mean += l
    mean /= len(list)
    return mean

  def get_var(list, mean):
    var = 0
    for l in list:
      var += (l - mean) ** 2
    var /= len(list)
    return var

  mean = get_mean(sample)
  var = get_var(sample, mean)
  std = var ** 0.5

  print(mean, var, std)
  normal_sample = np.random.normal(mean, std, n3)
  sm.qqplot(sample, loc = mean, scale = std, line = '45')

main_func(50)
plt.show()
main_func(100)
plt.show()
main_func(2000)
plt.show()

sample = np.random.choice(df['weight'].to_numpy(), 100)
statistic, p_value = stats.shapiro(sample)
print(p_value)



landa = 3
n = 5000
poisson_sample = np.random.poisson(landa, n)
plt.hist(poisson_sample)
plt.show()



def compare(n):
  poisson_sample = np.random.poisson(landa, n)
  sm.qqplot(poisson_sample, line = '45')
  statistic, p_value = stats.shapiro(poisson_sample)
  plt.show()
  print(p_value)
  
compare(5)
compare(50)
compare(5000)
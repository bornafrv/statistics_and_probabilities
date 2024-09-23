import scipy.stats as sc
import numpy as np

avg = 80
std = 12
my_normal = sc.norm(avg, std*std)

cdf0 = 0
cdf_minimum_mark = cdf0 + (1 - 0.1)
answer1 = sc.norm.ppf(cdf_minimum_mark, avg, std)
print(answer1)

percentile_75 = sc.norm.ppf(0.75, avg, std)
percentile_50 = sc.norm.ppf(0.5, avg, std)
answer2 = [percentile_50, percentile_75]
print(answer2)

answer3 = my_normal.cdf(90) - my_normal.cdf(80)
print(answer3)


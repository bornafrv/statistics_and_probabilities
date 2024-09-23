import matplotlib.pyplot as plt
from scipy.stats import binom 
from scipy.stats import poisson
from scipy.stats import norm

n = 250
prob = 0.008

binomial = binom.pmf(list(range(n+1)), n, prob)
poisson = poisson.pmf(list(range(n+1)), n*prob)
normal = norm.pdf(list(range(n+1)), n*prob, n*prob*(1-prob))

plt.plot(binomial)
plt.plot(poisson)
plt.plot(normal)
plt.show()
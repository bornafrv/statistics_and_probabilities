import numpy as np
import matplotlib.pyplot as plt

SUCCESS = 1
FAIL = 0

def create_bin_sample(n, prob, m):
    arr = np.array(np.random.choice([FAIL, SUCCESS], p = [1-prob, prob], size = (n*m)))
    matrix = arr.reshape(m, n) 
    return np.sum(matrix, axis = 1)

def exp_practical():
    arr = []
    for percent in range(101):
        arr.append(np.sum(create_bin_sample(500, percent / 100, 5000)) / 5000)
    return arr

def exp_theorical():
    arr = []
    for percent in range(101):
        arr.append(500 * percent / 100)
    return arr

def var_practical():
    arr = []
    for percent in range(101):
        arr.append(np.var(create_bin_sample(500, percent / 100, 5000)))
    return arr

def var_theorical():
    arr = []
    for percent in range(101):
        arr.append(500 * (percent / 100) * (1 - (percent / 100)))
    return arr

plt.plot(np.array(range(101)), np.array(exp_practical()))
plt.plot(np.array(range(101)), np.array(exp_theorical()))
plt.plot(np.array(range(101)), np.array(var_practical()))
plt.plot(np.array(range(101)), np.array(var_theorical()))
plt.show()
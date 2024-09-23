import random
import sympy
import math
def carlo(n, k):
    count = 0
    for i in range(k):
        numbers = []
        while(len(numbers) != n):
            num = random.randint(1, n)
            count = count + 1
            if num not in numbers: numbers.append(num)
    return count / k

n10_k10 = carlo(10, 10)
n10_k100 = carlo(10, 100)
n10_k1000 = carlo(10, 1000)
print(n10_k10, n10_k100, n10_k1000)

s = sympy.symbols('s')
def mgf_xi(n):
    mgf_xi = []
    for i in range(1, n + 1):
        num = (1 - (i - 1) / n) * pow(math.e, s) / (1 - (pow(math.e, s) * ((i - 1) / n)))
        mgf_xi.append(num)
    return mgf_xi

mgf_lists = mgf_xi(10)

mgf_x = 1
for num in mgf_lists: mgf_x *= num

deriv = sympy.diff(mgf_x, s)
mean = deriv.subs({s:0})
print(mean)
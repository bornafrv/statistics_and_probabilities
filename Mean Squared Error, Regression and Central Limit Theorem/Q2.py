import matplotlib.pyplot as plt
import numpy as np

def Regression(x, y):
    xx = []
    for i in range(len(x)):
        temp = x[i] * x[i]
        xx.append(temp)
        
    yy = []
    for i in range(len(x)):
        temp = y[i] * y[i]
        yy.append(temp)
        
    xy = []
    for i in range(len(x)):
        temp = x[i] * y[i]
        xy.append(temp)
    
    xsum = sum(x)
    ysum = sum(y)
    sumxx = sum(xx)
    sumyy = sum(yy)
    sumxy = sum(xy)
    
    t1 = (len(x) * sumxy) - (xsum * ysum)
    t2 = (len(x) * sumxx) - sumxx
    a = t1 / t2
    b = (ysum - a * xsum) / len(x)
    
    t3 = (len(x) * sumxy) - (xsum * ysum)
    t4 = len(x) * sumxx - (xsum ** 2)
    t5 = len(x) * sumyy - (ysum ** 2)
    t6 = (t4 ** 0.5) * (t5 ** 0.5)
    
    coef = t3 / t6
    
    print(a, b, coef)
    
    plt_x = np.linspace(-10, 10, 100)
    plt_y = (a * plt_x) + b
    
    plt.plot(plt_x, plt_y)
    plt.plot(x, y, 'go')
    plt.show()
    
x1 = [-2.3, -1.1, 0.5, 3.2, 4.0, 6.7, 10.3, 11.5]
y1 = [-9.6, -4.9, -4.1, 2.7, 5.9, 10.8, 18.9, 20.5]
x2 = [-2.3, -1.1, 0.5, 3.2, 4.0, 6.7, 10.3, 11.5, 5.8]
y2 = [-9.6, -4.9, -4.1, 2.7, 5.9, 10.8, 18.9, 20.5, 31.3]
x3 = [-2.3, -1.1, 0.5, 3.2, 4.0, 6.7, 10.3, 11.5, 20.4]
y3 = [-9.6, -4.9, -4.1, 2.7, 5.9, 10.8, 18.9, 20.5, 14.1]
x4 = [-2.3, -1.1, 0.5, 3.2, 4.0, 6.7, 10.3, 11.5, 20.4]
y4 = [-9.6, -4.9, -4.1, 2.7, 5.9, 10.8, 18.9, 20.5, 31.3]

Regression(x1, y1)
Regression(x2, y2)
Regression(x3, y3)
Regression(x4, y4)
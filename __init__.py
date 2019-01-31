# coding:utf-8
''''' 
Created on 2015年11月8日 

@author: Administrator 
'''
import numpy as np
import math


# 求解皮尔逊相关系数
def computeCorrelation(X, Y):
    xBar = np.mean(X)
    yBar = np.mean(Y)
    SSR = 0
    varX = 0
    varY = 0
    for i in range(0, len(X)):
        # 对应分子部分
        diffXXBar = X[i] - xBar
        diffYYBar = Y[i] - yBar
        SSR += (diffXXBar * diffYYBar)
        # 对应分母求和部分
        varX += diffXXBar ** 2
        varY += diffYYBar ** 2
    SST = math.sqrt(varX * varY)
    return SSR / SST


def polyfit(x, y, degree):
    results = {}
    # coeffs 为相关系数，x自变量，y因变量，degree为最高幂
    coeffs = np.polyfit(x, y, degree)

    # 定义一个字典存放值，值为相关系数list
    results['polynomial'] = coeffs.tolist()

    # p相当于直线方程
    p = np.poly1d(coeffs)
    yhat = p(x)  # 传入x，计算预测值为yhat

    ybar = np.sum(y) / len(y)  # 计算均值
    # 对应公式
    ssreg = np.sum((yhat - ybar) ** 2)
    sstot = np.sum((y - ybar) ** 2)
    results['determination'] = ssreg / sstot

    print" results :", results
    return results


testX = [1, 3, 8, 7, 9]
testY = [10, 12, 24, 21, 34]

# 输出的是简单线性回归的皮尔逊相关度和R平方值
print "r : ", computeCorrelation(testX, testY)
print "r^2 : ", str(computeCorrelation(testX, testY) ** 2)

print polyfit(testX, testY, 1)["determination"] 
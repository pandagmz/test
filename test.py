#!/usr/bin/python
from numpy import *
import csv
import numpy as np

n = 129
y = mat(zeros((n, 8)))
x = mat(zeros((n, 2)))

def loadcsv():
	reader = np.loadtxt("test.csv", dtype=np.str, delimiter=",")
	index = 0
	for row in reader:
		for i in range(0, 7):
			y[index, i] = row[i]
		x[index, 0] = row[8]
		x[index, 1] = row[9]
		index += 1

def mulreg(x0, x1, x2):
    a = np.mat([[n, sum(x1), sum(x2)], 
        [sum(x1), sum(multiply(x1, x1)), sum(multiply(x1, x2))],
        [sum(x2), sum(multiply(x1, x2)), sum(multiply(x2, x2))]])
    b = np.mat([[sum(x0)], [sum(multiply(x1, x0))], [sum(multiply(x2, x0))]])
    c = a.I * b;
    return c;

loadcsv();
res = zeros(8)
step = 10
maxp = 0
maxc = zeros(3)
for a1 in range(0, 1, step):
    for a2 in range(0, 100, step):
        for a3 in range(0, 100, step):
            for a4 in range(0, 100, step):
                for a5 in range(0, 100, step):
                    for a6 in range(0, 100, step):
                        for a7 in range(0, 100, step):
                            a8 = 100 - a1 - a2 - a3 - a4 - a5 - a6 - a7
                            if a8 < 0 :
                                continue

                            Y = (a1*y[:,0]+a2*y[:,1]+a3*y[:,2]+a4*y[:,3]+a5*y[:,4]+a6*y[:,5]+a7*y[:,6]+a8*y[:,7]);
                            Y = Y / 100 * 52 - 0.03;
                            c = mulreg(Y, x[:,0], x[:,1]);
                            if c[0] < 0.15 :
                                continue

                            if c[1] - c[2] < 0.15 :
                                continue

                            p = prod(Y + 1)
                            if p > maxp :
                                maxp = p
                                res = array([a1,a2,a3,a4,a5,a6,a7,a8])
                                maxc = c

print res
print maxc
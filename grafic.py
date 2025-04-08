import numpy as np
import matplotlib.pyplot as fig
#import math #outra forma
from math import exp,cos

n=int(input('n='))
x=np.zeros(n)
y=np.zeros(n)
for i in range(n):
    x[i]=0.1*i
 #   y[i]=math.exp(-0.1*x[i])*math.cos(x[i])
    y[i]=exp(-0.1*x[i])*cos(x[i]) 

    fig.plot(x,y)
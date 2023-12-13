import pandas
import numpy
import scipy
import matplotlib
import sklearn

from numpy import *
from pandas import *
from scipy import *
from scipy.interpolate import *
from matplotlib import *
from sklearn import *
from sklearn.metrics import mean_squared_error, r2_score

data=pandas.read_excel('dry.xlsx')
print (data)

x=data.iloc[:,0].values
y=data.iloc[:,1].values
print (x)
print (y)

f1=numpy.polyfit(x,y,1)
f2=numpy.polyfit(x,y,2)
f3=numpy.polyfit(x,y,3)
f4=numpy.polyfit(x,y,4)
print(f1)
print(f2)
print(f3)
print(f4)

from matplotlib.pyplot import *
plot(x,y,'o') #this plot the orignal points of x & y

plot(x,y,'o') #this plot the orignal points of x & y
xp=numpy.linspace(-0.01,0.08,100)
plot(xp,numpy.polyval(f1,xp),'r-')#this plot the new x values and the output y from equation f1 (1st degree linear equation)

plot(x,y,'o') #this plot the orignal points of x & y
plot(xp,numpy.polyval(f2,xp),'b--')#this plot the new x values and the output y from equation f2 (2rd degree Quadratic equation)

plot(x,y,'o') #this plot the orignal points of x & y
plot(xp,numpy.polyval(f3,xp),'m:')#this plot the new x values and the output y from equation f3 (3rd degree cubic equation)

plot(x,y,'o') #this plot the orignal points of x & y
plot(xp,numpy.polyval(f4,xp),'m:')#this plot the new x values and the output y from equation f4 (4rd degree equation)

plot(x,y,'o') #this plot the orignal points of x & y
xp=numpy.linspace(-0.01,0.08,100)
plot(xp,numpy.polyval(f1,xp),'r-')#this plot the new x values and the output y from equation f1 (1st degree linear equation)
plot(xp,numpy.polyval(f2,xp),'b--')#this plot the new x values and the output y from equation f2 (2rd degree Quadratic equation)
plot(xp,numpy.polyval(f3,xp),'m:')#this plot the new x values and the output y from equation f3 (3rd degree cubic equation)
plot(xp,numpy.polyval(f4,xp),'m:')#this plot the new x values and the output y from equation f4 (4rd degree equation)

r1=print(r2_score(y, numpy.polyval(f1,x)))
r2=print(r2_score(y, numpy.polyval(f2,x)))
r3=print(r2_score(y, numpy.polyval(f3,x)))
r4=print(r2_score(y, numpy.polyval(f4,x)))

print(mean_squared_error(y, numpy.polyval(f1,x)))
print(mean_squared_error(y, numpy.polyval(f2,x)))
print(mean_squared_error(y, numpy.polyval(f3,x)))
print(mean_squared_error(y, numpy.polyval(f4,x)))

y_pred1=numpy.polyval(f1,0.12)
print(y_pred1)
y_pred2=numpy.polyval(f2,0.12)
print(y_pred2)
y_pred3=numpy.polyval(f3,0.12)_
print(y_pred3)
y_pred4=numpy.polyval(f4,0.12)
print(y_pred4)

y_pred4_1=numpy.polyval(f4,0.09)
y_pred4_2=numpy.polyval(f4,0.11)
y_pred4_3=numpy.polyval(f4,0.13)
y_pred4_4=numpy.polyval(f4,0.15)
y_pred4_5=numpy.polyval(f4,0.17)
print(y_pred4_1)
print(y_pred4_2)
print(y_pred4_3)
print(y_pred4_4)
print(y_pred4_5)

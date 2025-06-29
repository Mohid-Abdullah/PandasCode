import numpy as np
import pandas as pd

a = np.array([12,42,5,33,27,42])

print(a)
print(a.ndim) #no of dimensions
print(a.size)
print(a[3]) #3rd index element

b = np.array([[73,24,53,23],[48,23,65,12]])

print(b)
print(b.ndim) #no of dimensions
print(b.size)
print(b.shape)
print(b[1,2]) #1 index row's 2nd index element

c = np.zeros(4)
d = np.ones(3)
print(c,d)

e = np.arange(5) #array with range
print(e)

f = np.linspace(0,16,num=5)#from 0 to 16 make 5 factors
print(f)

g = np.array([23,32,12,21])
h = np.concatenate((c,g),axis=0)#conc two arrays 
print(h)

a2 = a[2:4, np.newaxis]#make 1d to 2d(here we are making a 1d array into 2d column array)
print(a2.shape)
print(a2)

i = np.dot(c,g)
print(i)

import numpy as np
from copy import deepcopy
from scipy import linalg
import time
start_time = time.time()
def minor(m,i,j):       #numpy.delete(arr, obj, axis=None)
   m=np.delete(m,j,1)   #arr refers to the input array,
   m=np.delete(m,i,0)   #obj refers to which sub-arrays (e.g. column/row no. or slice of the array) and
   return m             #axis refers to either column wise (axis = 1) or row-wise (axis = 0) delete operation.
def det(m):             #Determinant
   opr=int(0)
   if len(m)==1 and len(m[0])==1:
     return m[0][0]
   for i in range(1):
      for j in range(len(m[i])):
         opr+=det(minor(m,i,j))*np.power(-1,i+j)*m[i][j]
   return opr
def replacement(m,b,k): #replacing the column in m with b
   '''n=[[0] * len(m) for i in range(len(m))]
   for i in range(len((m))):
     for j in range(len((m))):
       n[i][j]=m[i][j]'''
   for i in range(len((m))):
      m[i][k]=b[i][0]
   return m
def Kramer(m,b):        #Cramer's rule
   X = []
   detm=det(m)
   for j in range(len(m[0])):
      X.append(det(replacement(deepcopy(m),b,j))/detm)
   return X
m=[[89, 10, 9, 6],
  [2, 21, 3, 4],
  [3, 4, 43, 23],
  [8, 13, 14, 59]]
b=[[1],[2],[3],[4]]
epc=0.00001


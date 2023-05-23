import numpy as np 
#loadtxt file univariate.txt phân cách "," mặc định dtype=float
A=np.loadtxt("univariate.txt", delimiter=",")
#print 5 tuple đầu tiên
print(A[0:5,:])
#print size số row của A[0:5,:]
print(np.size(A[0:5,:],0))
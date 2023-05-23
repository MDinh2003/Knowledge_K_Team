import numpy as np
from functions import *


[X, y] = Loadtxt('data.txt')
[X, mu, s] = Normalize(X)
[Theta, J_hist] = GradientDescent(X,y,0.1,400)  

#Test trên array input
input = np.array([1,1650,3])
input = (input-mu)/s
#Lưu ý sửa lại x0 = 1
input[0] = 1

predict = predict(input,Theta)
print('%.2f$'%(predict))

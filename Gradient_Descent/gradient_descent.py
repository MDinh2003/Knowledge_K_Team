import numpy as np
import matplotlib.pyplot as plt #thư viện vẽ biểu đồ
from functions import *
raw=np.loadtxt('data.txt', delimiter=',')
X=np.copy(raw)
X[:,1]=X[:,0]
X[:,0]=1
y = raw[:,1]
#Train data
#mặc định alpha = 0.02 iter = 5000
[Theta, J_hist] = GradientDescent(X,y)
#Predict
#chuyển về đơn vị người
predict = predict(X,Theta) * 10000
#Plot kết quả
plt.figure(1)
plt.plot(X[:,1],y,'rx')
plt.plot(X[:,1],predict/10000,'-b') #đơn vị gốc: nghìn người
plt.figure(2)
plt.plot(J_hist[:,0],J_hist[:,1],'-r')
plt.show() #chỉ gọi 1 lần trong chương trình để hiển thị các biểu đồ cùng lúc
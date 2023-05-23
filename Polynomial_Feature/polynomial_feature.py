import numpy as np
from functions import *
import matplotlib.pyplot as plt

data = np.loadtxt('data.txt',delimiter=',')

#Khởi tạo ma trận X cùng kích thước với data 
X = np.ones(data.shape)
#lấy các cột đầu làm X
X[:,1:] = data[:,:-1]
#lấy cột cuối làm y
y = data[:,-1]

#Vòng lặp từ mũ 2 đến mũ 8
for i in range(2,9):
	#thêm một cột feature vào bên phải X với giá trị bằng x1 mũ i
	X = np.c_[X, X[:,1]**i]
#Lấy kích thước y làm m
m = y.size
#Lấy số cột của X làm n
n = X.shape[1]

#tính min và max của x1
min_x = np.min(X[:,1])
max_x = np.max(X[:,1])
#tạo ma trận xp có giá trị từ min_x – 10 đến max_x + 10, step là 0.5 (mỗi giá trị lệch nhau 0.5)
xp = np.arange(min_x - 10, max_x + 10, 0.5)
#thêm x0 bằng 1 cho xp
xp = np.c_[np.ones(xp.size), xp]
#thực hiện thêm polynomial feature như đã làm với X
for i in range(2,9):
	xp = np.c_[xp, xp[:,1]**i]

#Normalize X
[X, mu, sig] = Normalize(X)
#thực hiện normalize xp bằng mu và sigma tính từ X
xp -= mu
xp /= sig
xp[:,0] = 1

#train data với alpha bằng 0.1
theta, jhist = GradientDescent(X, y, 0.1, 100)
#plot bộ training set, cần đảo ngược quá trình normalize bằng cách * sigma + mu
plt.plot(X[:,1]*sig[1] +mu[1], y, 'rx')
#plot đường dự đoán
plt.plot(xp[:,1]*sig[1] +mu[1], xp@theta)

plt.show()
 
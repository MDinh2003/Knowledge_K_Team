import numpy as np
from functions import *
import matplotlib.pyplot as plt

raw = np.loadtxt('data.txt',delimiter=',')
#Câu lệnh dùng để sắp xếp ngẫu nhiên lại data, đảm bảo tính công bằng
np.random.shuffle(raw)
#Thêm cột 1 đầu tiên
data = np.ones([np.size(raw,0),np.size(raw,1)+1])
data[:,1:] = raw[:,0:]
#Normalize toàn bộ data
[data, mu, sig] = Normalize(data)
#Tách 20% đầu làm cross-validation set
Xcv = data[0:int(np.size(data,0)/100*20),0:-1]
ycv = data[0:int(np.size(data,0)/100*20),-1]
#Tách 20% tiếp theo làm test set
Xtest = data[int(np.size(data,0)/100*20):int(np.size(data,0)/100*40),0:-1]
ytest = data[int(np.size(data,0)/100*20):int(np.size(data,0)/100*40),-1]
#Phần còn lại là training set
X = data[int(np.size(data,0)/100*40):,0:-1]
y = data[int(np.size(data,0)/100*40):,-1]

#Chỉ lấy cột thứ 2, bỏ cột x0 luôn bằng 1
plt.plot(X[:,1],y,'rx')
plt.show()

#tạo list các giá trị có thể của alpha
alph = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1]
#tạo array lưu lại các J(θ) của từng giá trị alpha
costs = np.zeros(7)
for i in range(7):
	#train thuật toán với từng giá trị alpha
	[theta, jhist] = GradientDescent(X, y, alph[i], 100)
	#lưu lại J(θ) tính trên cross-validation set
	costs[i] = computeCost(Xcv,ycv,theta)

#tạo một đồ thị mới để plot
plt.figure(2)
#plot các giá trị cost cho từng giá trị alpha
plt.plot(alph,costs,'b-')
#tìm alpha có hiệu quả nhất (có cost thấp nhất)
alpha = alph[np.where(costs == np.min(costs))[0][0]]
print(alpha)
plt.show()

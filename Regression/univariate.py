#Trong vấn đề univariate này chúng ta sẽ dự đoán lợi nhuận của một xe thức ăn từ dân số của thành phố. Cột đầu trong file là dân số, cột thứ hai là lợi nhuận.
import numpy as np
import matplotlib.pyplot as plt     

#import toàn bộ file univariate.txt
X = np.loadtxt('univariate.txt', delimiter = ',')
#import Theta từ file univariate_theta.txt
Theta = np.loadtxt('univariate_theta.txt')
#Lưu ý y
y = np.copy(X[:,-1])
#Chuyển cột đầu (x1) sang cột thứ (x2)
X[:,1] = X[:,0]
#Đổi cột đầu x1 thành số 1
X[:,0] = 1
#Tính lợi nhuận (đơn vị 10000$)
predict = X @ Theta
#Chuyển lợi nhuận về đơn vị $
predict *= 10000
#in cặp dân số-lợi nhuận đầu tiên (đơn vị dân số: người)
print('%d người : %.2f$' %(X[0,1]*10000,predict[0]))

#Plot giá trị thực tế (không lấy cột bias 1 đầu)
#X[:,1:] là x-axis của biểu đồ, không lấy cột đầu; y là y-axis, rx là red x, plot dữ liệu bằng dấu x màu đỏ
plt.plot(X[:,1:],y,'rx')
#Plot dự đoán
#Ta dùng đơn vị gốc là 10000$, -b là đường thẳng màu xanh
plt.plot(X[:,1:],predict/10000,'-b')
#show kết quả
plt.show()
#Lưu kết quả
np.savetxt('predicted_value.txt',predict,fmt = '%.6f')
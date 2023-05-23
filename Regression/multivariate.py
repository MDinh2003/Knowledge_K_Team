#Ở vấn đề multivariate, chúng ta sẽ dự đoán giá nhà ($) từ kích thước (feet-vuông) và số phong ngủ. Ta sẽ có file multivariate.txt gồm những mẫu thử kích thước-số phòng-giá thực tế. File multivariate_theta.txt sẽ chứa các parameter Theta, giúp ta có thể dự đoán giá.
import numpy as np
#loadtxt input learningset
X_=np.loadtxt('multivariate.txt', delimiter=',')
#loadtxt parameter Theta
Theta=np.loadtxt('multivariate_theta.txt')
#Create X 
X=np.zeros((np.size(X_,0),np.size(X_,1)))
#Tinh zise n bỏ đi column y
n=np.size(X_,1)-1
#create x0
X[:,0]=1
#Thêm các cột x1 -> xn
X[:,1:]=X_[:,:n]
predict=X@Theta
print('%d feet-vuông, %d phòng ngủ : %.1f$' %(X[0,1], X[0,2], predict[0]))
#Lưu kết quả
np.savetxt('predicted_value_1.txt',predict,fmt = '%.2f')


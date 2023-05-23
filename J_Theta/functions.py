#file: functions.py
import numpy as np
def predict(X,Theta):
	return X @ Theta

#function computeCost
def computeCost(X,y,Theta):
    #Tính h theta
    predicted = predict(X,Theta)
    #Tính sai số bình phương
    sqr_error = (predicted - y)**2
    #Tính tổng sai số của mảng giá trị
    sum_error = np.sum(sqr_error)
    #Nhân 1/2m
    m = np.size(y)
    J = (1/(2*m))*sum_error
    return J

#function computeCost_Vec
#Ở phiên bản vectorized, ta có thể viết hàm J(θ) đơn giản hơn:
def computeCost_Vec(X,y,Theta):
    #Tính sai số
	error = predict(X,Theta) - y
	m = np.size(y)
    #Lưu ý phép nhân matrĩ là @ phép nhân số là *
	J = (1/(2*m))*np.transpose(error)@error
	return J
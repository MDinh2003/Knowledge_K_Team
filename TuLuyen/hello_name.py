#Viết chương trình hiển thị các từ theo yêu cầu ra màn hình: “Xin”, “chao!", “Toi", “ten", “la”, “{Tên của bạn}”. Các từ cách nhau bởi “--” và {Tên của bạn} được nhập từ bàn phím.
def p_name(name):
    print('Xin','chao!','Toi','ten','la','{}'.format(name),sep='--')
if __name__ == '__main__':
    name = input("Nhap vao name: ")
    p_name(name)
    
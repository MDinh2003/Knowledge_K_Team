#Viết chương trình tính và hiển thị ra màn hình tổng hai số nguyên được nhập bất kỳ từ bàn phím (Có xử lý ngoại lệ đầu vào).
from sum import sum
if __name__ == '__main__':
    try:
        a, b = map(int,input("Nhap 2 so nguyen: ").split())
        print(sum(a, b))
    except:
        print("Da xay ra loi")
#Viết chương trình tính và hiển thị ra màn hình tổng hai số nguyên được nhập bất kỳ từ bàn phím.
def sum(a, b):
    return a + b
if __name__ == '__main__':
    a, b = map(int,input("Nhap 2 so nguyen: ").split())
    print(sum(a, b))
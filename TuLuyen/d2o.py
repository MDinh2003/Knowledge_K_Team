def DecimalToOctal(a):
    res=0; i=1
    while a!=0:
        res+=((a%8)*i)
        a/=8
        i*=10
    return res
if __name__ == '__main__':
    a = input("Nhap so he thap phan: ")
    print(DecimalToOctal(a))
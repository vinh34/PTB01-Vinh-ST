import random
n = int(input("Nhập N: "))
if n%2==0:
    print("n là số chẵn")
else:
    print("n là số lẻ")
A=random.randint(1,4)
if A == 1:
    print("Bỏ vào giỏ A")
elif A == 2:
    print("Bỏ vào giỏ B")
elif A == 3:
    print("Bỏ vào giỏ C")
else:
    print("Bỏ vào giỏ D")
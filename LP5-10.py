import math
a = int(input("Enter A Number : "))
b = int(input("Enter Another Number : " ))
while(b>0):
    temp = a % b
    a = b
    b = temp
print(f"GCD : {a}")




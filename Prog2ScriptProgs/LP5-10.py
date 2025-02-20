num1 = int(input("Enter A Number: "))
num2 = int(input("Enter Another Number : "))
final = 0

for i in range(num2, 1-1,-1):
    test1 = i % num1
    test2 = i % num2
    if test1 == 0 and test2 == 0:
        final = i
print(

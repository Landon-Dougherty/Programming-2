copies = int(input("Enter # Of Copies To Be Printed : "))
price = 0.0
if 0 < copies <= 99:
    price = 0.30
elif 99 < copies <= 499:
    price = 0.28
elif 499 < copies <= 749:
    price = 0.27
elif 750 < price <= 999:
    price = 0.26
elif copies > 1000:
    price = 0.25
else: 
    print("Enter A Valid # Of Copies To Print")
    quit()

print(f"Your Price Per Copy Is : ${price}")
print(f"Your Total Cost Is : ${round(price*copies,2)}")
eggs = int(input("Enter # Of Eggs To Buy : "))
price = 0 
dozen = eggs//12
leftover = eggs - (dozen*12)

if 0 < eggs <= 35:
    price = 0.50
elif 35 < eggs <= 71:
    price = 0.45
elif 71 < eggs <= 131:
    price = 0.40
elif eggs > 131:
    price = 0.35
else:
    print("Please Enter A Valid # Of Eggs To Buy")

print(f"your price per dozen of eggs is : ${price}".title())
print(f"your total cost for the eggs is : ${round((dozen*price)+(leftover*(price/12)),2)}".title())



amount = 1500

if amount > 1000:
    discount = amount * 0.10
else:
    discount = 0

total = amount - discount
print("Discount:", discount)
print("Total Bill:", total)

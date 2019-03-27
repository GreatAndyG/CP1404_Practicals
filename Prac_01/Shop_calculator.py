## Ask for amount of items.
total = 0
number = int(input("Number of items: "))
while number < 0:
    print("Invalid Number of intems!")
    number = int(input("Number of items: "))
# Ask for price of each item
for i in range(number):
    price = float(input("Price of item: "))
    total += price
# Take 10% discount if total price of items > 100
if total > 100:
    total = total * .9

print("Total price for ", number, "items is $ ", total, sep=' ')

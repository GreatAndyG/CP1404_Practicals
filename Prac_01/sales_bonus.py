"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# sales = float(input("Enter sales: $"))
#
# if sales < 1000:
#     Bonues = sales * .1
#
#
# else:
#     Bonues = sales * .15
#
# print(Bonues)

sales = 0
while sales >= 0:
    sales = float(input("Enter sales: $"))
    if sales < 1000:
        bonues = sales * .1

    else:
        bonues = sales * .15
    print("Bonues is $ ",bonues,sep=' ')









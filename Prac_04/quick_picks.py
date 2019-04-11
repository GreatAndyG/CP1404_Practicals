"""Quick Pick Lottery Ticket Generator"""


import random



NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = int(input("How may quick picks? "))
    while number_of_quick_picks < 0:
        print("Cannot be less than 0")
        number_of_quick_picks = int(input("How many quick picks "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for p in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()

        print(" ".join("{:2}".format(number) for number in quick_pick))


main()

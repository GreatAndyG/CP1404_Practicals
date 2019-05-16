"""Test unreliable.car"""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Test UnreliableCars"""

    new_car = UnreliableCar("New Car", 100, 95)
    old_car = UnreliableCar("Old Car", 100, 25)

    for i in range(1, 40, 5):
        print("Drive car {}km:".format(i))
        print("{} drove {}km".format(new_car.name, new_car.drive(i)))
        print("{} drove {}km".format(old_car.name, old_car.drive(i)))

    print(new_car)
    print(old_car)


main()

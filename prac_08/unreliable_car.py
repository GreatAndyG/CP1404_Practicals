"""Unrealiable car class"""

from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """Unreliable Car"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """ Decide to Drive car based on reliability"""
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven




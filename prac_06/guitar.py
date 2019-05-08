"""Guitar class"""

CURRENT_YEAR = 2019
VINTAGE_AGE = 50


class Guitar:
    """class for storing details of a ."""

    def __init__(self, name='', year=0, cost=0):
        """Initialise a guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self, ):
        """Return a string for detials of a guitar."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get the age of guitar based on CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar is vintage or not based on age."""
        return (self.get_age()) >= VINTAGE_AGE

    def __lt__(self, other):
        """Sort guitar by year released"""
        return self.year < other.year

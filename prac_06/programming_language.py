class ProgrammingLanguage:
    """Represent information about  programing language"""

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of a programminglanguage"""


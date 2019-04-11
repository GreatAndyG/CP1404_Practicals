class ProgrammingLanguage:
    """Represent information about  programing language"""

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of a programming language"""
        return " {}, {} typing , Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                             self.year)

    def is_dynamic(self):
        """Determine if programming language is dynamically typed."""
        return self.typing == "Dynamic"

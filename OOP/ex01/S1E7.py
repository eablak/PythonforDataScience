from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """
        Initialize a Baratheon character with
        default traits and given first name."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """
        Return a user-friendly string representation
        of the Baratheon object."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a developer-friendly string
        representation of the Baratheon object."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):

    def __init__(self, first_name, is_alive=True):
        """Initialize a Lannister character with default
        traits and given first name."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Return a user-friendly string representation
        of the Baratheon object."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a developer-friendly string representation
        of the Baratheon object."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create and return a new Lannister instance
        with default traits."""
        return cls(first_name, is_alive)

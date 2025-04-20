from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """The mad King himself"""
    def __init__(self, first_name, is_alive=True):
        """Initialize the King with a first name and alive status."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, eye_color):
        """Set the eye color for the King."""
        self.eyes = eye_color

    def set_hairs(self, hair_color):
        """Set the hair color for the King."""
        self.hairs = hair_color

    def get_eyes(self):
        """Get the eye color of the King."""
        return (self.eyes)

    def get_hairs(self):
        """Get the hair color of the King."""
        return (self.hairs)

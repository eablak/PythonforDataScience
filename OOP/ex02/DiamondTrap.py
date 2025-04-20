from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """The mad King himself"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def set_eyes(self, eye_color):
        self.eyes = eye_color

    def set_hairs(self, hair_color):
        self.hairs = hair_color

    def get_eyes(self):
        return (self.eyes)

    def get_hairs(self):
        return (self.hairs)

from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract base class representing character status in game.

    Attributes:
        first_name = first name for character
        is_alive = life status for character
    """

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        self.is_alive = False


class Stark(Character):
    """
Inherits from Character.
Representing member of House Stark."""

    def __init__(self, first_name, is_alive=True):
        """
Initialize House Stark character.
Args:
first_name (str): first name for character
is_alive (bool): life status for character"""
        super().__init__(first_name, is_alive)

    def die(self):
        """
Change character's status in the game accordingly setting is_alive False"""
        self.is_alive = False

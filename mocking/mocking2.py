import unittest
from unittest.mock import MagicMock


class Actor:
    def jump_from_heli(self):
        return 'Nope, not gonna happen!'

    def light_on_fire(self):
        return 'Nooooooo way!'


class Movie:
    def __init__(self, actor):
        self.actor=actor

    def start_filmimng(self):
        self.actor.jump_from_heli()
        self.actor.light_on_fire()


class TestMovie(unittest.TestCase):
    def test_start_filming(self):
        stuntman=MagicMock()
        movie=Movie(stuntman)
        movie.start_filmimng()
        stuntman.jump_from_heli.assert_called()
        stuntman.light_on_fire.assert_called()



if __name__=='__main__':
    unittest.main()
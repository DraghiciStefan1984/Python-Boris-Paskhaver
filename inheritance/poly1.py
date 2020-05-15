import random


class Player:
    def __init__(self, games_played, victories):
        self.games_played=games_played
        self.victories=victories

    @property
    def win_ratio(self):
        return self.victories/self.games_played


class HumanPlayer(Player):
    def make_move(self):
        print('player makes move.')


class ComputerPlayer(Player):
    def make_move(self):
        print('computer makes move.')


hp=HumanPlayer(23, 15)
cp=ComputerPlayer(28, 19)

players=[hp, cp]
starting_player=random.choice(players)
starting_player.make_move()
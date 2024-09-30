import abc
import enum
import random

class Game(enum.Enum):
    Rock = "rock"
    Paper = "paper"
    Scissors = "scissors"
    Spock = "spock"
    Lizzard = "lizzard"


    @property
    def winners(self):
        return {
            Game.Rock : (Game.Scissors, Game.Lizzard),
            Game.Paper : (Game.Rock, Game.Spock),
            Game.Scissors : (Game.Paper, Game.Lizzard),
            Game.Lizzard : ( Game.Spock, Game.Paper),
            Game.Spock : (Game.Rock, Game.Scissors)
        }

    @classmethod
    def values(cls):
        return [op.value for op in Game]
    
    def __gt__(self, other):
        if other in self.winners[self]:
            return True 
        else:
            return False
    
class Player(abc.ABC):
    def __init__(self, name) -> None:
        self.name = name
        self.move = None
    def __str__(self):
        return f"Player: {self.name} move: {self.move}"
    def __gt__(self, other):
        return self.move > other.move
    
    @abc.abstractmethod
    def choose_move(self):
        pass
    
class HumanPlayer(Player):
    def choose_move(self):
        is_valid = False
        while not is_valid:
            value = input(f"Choose your move from {Game.values()}")
            value = value.lower().strip()
            try:
                self.move = Game(value)
                is_valid = True
            except ValueError as e:
                print(f"Your input should be in the list {Game.values()}") 

class ComputerPlayer(Player):
    def __init__(self) -> None:
        super().__init__("PC")

    def choose_move(self):
        self.move = random.choice([op for op in Game])


class GamePlay:

    def __init__(self, player1:Player, player2:Player):
        self.player1 = player1
        self.player2 = player2

    def determine_winner(self):
        if self.player1.move == self.player2.move:
            print("Draw")
        elif self.player1.move > self.player2.move:
            print(f"Player 1: {self.player1.name} won!!!")
        else:
            print(f"Player 2: {self.player2.name} won!!!")
        print(f"Player 1:  chose {self.player1.move}")
        print(f"Player 2:  chose {self.player2.move}")

    def play(self):
        while True:
            self.player1.choose_move()
            self.player2.choose_move()
            self.determine_winner()



# create a player class

class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None

    # function to make a choice

    def make_choice(self):
        raise NotImplementedError

    def __str__(self):
        return self.name


# create a human player class
class HumanPlayer(Player):
    # function to make a choice
    def make_choice(self):
        choices = ['rock', 'paper', 'scissors']
        while True:
            print(f"{self.name} make your choice")
            for i, choice in enumerate(choices):
                print(f"{i+1}. {choice}")
            choice = int(input()) - 1
            if 0 <= choice <= 2:
                self.choice = choices[choice]
                break
            else:
                print("Invalid choice, Try again")


# create a computer player class

class ComputerPlayer(Player):
    def make_choice(self):
        import random
        choices = ['rock', 'paper', 'scissors']
        self.choice = random.choice(choices)


class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]

    def play(self):
        for player in self.players:
            player.make_choice()
        self.show_choices()
        winner = self.get_winner()
        if winner:
            print(f"{winner} wins.")
        else:
            print("It's a tie.")

    def show_choices(self):
        print(f"{self.players[0]} chose {self.players[0].choice}")
        print(f"{self.players[1]} chose {self.players[1].choice}")

    def get_winner(self):
        choices = [p.choice for p in self.players]
        if choices[0] == choices[1]:
            return None

        if choices == ["rock", "scissors"]:
            return self.players[0]
        if choices == ['scissors', 'rock']:
            return self.players[1]
        if choices == ["paper", "rock"]:
            return self.players[0]
        if choices == ["rock", "paper"]:
            return self.players[1]
        if choices == ["scissors", "paper"]:
            return self.players[0]
        if choices == ["paper", "scissors"]:
            return self.players[1]


# create an object for the first player
player1 = HumanPlayer("Sanju")
# create an object for the second player(computer)
player2 = ComputerPlayer("Bot")

game = Game(player1, player2)
game.play()

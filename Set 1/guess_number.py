import random


class GuessTheNumber:
    def __init__(self):
        self.number = random.randint(1, 10)

    def play(self):
        while True:
            try:
                guess = int(input("Enter your guess: "))
                if guess < self.number:
                    print("Too low")
                elif guess > self.number:
                    print("Too high")
                else:
                    print(f'You got it🥳, the number was {self.number}.')
                    break
            except ValueError:
                print("Invalid input, try again.")


game = GuessTheNumber()
game.play()

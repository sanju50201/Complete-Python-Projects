import random

# create a hangman class


class Hangman:
    def __init__(self, word_list):
        self.word = random.choice(word_list).lower()
        self.remaining_lives = 6
        self.guessed_letters = set()
        self.display_word = ['_' for lette in self.word]

    # display the words

    def display(self):
        print("Current word:", " ".join(self.display_word))
        print(f"Remaining lives: {self.remaining_lives}")
        print("Guessed letters:", " ".join(sorted(self.guessed_letters)))

    # function to play
    def play(self):
        while self.remaining_lives > 0 and self.display_word:
            self.display()

            letter = input("Enter a letter: ").lower()

            if len(letter) != 1:
                print("Please enter a single letter.")
                continue
            if letter in self.guessed_letters:
                print(f'You already guessed "{letter}".')
                continue
            self.guessed_letters.add(letter)
            if letter in self.word:
                for i, c in enumerate(self.word):
                    if c == letter:
                        self.display_word[i] = c
                print(f'Correct! The letter "{letter}" is in the word.')
            else:
                self.remaining_lives -= 1
                print(f'Incorrect! The letter "{letter}" is not in the word.')

        if '_' not in self.display_word:
            print(f'Congratulations!🎊 You won. The word was "{self.word}".')
        else:
            print(f'Sorry😞, You lost, the word was "{self.word}".')


word_list = ['Java', 'Python', 'JavaScript']

game = Hangman(word_list)
game.play()

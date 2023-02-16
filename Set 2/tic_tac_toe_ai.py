# Tic Tac Toe AI using Minimax Algorithm

import random


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    # method to print the board

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        nums_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in nums_board:
            print("| " + " | ".join(row) + " |")

    # method to check for available moves
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    # method for empty squares

    def empty_squares(self):
        return " " in self.board

    # method to number of empty squares

    def num_empty_squares(self):
        return len(self.available_moves())

    # method to make a move

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.curernt_winner = letter
            return True
        return False

    # method to check for winner
    def winner(self, square, letter):
        # check the row
        row_index = square // 3
        row = self.board[row_index*3:(row_index+1)*3]
        if all([spot == letter for spot in row]):
            return True

        # check the column
        col_index = square % 3
        col = [self.board[col_index+i*3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        if square % 2 == 0:
            # check the diagonal
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    # method to check for game over
    def game_over(self):
        return self.num_empty_squares() == 0 or self.current_winner is not None

# function for minimax algorithm


def minimax(game, player):
    if game.current_winner:
        if game.current_winner == "O":
            return (None, 1)
        else:
            return (None, -1)
    elif not game.empty_squares():
        return (None, 0)
    elif player == "O":
        best_score = float("-inf")
        best_move = None

        for move in game.available_moves():
            game_copy = TicTacToe()
            game_copy.board = game.board[:]
            game_copy.make_move(move, player)
            score = minimax(game_copy, "X")[1]
            if score > best_score:
                best_score = score
                best_move = move
        return (best_move, best_score)
    elif player == "X":
        best_score = float("inf")
        best_move = None
        for move in game.available_moves():
            game_copy = TicTacToe()
            game_copy.board = game.board[:]
            game_copy.make_move(move, player)
            score = minimax(game_copy, "O")[1]
            if score < best_score:
                best_score = score
                best_move = move
        return (best_move, best_score)

# function to play the game


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = "X"
    while not game.game_over():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if square is not None and game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print("")

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter

            letter = "O" if letter == "X" else "X"

        else:
            print("Invalid move. Try again.")

    if print_game:
        print("It's a tie!")


# Human player class


class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter

    # method to get move
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val

# Random computer player class


class RandomComputerPlayer:
    def __init__(self, letter):
        self.letter = letter

    # method to get move
    def get_move(self, game):
        return random.choice(game.available_moves())

# Smart computer player class


class SmartComputerPlayer:
    def __init__(self, letter):
        self.letter = letter

    # method to get move
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = minimax(game, self.letter)[0]

# create an instance of the game


game = TicTacToe()
x_player = HumanPlayer("X")
o_player = SmartComputerPlayer("O")
play(game, x_player, o_player, print_game=True)

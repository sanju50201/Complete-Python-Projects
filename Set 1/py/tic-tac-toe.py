class TicTacToe:
    def __init__(self):
        self.board = [' ' for x in range(9)]
        self.player = 'X'

    # function to print the board

    def print_board(self):
        print(' {} | {} | {} '.format(
            self.board[0], self.board[1], self.board[2]))
        print('---+---+---')
        print(' {} | {} | {} '.format(
            self.board[3], self.board[4], self.board[5]))
        print('---+---+---')
        print(' {} | {} | {} '.format(
            self.board[6], self.board[7], self.board[8]))
        print()

    # function to make a move from the user

    def make_move(self, square):
        self.board[square] = self.player
        self.player = 'O' if self.player == 'X' else 'X'

    # check for winnner

    def check_for_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
            [0, 4, 8], [2, 4, 6]  # diagonals
        ]
        for combination in winning_combinations:

            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] and self.board[combination[0]] != ' ':
                return self.board[combination[0]]
        if ' ' not in self.board:
            return 'Tie'
        return None

    #  function to play

    def play(self):
        while True:
            self.print_board()
            print(f"Player {self.player} turn.")
            move = int(input("Enter your move (0-8): "))

            if self.board[move] != ' ':
                print("Square already filled. Try again.")
                continue
            self.make_move(move)
            winner = self.check_for_winner()

            if winner:
                self.print_board()
                print(f"Player {winner} wins the game")
                break


# creating a object for the class TicTacToe
game = TicTacToe()
game.play()

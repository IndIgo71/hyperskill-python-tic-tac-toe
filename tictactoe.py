class TicTacToe:
    __WIN_INDEXES = [[0, 1, 2], [3, 4, 5],
                     [6, 7, 8], [0, 3, 6],
                     [1, 4, 7], [2, 5, 8],
                     [0, 4, 8], [2, 4, 6]]

    __BOARDER = "---------"

    def __init__(self):
        self.current_player = None
        self.winner = None
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def change_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def print_board(self):
        print(self.__BOARDER)
        for i in range(len(self.board)):
            print('|', ' '.join(self.board[i]), '|')
        print(self.__BOARDER)

    def init_board_by_coords(self):
        coords = input()
        self.board = [list(coords[3 * i: 3 * (i + 1)].replace('_', ' ')) for i
                      in range(3)]

    def check_winnner(self):
        flat_board = [cell for row in self.board for cell in row]
        for win_index in self.__WIN_INDEXES:
            if ''.join([flat_board[i] for i in win_index]) == "XXX":
                self.winner = 'X'
            if ''.join([flat_board[i] for i in win_index]) == "OOO":
                self.winner = 'O'

    def is_finished(self):
        if all([cell != " " for row in self.board for cell in
                row]) or self.winner is not None:
            return True
        else:
            return False

    def game_result(self):
        if self.winner is None:
            print("Draw")
        else:
            print(f"{self.winner} wins")

    def user_move(self):
        while True:
            try:
                x, y = map(int, input("> ").split())
            except ValueError:
                print('You should enter numbers!')
            else:
                if not (0 < x <= 3 and 0 < y <= 3):
                    print("Coordinates should be from 1 to 3!")
                elif self.board[x - 1][y - 1] == ' ':
                    self.board[x - 1][y - 1] = self.current_player
                    break
                else:
                    print("This cell is occupied! Choose another one!")

    def start_game(self, starting_player):
        self.current_player = starting_player
        self.print_board()
        while not self.is_finished():
            self.user_move()
            self.print_board()
            self.check_winnner()
            self.change_player()
        self.game_result()


if __name__ == '__main__':
    starting_player = 'X'
    game = TicTacToe()
    game.start_game(starting_player)

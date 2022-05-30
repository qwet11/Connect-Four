def divider():
    print("-" * 50)
    print("\n")

class Connect_Four():
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        self.game_over = False
        self.turns = 0
    
    def play(self):
        self.turns = 0
        while not self.game_over:
            self.board.print_board()
            if self.turns % 2 == 0:
                self.player1.play(self.board)
            else:
                self.player2.play(self.board)
            self.check_winner()
            self.turns += 1

        self.board.print_board()
        print("{} won!".format(self.winner))
    
    def check_winner(self):
        self.game_over = self.board.check_game_over()
        if self.game_over:
            if self.turns % 2 == 0:
                self.winner = self.player1.name
            else:
                self.winner = self.player2.name

class Player():
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    
    def play(self, board):
        # Plays a turn
        print("It's {}'s turn".format(self.name))
        col = -1
        while not board.check_valid(col):
            col = input("Enter a column (1-7): ")

            col = int(col) - 1
        
        board.drop_piece(col, self.symbol)
        divider()


class Board():
    num_row = 6
    num_col = 7

    def __init__(self):
        self.board = [[' ' for col in range(Board.num_col)] for row in range(Board.num_row)]
    
    def print_board(self):
        for row in self.board:
            print(row)
        print("\n")
    
    def check_game_over(self):
        # Check for horizontal win
        for row in self.board:
            for i in range(3):
                if row[i] == row[i+1] == row[i+2] == row[i+3] != ' ':
                    return True

        # Check for vertical win
        for i in range(3):
            for j in range(6):
                if self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j] != ' ':
                    return True

        # Check for diagonal win
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3] != ' ':
                    return True

        # Check for diagonal win
        for i in range(3):
            for j in range(3, 6):
                if self.board[i][j] == self.board[i+1][j-1] == self.board[i+2][j-2] == self.board[i+3][j-3] != ' ':
                    return True
        return False
    
    def check_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True
    
    def check_valid(self, col):
        if col < 0 or col > 6:
            return False
        if self.board[0][col] != ' ':
            return False
        return True
    
    def drop_piece(self, col, player_symbol):
        for row in range(Board.num_row-1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = player_symbol
                return True
        return False

if __name__ == '__main__':
    board = Board()
    player1 = Player('Player 1', 'X')
    player2 = Player('Player 2', 'O')
    connect_four = Connect_Four(board, player1, player2)
    connect_four.play()
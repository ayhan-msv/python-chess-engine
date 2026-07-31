#
#
#
# 
#
from enums import Player


class Piece:
    #
    def __init__(self, name, row_number, col_number, player):
        self._name = name
        self.row_number = row_number
        self.col_number = col_number
        self._player = player

    #
    def get_row_number(self):
        return self.row_number

    #
    def get_col_number(self):
        return self.col_number

    # 
    def get_name(self):
        return self._name

    def get_player(self):
        return self._player

    def is_player(self, player_checked):
        return self.get_player() == player_checked

    def can_move(self, board, starting_square):
        pass

    def can_take(self, is_check):
        pass

    def change_row_number(self, new_row_number):
        self.row_number = new_row_number

    def change_col_number(self, new_col_number):
        self.col_number = new_col_number

    def get_valid_piece_takes(self, game_state):
        pass

    def get_valid_peaceful_moves(self, game_state):
        pass

    #
    def get_valid_piece_moves(self, board):
        pass


#
class Rook(Piece):
    def __init__(self, name, row_number, col_number, player):
        super().__init__(name, row_number, col_number, player)
        self.has_moved = False

    def get_valid_peaceful_moves(self, game_state):
        return self.traverse(game_state)[0]

    def get_valid_piece_takes(self, game_state):
        return self.traverse(game_state)[1]

    def get_valid_piece_moves(self, game_state):
        return self.get_valid_peaceful_moves(game_state) + self.get_valid_piece_takes(game_state)

    def traverse(self, game_state):
        _peaceful_moves = []
        _piece_takes = []

        self._up = 1
        self._down = 1
        self._left = 1
        self._right = 1

        #
        self._breaking_point = False
        while self.get_col_number() - self._left >= 0 and not self._breaking_point:
            # 
            if game_state.get_piece(self.get_row_number(), self.get_col_number() - self._left) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number(), self.get_col_number() - self._left))
                self._left += 1
            #
            elif game_state.is_valid_piece(self.get_row_number(), self.get_col_number() - self._left) and \
                    not game_state.get_piece(self.get_row_number(), self.get_col_number() - self._left).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number(), self.get_col_number() - self._left))
                self._breaking_point = True
            else:
                self._breaking_point = True

        #
        self._breaking_point = False
        while self.get_col_number() + self._right < 8 and not self._breaking_point:
            #
            if game_state.get_piece(self.get_row_number(), self.get_col_number() + self._right) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number(), self.get_col_number() + self._right))
                self._right += 1
            #
            elif game_state.is_valid_piece(self.get_row_number(), self.get_col_number() + self._right) and \
                    not game_state.get_piece(self.get_row_number(), self.get_col_number() + self._right).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number(), self.get_col_number() + self._right))
                self._breaking_point = True
            else:
                self._breaking_point = True

        #
        self._breaking_point = False
        while self.get_row_number() + self._down < 8 and not self._breaking_point:
            # 
            if game_state.get_piece(self.get_row_number() + self._down, self.get_col_number()) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number() + self._down, self.get_col_number()))
                self._down += 1
            # 
            elif game_state.is_valid_piece(self.get_row_number() + self._down, self.get_col_number()) and \
                    not game_state.get_piece(self.get_row_number() + self._down, self.get_col_number()).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number() + self._down, self.get_col_number()))
                self._breaking_point = True
            else:
                self._breaking_point = True

        # 
        self._breaking_point = False
        while self.get_row_number() - self._up >= 0 and not self._breaking_point:
            #
            if game_state.get_piece(self.get_row_number() - self._up, self.get_col_number()) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number() - self._up, self.get_col_number()))
                self._up += 1
            #
            elif game_state.is_valid_piece(self.get_row_number() - self._up, self.get_col_number()) and \
                    not game_state.get_piece(self.get_row_number() - self._up, self.get_col_number()).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number() - self._up, self.get_col_number()))
                self._breaking_point = True
            else:
                self._breaking_point = True
        return (_peaceful_moves, _piece_takes)


#
class Knight(Piece):
    def get_valid_peaceful_moves(self, game_state):
        _moves = []
        row_change = [-2, -2, -1, -1, +1, +1, +2, +2]
        col_change = [-1, +1, -2, +2, -2, +2, +1, -1]

        for i in range(0, 8):
            new_row = self.get_row_number() + row_change[i]
            new_col = self.get_col_number() + col_change[i]
            evaluating_square = game_state.get_piece(new_row, new_col)
            #
            if evaluating_square == Player.EMPTY:
                _moves.append((new_row, new_col))
        return _moves

    def get_valid_piece_takes(self, game_state):
        _moves = []
        row_change = [-2, -2, -1, -1, +1, +1, +2, +2]
        col_change = [-1, +1, -2, +2, -2, +2, +1, -1]

        for i in range(0, 8):
            new_row = self.get_row_number() + row_change[i]
            new_col = self.get_col_number() + col_change[i]
            evaluating_square = game_state.get_piece(new_row, new_col)
            #
            if game_state.is_valid_piece(new_row, new_col) and self.get_player() is not evaluating_square.get_player():
                _moves.append((new_row, new_col))
        return _moves

    def get_valid_piece_moves(self, game_state):

        return self.get_valid_peaceful_moves(game_state) + self.get_valid_piece_takes(game_state)
#
class Bishop(Piece):
    def __init__(self, name, row_number, col_number, player):
        super().__init__(name, row_number, col_number, player)

    def get_valid_piece_takes(self, game_state):
        return self.traverse(game_state)[1]

    def get_valid_peaceful_moves(self, game_state):
        return self.traverse(game_state)[0]

    def get_valid_piece_moves(self, game_state):
        return self.get_valid_piece_takes(game_state) + self.get_valid_peaceful_moves(game_state)

    def traverse(self, game_state):
        _peaceful_moves = []
        _piece_takes = []

        self._breaking_point = False
        self._up = 1
        self._down = 1
        self._left = 1
        self._right = 1
        while self.get_col_number() - self._left >= 0 and self.get_row_number() - self._up >= 0 and not self._breaking_point:
            #
            if game_state.get_piece(self.get_row_number() - self._up, self.get_col_number() - self._left) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number() - self._up, self.get_col_number() - self._left))
                self._left += 1
                self._up += 1
            #
            elif game_state.is_valid_piece(self.get_row_number() - self._up, self.get_col_number() - self._left) and \
                    not game_state.get_piece(self.get_row_number() - self._up, self.get_col_number() - self._left).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number() - self._up, self.get_col_number() - self._left))
                self._breaking_point = True
            else:
                self._breaking_point = True

        #
        self._breaking_point = False
        self._up = 1
        self._down = 1
        self._left = 1
        self._right = 1
        while self.get_col_number() + self._right < 8 and self.get_row_number() - self._up >= 0 and not self._breaking_point:
            # 
            if game_state.get_piece(self.get_row_number() - self._up, self.get_col_number() + self._right) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number() - self._up, self.get_col_number() + self._right))
                self._right += 1
                self._up += 1
            #
            elif game_state.is_valid_piece(self.get_row_number() - self._up, self.get_col_number() + self._right) and \
                    not game_state.get_piece(self.get_row_number() - self._up, self.get_col_number() + self._right).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number() - self._up, self.get_col_number() + self._right))
                self._breaking_point = True
            else:
                self._breaking_point = True

        #
        self._breaking_point = False
        self._up = 1
        self._down = 1
        self._left = 1
        self._right = 1
        while self.get_col_number() - self._left >= 0 and self.get_row_number() + self._down < 8 and not self._breaking_point:
            #
            if game_state.get_piece(self.get_row_number() + self._down, self.get_col_number() - self._left) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number() + self._down, self.get_col_number() - self._left))
                self._down += 1
                self._left += 1
            #
            elif game_state.is_valid_piece(self.get_row_number() + self._down, self.get_col_number() - self._left) and \
                    not game_state.get_piece(self.get_row_number() + self._down, self.get_col_number() - self._left).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number() + self._down, self.get_col_number() - self._left))
                self._breaking_point = True
            else:
                self._breaking_point = True

        #
        self._breaking_point = False
        self._up = 1
        self._down = 1
        self._left = 1
        self._right = 1
        while self.get_col_number() + self._right < 8 and self.get_row_number() + self._down < 8 and not self._breaking_point:
            #
            if game_state.get_piece(self.get_row_number() + self._down, self.get_col_number() + self._right) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number() + self._down, self.get_col_number() + self._right))
                self._down += 1
                self._right += 1
            #
            elif game_state.is_valid_piece(self.get_row_number() + self._down, self.get_col_number() + self._right) and \
                    not game_state.get_piece(self.get_row_number() + self._down, self.get_col_number() + self._right).is_player(
                        self.get_player()):
                _piece_takes.append((self.get_row_number() + self._down, self.get_col_number() + self._right))
                self._breaking_point = True
            else:
                self._breaking_point = True
        return (_peaceful_moves, _piece_takes)



#
class Pawn(Piece):
    def get_valid_piece_takes(self, game_state):
        _moves = []
        if self.is_player(Player.PLAYER_1):
            #
            if game_state.is_valid_piece(self.get_row_number() + 1, self.get_col_number() - 1) and \
                    game_state.get_piece(self.get_row_number() + 1, self.get_col_number() - 1).is_player(Player.PLAYER_2):
                _moves.append((self.get_row_number() + 1, self.get_col_number() - 1))
            #
            if game_state.is_valid_piece(self.get_row_number() + 1, self.get_col_number() + 1) and \
                    game_state.get_piece(self.get_row_number() + 1, self.get_col_number() + 1).is_player(Player.PLAYER_2):
                _moves.append((self.get_row_number() + 1, self.get_col_number() + 1))
            if game_state.can_en_passant(self.get_row_number(), self.get_col_number()):
                _moves.append((self.get_row_number() + 1, game_state.previous_piece_en_passant()[1]))
        #
        elif self.is_player(Player.PLAYER_2):
            # 
            if game_state.is_valid_piece(self.get_row_number() - 1, self.get_col_number() - 1) and \
                    game_state.get_piece(self.get_row_number() - 1, self.get_col_number() - 1).is_player(Player.PLAYER_1):
                _moves.append((self.get_row_number() - 1, self.get_col_number() - 1))
            #
            if game_state.is_valid_piece(self.get_row_number() - 1, self.get_col_number() + 1) and \
                    game_state.get_piece(self.get_row_number() - 1, self.get_col_number() + 1).is_player(Player.PLAYER_1):
                _moves.append((self.get_row_number() - 1, self.get_col_number() + 1))
            if game_state.can_en_passant(self.get_row_number(), self.get_col_number()):
                _moves.append((self.get_row_number() - 1, game_state.previous_piece_en_passant()[1]))
        return _moves

    def get_valid_peaceful_moves(self, game_state):
        _moves = []
        #
        if self.is_player(Player.PLAYER_1):
            #
            if game_state.get_piece(self.get_row_number() + 1, self.get_col_number()) == Player.EMPTY:
                #
                if self.get_row_number() == 1 and game_state.get_piece(self.get_row_number() + 2,
                                                                       self.get_col_number()) == Player.EMPTY:
                    _moves.append((self.get_row_number() + 1, self.get_col_number()))
                    _moves.append((self.get_row_number() + 2, self.get_col_number()))
                #
                else:
                    _moves.append((self.get_row_number() + 1, self.get_col_number()))
        #
        elif self.is_player(Player.PLAYER_2):
            #
            if game_state.get_piece(self.get_row_number() - 1, self.get_col_number()) == Player.EMPTY:
                # 
                if self.get_row_number() == 6 and game_state.get_piece(self.get_row_number() - 2,
                                                                       self.get_col_number()) == Player.EMPTY:
                    _moves.append((self.get_row_number() - 1, self.get_col_number()))
                    _moves.append((self.get_row_number() - 2, self.get_col_number()))
                # 
                else:
                    _moves.append((self.get_row_number() - 1, self.get_col_number()))
        return _moves

    def get_valid_piece_moves(self, game_state):

        return self.get_valid_peaceful_moves(game_state) + self.get_valid_piece_takes(game_state)


#
class Queen(Rook, Bishop):
    def get_valid_peaceful_moves(self, game_state):
        return (Rook.get_valid_peaceful_moves(Rook(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), game_state) +
                Bishop.get_valid_peaceful_moves(Bishop(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), game_state))

    def get_valid_piece_takes(self, game_state):
        return (Rook.get_valid_piece_takes( Rook(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), game_state) +
                Bishop.get_valid_piece_takes(Bishop(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), game_state))

    def get_valid_piece_moves(self, game_state):
        return (Rook.get_valid_piece_moves(Rook(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), game_state) +
                Bishop.get_valid_piece_moves(Bishop(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), game_state))

#
class King(Piece):
    def get_valid_piece_takes(self, game_state):
        _moves = []
        row_change = [-1, +0, +1, -1, +1, -1, +0, +1]
        col_change = [-1, -1, -1, +0, +0, +1, +1, +1]

        for i in range(0, 8):
            new_row = self.get_row_number() + row_change[i]
            new_col = self.get_col_number() + col_change[i]
            evaluating_square = game_state.get_piece(new_row, new_col)
            #
            if game_state.is_valid_piece(new_row, new_col):
                #
                if self.is_player(Player.PLAYER_1) and evaluating_square.is_player(Player.PLAYER_2):
                    _moves.append((new_row, new_col))
                #
                elif self.is_player(Player.PLAYER_2) and evaluating_square.is_player(Player.PLAYER_1):
                    _moves.append((new_row, new_col))
        return _moves

    def get_valid_peaceful_moves(self, game_state):
        _moves = []
        row_change = [-1, +0, +1, -1, +1, -1, +0, +1]
        col_change = [-1, -1, -1, +0, +0, +1, +1, +1]

        for i in range(0, 8):
            new_row = self.get_row_number() + row_change[i]
            new_col = self.get_col_number() + col_change[i]
            evaluating_square = game_state.get_piece(new_row, new_col)
            # when the square with new_row and new_col is empty
            if evaluating_square == Player.EMPTY:
                _moves.append((new_row, new_col))

        if game_state.king_can_castle_left(self.get_player()):
            if self.is_player(Player.PLAYER_1):
                _moves.append((0, 1))
            elif self.is_player(Player.PLAYER_2):
                _moves.append((7, 1))
        elif game_state.king_can_castle_right(self.get_player()):
            if self.is_player(Player.PLAYER_1):
                _moves.append((0, 5))
            elif self.is_player(Player.PLAYER_2):
                _moves.append((7, 5))
        return _moves

    def get_valid_piece_moves(self, game_state):
 
        return self.get_valid_peaceful_moves(game_state) + self.get_valid_piece_takes(game_state)

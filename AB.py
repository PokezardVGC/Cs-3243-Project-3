import sys
from copy import deepcopy
from random import choice, seed

# Helper functions to aid in your implementation. Can edit/remove
#############################################################################
all_pieces = {('a', 1): ('Ferz', 'White'), ('a', 5): ('Ferz', 'Black'), ('g', 1):
    ('Ferz', 'White'), ('g', 5): ('Ferz', 'Black'), ('b', 1): ('Pawn',
                                                               'White'), ('b', 5): ('Pawn', 'Black'),
              ('c', 1): ('Pawn', 'White'),
              ('c', 5): ('Pawn', 'Black'), ('d', 1): ('Pawn', 'White'), ('d', 5):
                  ('Pawn', 'Black'), ('e', 1): ('Pawn', 'White'), ('e', 5): ('Pawn',
                                                                             'Black'), ('f', 1): ('Pawn', 'White'),
              ('f', 5): ('Pawn', 'Black'),
              ('a', 0): ('Knight', 'White'), ('a', 6): ('Knight', 'Black'), ('b',
                                                                             0): ('Bishop', 'White'),
              ('b', 6): ('Bishop', 'Black'), ('c', 0):
                  ('Queen', 'White'), ('c', 6): ('Queen', 'Black'), ('d', 0): ('King',
                                                                               'White'), ('d', 6): ('King', 'Black'),
              ('e', 0): ('Princess', 'White'),
              ('e', 6): ('Princess', 'Black'), ('f', 0): ('Empress', 'White'),
              ('f', 6): ('Empress', 'Black'), ('g', 0): ('Rook', 'White'), ('g',
                                                                            6): ('Rook', 'Black')}


######## Piece
#############################################################################

def get_start_to_end(coord, lis):
    ls = []
    for item in lis:
        ls.append((coord, item))
    return ls


def get_actions(coord, piece, grid):
    # aps, 1st coord is x, 2nd is y
    if piece[0] == "Pawn":
        return get_start_to_end(coord, get_pawn_actions(coord[0], coord[1], grid, 7, 7, piece[1]))
    elif piece[0] == "King":
        return get_start_to_end(coord, get_king_actions(coord[0], coord[1], grid, 7, 7, piece[1]))
    elif piece[0] == "Ferz":
        return get_start_to_end(coord, get_frez_actions(coord[0], coord[1], grid, 7, 7, piece[1]))
    elif piece[0] == "Knight":
        return get_start_to_end(coord, get_knight_actions(coord[0], coord[1], grid, 7, 7, piece[1]))
    elif piece[0] == "Rook":
        return get_start_to_end(coord, get_rook_actions(coord[0], coord[1], grid, 7, 7, piece[1]))
    elif piece[0] == "Bishop":
        return get_start_to_end(coord, get_bishop_actions(coord[0], coord[1], grid, 7, 7, piece[1]))
    elif piece[0] == "Queen":
        return get_start_to_end(coord, get_queen_actions(coord[0], coord[1], grid, 7, 7, piece[1]))
    elif piece[0] == "Empress":
        return get_start_to_end(coord, get_empress_actions(coord[0], coord[1], grid, 7, 7, piece[1]))
    elif piece[0] == "Princess":
        return get_start_to_end(coord, get_princess_actions(coord[0], coord[1], grid, 7, 7, piece[1]))


def get_king_actions(y, x, grid, row, col, own_color):
    ls = []
    right = (y, x + 1)
    ls.append(right)
    diag_right_up = (y + 1, x + 1)
    ls.append(diag_right_up)

    left = (y, x - 1)
    ls.append(left)
    diag_left_up = (y + 1, x - 1)
    ls.append(diag_left_up)

    down = (y - 1, x)
    ls.append(down)
    diag_left_down = (y - 1, x - 1)
    ls.append(diag_left_down)

    up = (y + 1, x)
    ls.append(up)
    diag_right_down = (y - 1, x + 1)
    ls.append(diag_right_down)

    pieces = ls.copy()
    for piece in ls:
        # assume a is start
        if piece[1] >= col or piece[1] < 0 or piece[0] < 0 or piece[0] >= row:
            pieces.remove(piece)

    # remove tiles with own piece color
    copy_pieces = pieces.copy()
    for piece in copy_pieces:
        if grid[piece]:
            side_color = grid[piece][1]
            if side_color == own_color:
                pieces.remove(piece)
    return pieces


def get_frez_actions(y, x, grid, row, col, own_color):
    ls = []
    if y + 1 < row:
        if x - 1 >= 0:
            diag_left_up = (y + 1, x - 1)
            ls.append(diag_left_up)
        if x + 1 < col:
            diag_right_up = (y + 1, x + 1)
            ls.append(diag_right_up)

    if y - 1 >= 0:
        if x - 1 >= 0:
            diag_left_down = (y - 1, x - 1)
            ls.append(diag_left_down)
        if x + 1 < col:
            diag_right_down = (y - 1, x + 1)
            ls.append(diag_right_down)

    pieces = ls.copy()
    for piece in ls:
        # assume a is start
        if piece[1] >= col or piece[1] < 0 or piece[0] < 0 or piece[0] >= row:
            pieces.remove(piece)

    copy_pieces = pieces.copy()
    for piece in copy_pieces:
        if grid[piece]:
            side_color = grid[piece][1]
            if side_color == own_color:
                pieces.remove(piece)
    return pieces


def get_knight_actions(y, x, grid, row, col, own_color):
    ls = []

    top_left = (y + 2, x - 1)
    ls.append(top_left)
    top_right = (y + 2, x + 1)
    ls.append(top_right)

    bottom_left = (y - 2, x - 1)
    ls.append(bottom_left)
    bottom_right = (y - 2, x + 1)
    ls.append(bottom_right)

    left_top = (y + 1, x - 2)
    ls.append(left_top)

    left_bottom = (y - 1, x - 2)
    ls.append(left_bottom)

    right_top = (y + 1, x + 2)
    ls.append(right_top)

    right_bottom = (y - 1, x + 2)
    ls.append(right_bottom)

    pieces = ls.copy()
    for piece in ls:
        # assume a is start
        if piece[1] >= col or piece[1] < 0 or piece[0] < 0 or piece[0] >= row:
            pieces.remove(piece)

    copy_pieces = pieces.copy()
    for piece in copy_pieces:
        if grid[piece]:
            side_color = grid[piece][1]
            if side_color == own_color:
                pieces.remove(piece)
    return pieces


def get_rook_actions(y, x, grid, row, col, own_color):
    ls = []

    # rook like movement
    for i in range(x - 1, -1, -1):
        piece = (y, i)
        if grid[piece]:
            tile_color = grid[piece][1]
            if tile_color == own_color:  # same team, stop in front
                break
            else:
                ls.append(piece)  # capture piece and break
                break
        ls.append(piece)

    for i in range(x + 1, col):
        piece = (y, i)
        if grid[piece]:
            tile_color = grid[piece][1]
            if tile_color == own_color:  # same team, stop in front
                break
            else:
                ls.append(piece)  # capture piece and break
                break
        ls.append(piece)

    for i in range(y - 1, -1, -1):
        piece = (i, x)
        if grid[piece]:
            tile_color = grid[piece][1]
            if tile_color == own_color:  # same team, stop in front
                break
            else:
                ls.append(piece)  # capture piece and break
                break
        ls.append(piece)

    for i in range(y + 1, row):
        piece = (i, x)
        if grid[piece]:
            tile_color = grid[piece][1]
            if tile_color == own_color:  # same team, stop in front
                break
            else:
                ls.append(piece)  # capture piece and break
                break
        ls.append(piece)
    return ls


def get_bishop_actions(y, x, grid, row, col, own_color):
    ls = []

    counter_2 = 0
    for i in range(x - 1, - 1, -1):
        counter_2 -= 1
        if col > y + counter_2:
            piece = (y + counter_2, i)
            if y + counter_2 < 0:
                break
            elif grid[piece]:
                tile_color = grid[piece][1]
                if tile_color == own_color:  # same team, stop in front
                    break
                else:
                    ls.append(piece)  # capture piece and break
                    break
            ls.append(piece)

    counter_1 = 0
    for i in range(x + 1, col):
        counter_1 += 1
        if row > y + counter_1:
            piece = (y + counter_1, i)
            if grid[piece]:
                tile_color = grid[piece][1]
                if tile_color == own_color:  # same team, stop in front
                    break
                else:
                    ls.append(piece)  # capture piece and break
                    break
            ls.append(piece)

    counter_3 = 0
    for i in range(y - 1, - 1, -1):
        counter_3 += 1
        if col > x + counter_3:
            piece = (i, x + counter_3)
            if grid[piece]:
                tile_color = grid[piece][1]
                if tile_color == own_color:  # same team, stop in front
                    break
                else:
                    ls.append(piece)  # capture piece and break
                    break
            ls.append(piece)

    counter_4 = 0
    for i in range(y + 1, row):
        counter_4 += 1
        if x - counter_4 >= 0:
            piece = (i, x - counter_4)
            if grid[piece]:
                tile_color = grid[piece][1]
                if tile_color == own_color:  # same team, stop in front
                    break
                else:
                    ls.append(piece)  # capture piece and break
                    break
            ls.append(piece)
    return ls


def get_queen_actions(y, x, grid, row, col, own_color):
    ls = []
    ls.extend(get_rook_actions(y, x, grid, row, col, own_color))
    ls.extend(get_bishop_actions(y, x, grid, row, col, own_color))
    return ls


def get_empress_actions(y, x, grid, row, col, own_color):
    ls = []
    ls.extend(get_rook_actions(y, x, grid, row, col, own_color))
    ls.extend(get_knight_actions(y, x, grid, row, col, own_color))
    return ls


def get_princess_actions(y, x, grid, row, col, own_color):
    ls = []
    ls.extend(get_bishop_actions(y, x, grid, row, col, own_color))
    ls.extend(get_knight_actions(y, x, grid, row, col, own_color))
    return ls


def get_pawn_actions(y, x, grid, row, col, own_color):
    ls = []

    if own_color == "White":
        piece = (y, x + 1)
        if x + 1 < row and not grid[piece]:  # there is no piece in front
            ls.append(piece)
        piece = (y - 1, x + 1)
        if y - 1 >= 0 and x + 1 < row and grid[piece] and grid[piece][1] != own_color:
            ls.append(piece)
        piece = (y + 1, x + 1)
        if y + 1 < col and x + 1 < row and grid[piece] and grid[piece][1] != own_color:
            ls.append(piece)

    if own_color == "Black":
        piece = (y, x - 1)
        if x - 1 >= 0 and not grid[piece]:  # there is no piece in front
            ls.append(piece)
        piece = (y - 1, x - 1)
        if y - 1 >= 0 and x - 1 >= 0 and grid[piece] and grid[piece][1] != own_color:
            ls.append(piece)
        piece = (y + 1, x - 1)
        if y + 1 < col and x - 1 >= 0 and grid[piece] and grid[piece][1] != own_color:
            ls.append(piece)

    return ls


#############################################################################
######## Board
#############################################################################
class Board:
    pass


#############################################################################
######## State
#############################################################################
class State:

    def __init__(self, rows, cols, board, turn, is_terminal):
        self.rows = rows
        self.cols = cols
        self.board = board
        self.turn = turn
        self.is_terminal = is_terminal

    def whose_turn(self):
        colours = ["White", "Black"]
        return colours[self.turn % 2]

    def get_actions(self, curr_turn):
        moves = {
            'King': [],
            'Ferz': [],
            'Rook': [],
            'Bishop': [],
            'Knight': [],
            'Queen': [],
            'Empress': [],
            'Princess': [],
            'Pawn': []
        }

        for coord, piece in self.board.items():
            if piece:
                if piece[1] == curr_turn:
                    type = piece[0]
                    actions = get_actions(coord, piece, self.board)
                    moves[type].extend(actions)
        ls = []
        for value in moves.values():
            ls.extend(value)
        return ls

    def move(self, coord):
        if not coord:
            return State(0, 0, {}, -1, False)
        old_coord = coord[0]
        new_coord = coord[1]
        piece = self.board[old_coord]
        terminate = False
        attacking_tile = self.board[new_coord]
        if attacking_tile and attacking_tile[0] == "King" and attacking_tile[1] != piece[1]:
            terminate = True
        copy_board = deepcopy(self.board)
        copy_board[old_coord] = False
        # if copy_board[new_coord]:
        #     captured_piece = copy_board[new_coord]
        copy_board[new_coord] = piece
        state = State(self.rows, self.cols, copy_board, self.turn + 1, terminate)
        return state

    def utility(self):
        colours = ["White", "Black"]
        points = {
            "Pawn": 1,
            "Ferz": 2,
            "Knight": 3,
            "Bishop": 3,
            "Rook": 5,
            "Princess": 6,
            "Empress": 8,
            "Queen": 9,
            "King": 200,
            "Movement": 0.1
        }
        count = {
            "Pawn": 0,
            "Ferz": 0,
            "Knight": 0,
            "Bishop": 0,
            "Rook": 0,
            "Princess": 0,
            "Empress": 0,
            "Queen": 0,
            "King": 0,
            "Movement": len(self.get_actions(colours[0])) -
                        len(self.get_actions(colours[1]))
        }
        turn = "White"
        for value in self.board.values():
            if value:
                piece = value[0]
                color = value[1]
                if color == turn:
                    count[piece] += 1
                else:
                    count[piece] -= 1
        total = 0
        for key, value in count.items():
            curr_point = points[key]
            curr_point *= value
            total += curr_point

        return total


# Implement your minimax with alpha-beta pruning algorithm here.

def max_val(state, alpha, beta, depth):
    move = 0
    if state.is_terminal or depth == 0:
        return state.utility(), None
    v = -float('inf')
    for action in state.get_actions(state.whose_turn()):
        v2, _ = min_val(state.move(action), alpha, beta, depth - 1)
        if v2 > v:
            v, move = v2, action
            alpha = max(alpha, v)
        if v >= beta:
            return v, move
    return v, move


def min_val(state, alpha, beta, depth):
    move = 0
    if state.is_terminal or depth == 0:
        return state.utility(), None
    v = float('inf')
    for action in state.get_actions(state.whose_turn()):
        v2, _ = max_val(state.move(action), alpha, beta, depth - 1)
        if v2 < v:
            v, move = v2, action
            beta = min(beta, v)
        if v <= alpha:
            return v, move
    return v, move


def to_alpha_numeric(coord):
    return chr(coord[0] + 97), coord[1]


def ab(gameboard):
    colours = ["White", "Black"]
    rows = 7
    cols = 7
    pieces = gameboard
    grid = {}
    for row in range(rows):
        for col in range(cols):
            grid[(row, col)] = False
    for key, value in pieces.items():
        grid[(ord(key[0]) - 97, key[1])] = value
    # format of (col, row) (a, 0)
    state = State(rows, cols, grid, 0, False)
    seed(4200)
    depth = choice([3, 3, 2, 2, 2, 2, 2, 2])
    value, move = max_val(state, -float('inf'), float('inf'), depth)
    return to_alpha_numeric(move[0]), to_alpha_numeric(move[1])


#############################################################################
######## Parser function and helper functions
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
# Return number of rows, cols, grid containing obstacles and step costs of coordinates, enemy pieces, own piece, and goal positions
def parse(testcase):
    handle = open(testcase, "r")

    get_par = lambda x: x.split(":")[1]
    rows = int(get_par(handle.readline()))  # Integer
    cols = int(get_par(handle.readline()))  # Integer
    gameboard = {}

    enemy_piece_nums = get_par(handle.readline()).split()
    num_enemy_pieces = 0  # Read Enemy Pieces Positions
    for num in enemy_piece_nums:
        num_enemy_pieces += int(num)

    handle.readline()  # Ignore header
    for i in range(num_enemy_pieces):
        line = handle.readline()[1:-2]
        coords, piece = add_piece(line)
        gameboard[coords] = (piece, "Black")

    own_piece_nums = get_par(handle.readline()).split()
    num_own_pieces = 0  # Read Own Pieces Positions
    for num in own_piece_nums:
        num_own_pieces += int(num)

    handle.readline()  # Ignore header
    for i in range(num_own_pieces):
        line = handle.readline()[1:-2]
        coords, piece = add_piece(line)
        gameboard[coords] = (piece, "White")

    return rows, cols, gameboard


class Piece(object):
    pass


def add_piece(comma_seperated) -> Piece:
    piece, ch_coord = comma_seperated.split(",")
    r, c = from_chess_coord(ch_coord)
    return [(r, c), piece]


def from_chess_coord(ch_coord):
    return (int(ch_coord[1:]), ord(ch_coord[0]) - 97)


# You may call this function if you need to set up the board
def setUpBoard():
    config = sys.argv[1]
    rows, cols, gameboard = parse(config)


### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# Chess Pieces: King, Queen, Knight, Bishop, Rook, Princess, Empress, Ferz, Pawn (First letter capitalized)
# Colours: White, Black (First Letter capitalized)
# Positions: Tuple. (column (String format), row (Int)). Example: ('a', 0)

# Parameters:
# gameboard: Dictionary of positions (Key) to the tuple of piece type and its colour (Value). This represents the current pieces left on the board.
# Key: position is a tuple with the x-axis in String format and the y-axis in integer format.
# Value: tuple of piece type and piece colour with both values being in String format. Note that the first letter for both type and colour are capitalized as well.
# gameboard example: {('a', 0) : ('Queen', 'White'), ('d', 10) : ('Knight', 'Black'), ('g', 25) : ('Rook', 'White')}
#
# Return value:
# move: A tuple containing the starting position of the piece being moved to the new ending position for the piece. x-axis in String format and y-axis in integer format.
# move example: (('a', 0), ('b', 3))

def studentAgent(gameboard):
    # You can code in here but you cannot remove this function, change its parameter or change the return type
    move = ab(gameboard)
    return move  # Format to be returned (('a', 0), ('b', 3))


# print(studentAgent(all_pieces))

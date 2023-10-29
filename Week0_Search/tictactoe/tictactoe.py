"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy   # Requirement to use deep copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_turn_x = 0
    count_turn_o = 0

    # if the board state and inital state are same then first turn will X
    if board == initial_state():
        return X           

    # count the number of X and O in board to decide the which player have next turn
    else:
        for i in board:
            for j in i:
                if j == X:
                    count_turn_x += 1
                elif j == O:
                    count_turn_o += 1
    
        if count_turn_x > count_turn_o:
            return O
        else:
            return X                          


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # This will give the all the available spaces present for player.
    possible_action = set((i,j) for j in range(3) for i in range(3) if board[i][j]==None)

    return possible_action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Here we make deep copy of the board
    board_copy = deepcopy(board)

    # unpacking tuple
    i, j = action  

    # checking that box is already filled or not
    if board[i][j] != EMPTY:
        raise Exception("Box already filled")

    else:
        board_copy[i][j] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = None

    for i in range(len(board)):
        # Checking row and column are same or not
        if (board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != EMPTY):
            winner = board[i][0]
            return winner
        elif (board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != EMPTY):
            winner = board[0][i]
            return winner

    # Checking diagonal are same or not
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY) or (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != EMPTY):
        winner = board[1][1]
        return winner
    
    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_space = 0

    # Checking the winner ("X" or "O")
    if winner(board) == X or winner(board) == O:
        return True

    # Checking Empty space in a board. If there is no Empty space then, match is Tie  
    for row in board:
        for item in row:
            if item == EMPTY:
                empty_space += 1
    if empty_space == 0:
        return True
    
    # Match is in progress
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # Checking that game is end or not
    if terminal(board) == True:
        
        # if winner is X then return 1
        if winner(board) == X:
            return 1

        # if winner is O then return -1    
        elif winner(board) == O:
            return -1

        else:
            return 0    

def max_value(board):
    # Check winner
    if terminal(board):
        return utility(board)

    v = -100

    for action in actions(board):
        v = max(v, min_value(result(board, action))) 
    return v     


def min_value(board):
    # Check winner
    if terminal(board):
        return utility(board)

    v = 100    

    for action in actions(board):
        v = min(v, max_value(result(board, action))) 
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Check Winner
    if terminal(board) == True:
        return None

    # Give the optimal action
    else:
        # For X player
        if player(board) == X:
            v = -100
            for move in actions(board):
                i = min_value(result(board, move))  
                if i > v:
                    v = i
                    action = move
        else:
            # For O player
            v = 100
            for move in actions(board):
                i = max_value(result(board, move))
                if i < v:
                    v = i
                    action = move

    return action
    
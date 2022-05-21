"""
GameOFNim
"""

# from search import *
from asyncio.windows_events import NULL
from games import *
# from utils import *

class GameOfNim(Game):
    # YOUR CODE GOES HERE
    def __init__(self, board, screen, pygame, manager):
        """ Define goal state and initialize a problem """
        self.board = board
        self.screen = screen
        self.pygame = pygame
        self.manager = manager
        GameState = namedtuple('GameState', 'to_move, utility, board, moves')
        moves = []
        for index in range(0, len(board)):
            for numCards in range(1, board[index] + 1):
                if board[index] != 0:
                    moves.append((index, numCards))
        print('Starting Moves:', moves)
        self.initial = GameState(to_move='MAX', utility=0, board=board, moves=moves)



    def result(self, state, moves):
        nboard = state.board.copy()
        nboard[moves[0]] = (nboard[moves[0]] - moves[1])
        nmoves = []
        for index in range(0, len(nboard)):
            for numCards in range(1, nboard[index] + 1):
                if nboard[index] != 0:
                    nmoves.append((index, numCards))

        return GameState(to_move=('MIN' if state.to_move == 'MAX' else 'MAX'),
                         utility=self.utility(state, state.to_move),
                         board=nboard, moves=nmoves)

    def actions(self, state):  # return list of valid actions
        return state.moves

    def terminal_test(self,state):  # returns true if given state is end of game
        newboard = state.board.copy()
        #print(newboard)
        empty = True
        for index in range(0, len(newboard)):
            if newboard[index] != 0:
                empty = False
        return empty

    def eval(self,state):
        if (self.terminal_test(state) == True):
            return 1
        else:
            return 0

    def utility(self, state, player):
        if(self.terminal_test(state) == True):
            if (state.to_move=='MAX') :
               # print("max loses")
                #if max is playing terminal state, they lose
                return -1
            else:
                return 1
        else:
            return 0
     #def to_move(self, state):  # default implementation in game should be enough


if __name__ == "__main__":
    exit
    #nim = GameOfNim(board=[0, 5, 3, 1])  # Creating the game instance
    # nim = GameOfNim(board=[0,5,3,1])
    nim = GameOfNim(board=[5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    print(nim.initial.board) # must be [0, 5, 3, 1]
    print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2,1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1,3) ))
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")

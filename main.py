import chess
import chess.svg
import random
import time

# https://python-chess.readthedocs.io/en/latest/
# https://github.com/niklasf/web-boardimage
# https://www.freecodecamp.org/news/simple-chess-ai-step-by-step-1d55a9266977/

# returns a random move out of all possible moves
def randomMove():
    legalMoves = board.legal_moves
    legalMovesList = []
    for i in board.legal_moves:
        legalMovesList.append(i)

    randNum = random.randint(0, board.legal_moves.count()-1)

    #print("legal Moves")
    #print(legalMovesList)
    return legalMovesList[randNum]

# Initialize the board object
board = chess.Board()

counter = 1
# Main loop
while board.is_game_over() != True:
    print(counter)
    print(board.is_game_over())
    #print(chess.Move.from_uci('e2e4'))
    board.push_uci(str(randomMove()))
    board.push_uci(str(randomMove()))

    board.is_game_over

    print(board)
    time.sleep(0.5)
    counter += 1

'''
print(randomMove())
board.push_san(randomMove())
board.push_san(randomMove())
print(board)
'''
'''
print(board.legal_moves)

board.push_san("e4")
a = board.legal_moves
print()
board.push_san("e5")
print(board.legal_moves)
'''



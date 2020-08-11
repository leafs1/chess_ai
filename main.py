import chess
import chess.svg
import random
import time

# https://python-chess.readthedocs.io/en/latest/
# https://github.com/niklasf/web-boardimage
# https://www.freecodecamp.org/news/simple-chess-ai-step-by-step-1d55a9266977/



# Initialize the board object
board = chess.Board()

# Piece Values
pawnVal = 1
bishopVal = 3
knightVal = 3
rookVal = 5
queenVal = 9
kingVal = 90 

whitePoints = 0
blackPoints = 0


# returns a random move out of all possible moves
def randomMove():
    legalMoves = board.legal_moves
    legalMovesList = []
    for i in board.legal_moves:
        legalMovesList.append(i)

    randNum = random.randint(0, board.legal_moves.count()-1)

    print("legal Moves")
    print(legalMovesList)
    return str(legalMovesList[randNum])

# Takes in a SAN value (i.e.a1) and converts it into an int on the board (i.e. 1)
def SANtoInt(san):
    #print("san = " + str(san))
    letterNum = 0

    if san[0] == "b" or san[0] == "B":
        letterNum = 1
    elif san[0] == "c" or san[0] == "C":
        letterNum = 2
    elif san[0] == "d" or san[0] == "D":
        letterNum = 3
    elif san[0] == "e" or san[0] == "E":
        letterNum = 4
    elif san[0] == "f" or san[0] == "F":
        letterNum = 5
    elif san[0] == "g" or san[0] == "G":
        letterNum = 6
    elif san[0] == "h" or san[0] == "H":
        letterNum = 7
    else:
        pass

    return int(san[1]) * 8 - 8 + letterNum 
    

# Uses the basic chess point system to determin the optimal move
def pointEval():
    legalMoves = board.legal_moves
    optimalMove = ""
    highestPointDiff = 0

    for i in board.legal_moves:
        #print(i)
        if board.is_capture(i) == True:
            move = [str(i)[0:2], str(i)[2:4]]
            #print("special move = " + str(move[1]))
            piece = str(board.piece_at(SANtoInt(move[1])))

            if piece == "p" or piece == "P":
                if highestPointDiff < 1:
                    highestPointDiff = pawnVal
                    optimalMove = str(i)
            elif piece == "n" or piece == "N":
                if highestPointDiff < 3:
                    highestPointDiff = knightVal
                    optimalMove = str(i)
            elif piece == "b" or piece == "B":
                if highestPointDiff < 3:
                    highestPointDiff = bishopVal
                    optimalMove = str(i)
            elif piece == "r" or piece == "R":
                if highestPointDiff < 5:
                    highestPointDiff = rookVal
                    optimalMove = str(i)
            elif piece == "q" or piece == "Q":
                if highestPointDiff < 9:
                    highestPointDiff = queenVal
                    optimalMove = str(i)
            elif piece == "k" or piece == "K":
                if highestPointDiff < 90:
                    highestPointDiff = kingVal
                    optimalMove = str(i)
    
    if highestPointDiff == 0:
        return randomMove()
    else:
        return optimalMove
        



    



counter = 1
# Main loop
while board.is_game_over() != True:
    print(counter)
    print(pointEval())
    print(board.is_game_over())
    #print(board.piece_at(9))
    #print(chess.Move.from_uci('e2e4'))
    #board.push_uci(randomMove())
    board.push_uci(pointEval())
    print(board)

    move = str(input("move"))
    board.push_uci(move)


    print(board)
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



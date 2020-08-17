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
pawnVal = 10
bishopVal = 30
knightVal = 30
rookVal = 50
queenVal = 90
kingVal = 900

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
                if highestPointDiff < 10:
                    highestPointDiff = pawnVal
                    optimalMove = str(i)
            elif piece == "n" or piece == "N":
                if highestPointDiff < 30:
                    highestPointDiff = knightVal
                    optimalMove = str(i)
            elif piece == "b" or piece == "B":
                if highestPointDiff < 30:
                    highestPointDiff = bishopVal
                    optimalMove = str(i)
            elif piece == "r" or piece == "R":
                if highestPointDiff < 50:
                    highestPointDiff = rookVal
                    optimalMove = str(i)
            elif piece == "q" or piece == "Q":
                if highestPointDiff < 90:
                    highestPointDiff = queenVal
                    optimalMove = str(i)
            elif piece == "k" or piece == "K":
                if highestPointDiff < 900:
                    highestPointDiff = kingVal
                    optimalMove = str(i)
    
    if highestPointDiff == 0:
        return randomMove()
    else:
        return optimalMove
        

def minimaxRoot(depth, board, maximizingPlayer):
    possibleMoves = board.legal_moves
    bestMove = -9999
    bestMoveFinal = None
    for x in possibleMoves:
        move = chess.Move.from_uci(str(x))
        board.push(move)
        #print("new board")
        #print(board)
        value = max(bestMove, minimax(depth - 1, board, -10000, 10000, not maximizingPlayer))
        #print("after testing")
        board.pop()
        print(str(move) + " " + str(value))
        if (value > bestMove):
            print("Best score: " ,str(bestMove))
            print("Best move: ",str(bestMoveFinal))
            bestMove = value
            bestMoveFinal = move
    return bestMoveFinal

def minimax(depth, board, alpha, beta, maximizingPlayer):
    # https://en.wikipedia.org/wiki/Minimax
    # https://github.com/AnthonyASanchez/PythonChessAi

    
    #print("test board")
    #print(board)
   # print(depth)
    #print(maximizingPlayer)
    moves = board.legal_moves

    if depth == 0:
       # print("depth 00")
        return -evaluation(board, maximizingPlayer)

    #print("after depth")

    # If it's white's turn (white wants to maximize their score)
    if maximizingPlayer:    
        value = -9999
        for i in moves:     
            board.push(chess.Move.from_uci(str(i)))
            value = max(value, minimax(depth-1, board, alpha, beta, not maximizingPlayer))
            board.pop()
            alpha = max(alpha, value)
            if beta <= alpha:
                return value
        return value
    else:
        # Black's turn (black wants to minimize their score)
        value = 9999
        for i in moves:
            board.push(chess.Move.from_uci(str(i)))
            value = min(value, minimax(depth-1, board, alpha, beta, not maximizingPlayer))
            board.pop()
            beta = min(beta, value)
            if beta <= alpha:
                return value
        return value

def evaluation(board, maximizingPlayer):
    boardPos = 0
    evaluation = 0

    while boardPos < 64:
        evaluation += getPieceValue(str(board.piece_at(boardPos)))
        boardPos += 1
    
    #print("in evaluation")
    #print(evaluation)
    return evaluation


def getPieceValue(piece):
    if(piece == None):
        return 0
    value = 0
    if piece == "P" or piece == "p":
        value = 10
    if piece == "N" or piece == "n":
        value = 30
    if piece == "B" or piece == "b":
        value = 30
    if piece == "R" or piece == "r":
        value = 50
    if piece == "Q" or piece == "q":
        value = 90
    if piece == 'K' or piece == 'k':
        value = 900
    return value
    

    


counter = 1
n = 0

# Main loop
while board.is_game_over() != True:
   # print(counter)
    #print(pointEval())
    #print(board.is_game_over())
    #print(board.piece_at(9))
    #print(chess.Move.from_uci('e2e4'))
    #board.push_uci(randomMove())
    #board.push_uci(pointEval())
    #print(board)

    #move = str(input("move"))
    #board.push_uci(move)

    print(board)
    
    if n%2 == 0:
        move = input("Enter move: ")
        move = chess.Move.from_uci(str(move))
        board.push(move)
    else:
        print("Computers Turn:")
        move = minimaxRoot(5,board,True)
        print("move = " + str(move))
        move = chess.Move.from_uci(str(move))
        board.push(move)
    #print(board)
    #print("end")
    n += 1


    counter += 1


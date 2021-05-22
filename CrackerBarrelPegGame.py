# board:
#                   0
#                 1   2
#               3   4   5
#             6   7   8   9
#          10  11  12  13  14
import copy, sys


movecombos =    [ [ [1,2] , [3,5] ],
                  [ [3,4] , [6,8] ],
                  [ [4,5] , [7,9] ],
                  [ [6,7,4,1] , [10,12,5,0] ],
                  [ [7,8] , [11,13] ],
                  [ [2,4,8,9] , [0,3,12,14] ],
                  [ [3,7] , [1,8] ],
                  [ [4,8] , [2,9] ],
                  [ [7,4] , [6,1] ],
                  [ [8,5] , [7,2] ],
                  [ [6,11] , [3,12] ],
                  [ [7,12] , [4,13] ],
                  [ [11,7,8,13] , [10,3,5,14] ],
                  [ [12,8] , [11,4] ],
                  [ [13,9] , [12,5] ]]

class board:
    def __init__(self, pegs, solution):
        self.pegs = pegs
        self.solution = solution

    def moves(self): #returns list of possible moves
        retVal = []
        for i in range(15):
            if self.pegs[i] == 1:
                for j in range(len(movecombos[i][0])):
                    pegToJump = movecombos[i][0][j]
                    endLocation = movecombos[i][1][j]
                    if self.pegs[pegToJump] == 1 and self.pegs[endLocation] == 0:
                        retVal.append([i, pegToJump, endLocation])
        return retVal

    def movePegs(self, moveIndeces):
        self.solution.append(moveIndeces)
        self.pegs[moveIndeces[0]] = 0
        self.pegs[moveIndeces[1]] = 0
        self.pegs[moveIndeces[2]] = 1

    def __deepcopy__(self, memo):
        _copy = memo.get(id(self))
        if _copy is None:
            _copy = board(copy.deepcopy(self.pegs, memo), copy.deepcopy(self.solution, memo))
            memo[id(self)] = _copy
        return _copy


def printSolution(moves):
    print("Solution:")
    for i in range(13):
        print("\tpeg " + str(moves[i][0]) + " jumps peg " + str(moves[i][1]))
    print("\n   ** solution finder for the Cracker Barrel peg game **\n")

def findSol(b):
    numPegs = 0
    for i in range(15):
        numPegs += b.pegs[i]
    if numPegs == 1:            # base case
        printSolution(b.solution)
        sys.exit()
    else:
        possibleMoves = b.moves()
        for i in range(len(possibleMoves)):
            newBoard = copy.deepcopy(b)
            newBoard.movePegs(possibleMoves[i])
            findSol(newBoard)



print("\n   ** solution finder for the Cracker Barrel peg game **\n")
print("Board position indeces:")
print("                                 ")
print("                       0         ")
print("                     1   2       ")
print("                   3   4   5     ")
print("                 6   7   8   9   ")
print("               10  11  12  13  14")
print("                                 ")

startingEmpty = int(input("Enter starting empty hole: "))

startingPegs = []
for i in range(15):
    startingPegs.append(1)
startingPegs[startingEmpty] = 0

startingBoard = board(startingPegs, [])
findSol(startingBoard)

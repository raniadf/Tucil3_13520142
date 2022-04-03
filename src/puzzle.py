import heapq
import numpy as np
import time

# PUZZLE CLASS
class Puzzle :
    goalstate = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

    # 1. Puzzle Initialization
    def __init__(self):
        self.mtx = np.empty((4,4), int) # Create Empty Matrix
        self.cost = 0 # Cost of the puzzle
        self.zero = (0,0) # Position of the basis
        self.path = [] # Path of the puzzle
        self.up, self.down, self.left, self.right = None, None, None, None # Up, Down, Left, Right

    # 2. Cost Counter
    def countCost(self):
        count = 0
        for i in range (4) :
            for j in range (4) :
                # Count number of matrix that is not in position
                if (self.mtx[i][j] != Puzzle.goalstate[i][j]) :
                    count += 1
        
        return count

    # 3. Handle <
    def __lt__ (self,other) :
        return True

# IS FINISH BOOLEAN
def isFinish(puzzle):
    if (puzzle.countCost() == 0) :
        return True
    else :
        return False

# CHECK PUZZLE VALIDITY
def puzzleValid(puzzle) :
    # 1. Change 2d array -> list
    puzz = (np.reshape(puzzle.mtx, 16)).tolist()
    # 2. Check if 1-16 is in order
    for i in range (1,17) :
        if (SearchI(puzz, i) == -1) :
            return False
        
    return True

# READ PUZZLE FROM FILE
def readPuzzleFromFile(filename):
    # 1. Initialize Puzzle
    Puz15 = Puzzle()
    # 2. Open Puzzle File
    try :
        f = open(filename, "r")
        # 3. Read Puzzle
        try :
            for i in range(4):
                temp = f.readline()
                Puz15.mtx[i] = temp.split()
                for j in range(4):
                    Puz15.mtx[i][j] = int(Puz15.mtx[i][j])
                    if (Puz15.mtx[i][j] == 0 or Puz15.mtx[i][j] == 16) :
                        Puz15.mtx[i][j] = 16
                        Puz15.zero = (i,j)
            f.close()
            Puz15.cost = Puz15.countCost()

            # 4. Return Puzzle If Puzzle is Valid
            if (puzzleValid(Puz15)) :
                return Puz15
            else :
                print("  ║         Invalid input                                                    ║")
                return None
        except :
            print("  ║         Invalid input                                                    ║")
            return None
    except :
        print("  ║         File not found                                                   ║")
        return None

# READ PUZZLE FROM CONSOLE
def readPuzzleFromConsole():
    try :
        # 1. Initialize Puzzle
        Puz15 = Puzzle()
        # 2. Read Puzzle
        print("  ║         Input Puzzle (4x4), consists of :                                ║")
        print("  ║         a. Number 1 - 15                                                 ║")
        print("  ║         b. 0 or 16 as basis                                              ║")
        for i in range(4):
            print("                                >> ", end="")
            temp = str(input())
            Puz15.mtx[i] = temp.split()
            for j in range(4):
                Puz15.mtx[i][j] = int(Puz15.mtx[i][j])
                if (Puz15.mtx[i][j] == 0 or Puz15.mtx[i][j] == 16) :
                    Puz15.mtx[i][j] = 16
                    Puz15.zero = (i,j)
        
        Puz15.cost = Puz15.countCost()

        # 3. Return Puzzle If Puzzle is Valid
        if (puzzleValid(Puz15)) :
                return Puz15
        else :
            print("  ║         Invalid input                                                    ║")
            return None
    except :
        print("  ║         Invalid input                                                    ║")
        return None

# SEARCH INDEX OF NUM
def SearchI(puzz, num) :
    for i in range(len(puzz)) :
        if (puzz[i] == num) :
            return i

    return -1

# PRINT PUZZLE
def printPuzzle(puzz):
    print("                              ╔════╦════╦════╦════╗")
    for i in range(4):
        print("                              ", end = "")
        for j in range(4):
            print("║ ",end="")
            if (puzz[i][j] == 16) :
                print("   ", end = "")
                continue
            print("%02d " % puzz[i][j], end = "")
        print("║")
        if(i != 3):
            print("                              ╠════╬════╬════╬════╣")
    print("                              ╚════╩════╩════╩════╝")

# CONVERT PUZZLE TO LIST
def puzzleToList(Puzzle) :
    puzz = ""
    temp = (np.reshape(Puzzle, 16)).tolist()
    for i in range(16) :
        puzz += str(temp[i])

    return puzz

# FIND KURANG(I) + X (BASIS POSITION)
# TO CHECK IF PUZZLE IS REACHABLE
def Reachable(Puzzle) :
    # 1. Convert Puzzle to List
    puzz = (np.reshape(Puzzle.mtx, 16)).tolist()
    
    # 2. Find Kurang(i)
    count = 0
    print("                                ╔════╦═══════════╗     ")
    print("                                ║  i ║ kurang(i) ║     ")
    print("                                ╠════╬═══════════╣     ")
    for i in range (1,17) :
        temp = 0
        index = SearchI(puzz, i)
        for j in range (index, 16) :
            if (i > puzz[j]) :
                temp += 1
        count += temp
        print("                                ║ ", end = "")
        if (i < 10) :
            print(" %d" % i, end = "")
        else :
            print("%d" % i, end = "")
        print(" ║    ", end="")
        if (temp < 10) :
            print(" %d" % temp, end = "")
        else :
            print("%d" % temp, end = "")
        print("     ║")
    print("                                ╚════╩═══════════╝")
    
    # 3. Find basis position
    if ((Puzzle.zero[0] + Puzzle.zero[1]) % 2 != 0) :
        count += 1
    
    return count

# SOLVE PUZZLE
def solvePuzzle(PuzzPar) :
    # 1. Initialize Time
    now = time.time()
    # 2. Initialize Puzzle
    currPuzz = PuzzPar
    # 3. Initialize Checked Dictionary
    checked = {}
    puzz = puzzleToList(currPuzz.mtx)
    checked[puzz] = True
    # 4. Initialize HeapQueue
    pq = [] 
    # 5. Initialize node
    simpul = 0
    # 6. Loop until Puzzle = Goal State
    while (not (isFinish(currPuzz))) :
        # Check last path
        if (len(currPuzz.path) != 0) :
            path = currPuzz.path[len(currPuzz.path)-1]
        else :
            path = None

        # Check Up
        if (currPuzz.zero[0] != 0 and path != "DOWN") :
            currPuzz.up = Puzzle()
            currPuzz.up.mtx = np.copy(currPuzz.mtx)
            currPuzz.up.mtx[currPuzz.zero[0]][currPuzz.zero[1]] = currPuzz.up.mtx[currPuzz.zero[0]-1][currPuzz.zero[1]]
            currPuzz.up.mtx[currPuzz.zero[0]-1][currPuzz.zero[1]] = 16
            temp = puzzleToList(currPuzz.up.mtx)
            if (temp not in checked) :
                currPuzz.up.path = currPuzz.path + ["UP"]
                currPuzz.up.zero = [currPuzz.zero[0]-1, currPuzz.zero[1]]
                currPuzz.up.cost = currPuzz.up.countCost() + len(currPuzz.up.path)
                heapq.heappush(pq, (currPuzz.up.cost, currPuzz.up))
                simpul += 1
                if (isFinish(currPuzz.up)) :
                    currPuzz = currPuzz.up
                    break

        # Check Down
        if (currPuzz.zero[0] != 3 and path != "UP") :  
            currPuzz.down = Puzzle()
            currPuzz.down.mtx = np.copy(currPuzz.mtx)
            currPuzz.down.mtx[currPuzz.zero[0]][currPuzz.zero[1]] = currPuzz.down.mtx[currPuzz.zero[0]+1][currPuzz.zero[1]]
            currPuzz.down.mtx[currPuzz.zero[0]+1][currPuzz.zero[1]] = 16
            temp = puzzleToList(currPuzz.down.mtx)
            if (temp not in checked) :
                currPuzz.down.path = currPuzz.path + ["DOWN"]
                currPuzz.down.zero = [currPuzz.zero[0]+1, currPuzz.zero[1]]
                currPuzz.down.cost = currPuzz.down.countCost() + len(currPuzz.down.path)
                heapq.heappush(pq, (currPuzz.down.cost, currPuzz.down))
                simpul += 1
                if (isFinish(currPuzz.down)) :
                    currPuzz = currPuzz.down
                    break

        # Check Left
        if (currPuzz.zero[1] != 0 and path != "RIGHT") :
            currPuzz.left = Puzzle()
            currPuzz.left.mtx = np.copy(currPuzz.mtx)
            currPuzz.left.mtx[currPuzz.zero[0]][currPuzz.zero[1]] = currPuzz.left.mtx[currPuzz.zero[0]][currPuzz.zero[1]-1]
            currPuzz.left.mtx[currPuzz.zero[0]][currPuzz.zero[1]-1] = 16
            temp = puzzleToList(currPuzz.left.mtx)
            if (temp not in checked) :
                currPuzz.left.path = currPuzz.path + ["LEFT"]
                currPuzz.left.zero = [currPuzz.zero[0], currPuzz.zero[1]-1]
                currPuzz.left.cost = currPuzz.left.countCost() + len(currPuzz.left.path)
                heapq.heappush(pq, (currPuzz.left.cost, currPuzz.left))
                simpul += 1
                if (isFinish(currPuzz.left)) :
                    currPuzz = currPuzz.left
                    break

        # Check Right
        if (currPuzz.zero[1] != 3 and path != "LEFT") :
            currPuzz.right = Puzzle()
            currPuzz.right.mtx = np.copy(currPuzz.mtx)
            currPuzz.right.mtx[currPuzz.zero[0]][currPuzz.zero[1]] = currPuzz.right.mtx[currPuzz.zero[0]][currPuzz.zero[1]+1]
            currPuzz.right.mtx[currPuzz.zero[0]][currPuzz.zero[1]+1] = 16
            temp = puzzleToList(currPuzz.right.mtx)
            if (temp not in checked) :
                currPuzz.right.path = currPuzz.path + ["RIGHT"]
                currPuzz.right.zero = [currPuzz.zero[0], currPuzz.zero[1]+1]
                currPuzz.right.cost = currPuzz.right.countCost() + len(currPuzz.right.path)
                heapq.heappush(pq, (currPuzz.right.cost, currPuzz.right))
                simpul += 1
                if (isFinish(currPuzz.right)) :
                    currPuzz = currPuzz.right
                    break
        
        currPuzz = heapq.heappop(pq)[1]
        puzz = puzzleToList(currPuzz.mtx)
        checked[puzz] = True

    t = time.time() - now
    # 7. Print Solution Puzzle
    start = PuzzPar.mtx
    zero = PuzzPar.zero
    for i in range (len(currPuzz.path)) :
        # Change Position
        if (currPuzz.path[i] == "UP") :
            start[zero[0]][zero[1]] = start[zero[0]-1][zero[1]]
            start[zero[0]-1][zero[1]] = 16
            zero = (zero[0]-1, zero[1])
        elif (currPuzz.path[i] == "DOWN") :
            start[zero[0]][zero[1]] = start[zero[0]+1][zero[1]]
            start[zero[0]+1][zero[1]] = 16
            zero = (zero[0]+1, zero[1])
        elif (currPuzz.path[i] == "LEFT") :
            start[zero[0]][zero[1]] = start[zero[0]][zero[1]-1]
            start[zero[0]][zero[1]-1] = 16
            zero = (zero[0], zero[1]-1)
        elif (currPuzz.path[i] == "RIGHT") :
            start[zero[0]][zero[1]] = start[zero[0]][zero[1]+1]
            start[zero[0]][zero[1]+1] = 16
            zero = (zero[0], zero[1]+1)
        
        # Print Puzzle
        print("                                  STEP %d = %s" % (i+1, currPuzz.path[i]))
        printPuzzle(start)

    return currPuzz, t, simpul
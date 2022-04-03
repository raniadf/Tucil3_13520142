import puzzle

def Mainmenu(first) :
    if first == True :
        print("  ╔══════════════════════════════════════════════════════════════════════════╗")
    print("  ║         1. Input From EXTERNAL FILE (inside the test dir)                ║")
    print("  ║         2. Input From CONSOLE                                            ║")
    print("  ║         3. EXIT                                                          ║")
    print("  ║        =========================================================         ║")
    try :
        op = int(input("            Choose Menu : "))
        if (op == 1) :
            filename = input("            File Path : ")
            Puz15 = puzzle.readPuzzleFromFile(".\\test\\" + filename)
        elif (op == 2) :
            Puz15 = puzzle.readPuzzleFromConsole()
        elif (op == 3) :
            Puz15 = None
        print("  ╚══════════════════════════════════════════════════════════════════════════╝")
        return op, Puz15
    except : 
        print("  ║                   T R Y  A G A I N ! (invalid input)                     ║")
        print("  ║        =========================================================         ║")
        return Mainmenu(False)

print("                               W E L C O M E   T O                  ")                                                                         
print("      ░░███╗░░███████╗  ██████╗░██╗░░░██╗███████╗███████╗██╗░░░░░███████╗")
print("      ░████║░░██╔════╝  ██╔══██╗██║░░░██║╚════██║╚════██║██║░░░░░██╔════╝")
print("      ██╔██║░░██████╗░  ██████╔╝██║░░░██║░░███╔═╝░░███╔═╝██║░░░░░█████╗░░")
print("      ╚═╝██║░░╚════██╗  ██╔═══╝░██║░░░██║██╔══╝░░██╔══╝░░██║░░░░░██╔══╝░░")
print("      ███████╗██████╔╝  ██║░░░░░╚██████╔╝███████╗███████╗███████╗███████╗")
print("      ╚══════╝╚═════╝░  ╚═╝░░░░░░╚═════╝░╚══════╝╚══════╝╚══════╝╚══════╝")
print("           ╔════╦════╦════╦════╗             ╔════╦════╦════╦════╗")
print("           ║ XX ║ XX ║ XX ║ XX ║             ║ 01 ║ 02 ║ 03 ║ 04 ║")
print("           ╠════╬════╬════╬════╣             ╠════╬════╬════╬════╣")
print("           ║ XX ║ XX ║    ║ XX ║             ║ 05 ║ 06 ║ 07 ║ 08 ║")
print("           ╠════╬════╬════╬════╣      ➜      ╠════╬════╬════╬════╣")
print("           ║ XX ║ XX ║ XX ║ XX ║             ║ 09 ║ 10 ║ 11 ║ 12 ║")
print("           ╠════╬════╬════╬════╣             ╠════╬════╬════╬════╣")
print("           ║ XX ║ XX ║ XX ║ XX ║             ║ 13 ║ 14 ║ 15 ║    ║")
print("           ╚════╩════╩════╩════╝             ╚════╩════╩════╩════╝")

op, Puz15 = Mainmenu(True)

while (op!= 3) :
    if (Puz15 != None) :
        print()
        print("                                   P U Z Z L E")
        puzzle.printPuzzle(Puz15.mtx)
        count= puzzle.Reachable(Puz15)
        print("                                  Kurang(i) = %d" % count)
        if (count % 2 == 0) :
            print("\n                   ===========   S O L U T I O N  ===========")
            Result, time, simpul = puzzle.solvePuzzle(Puz15)
            print("                                Node Count = %d" % simpul)
            print("                                Time = %f s" % (time))
        else :
            print("                            Puzzle can not be solved !!")


    op, Puz15 = Mainmenu(True)

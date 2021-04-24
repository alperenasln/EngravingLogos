"""
Alperen ASLAN
"""
# Here is the simple board
import sys

board = [
    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],

]


#Initializing empty list

logoNamelist=[]
logoMoveList=[]
movements=[]
sameMovements1=[]
sameMovements2=[]
allvalues = []
allvalues2 = []
zipped = []
zipped2 = []
differences=[]
x_r1 = 0
x_r2 = 0
y_r1 = 0
y_r2 = 0
inFile = open(sys.argv[1], 'r')
while True:
    #Taking and splitting input

    inp = inFile.readline()
    parts = inp.split()
    if inp =='':
        break
    else:
        if parts[0] == "LOGO":
            # For logo command, inserting names and movements into list.
            if parts[1] in logoNamelist:
                print(parts[1] + " is in already list.")
            else:
                logoNamelist.append(parts[1])
                logoMoveList.append(parts[2])
                print(parts[1] + " defined")
        elif parts[0] == "ENGRAVE":
            # Coordinate managing because of dots in board.
            x_coor = int(parts[2]) * 2 - 1
            y_coor = int(parts[3]) * 2 - 1
            # Splitting the movement letters
            movements[:] = logoMoveList[logoNamelist.index(parts[1])]
            for k in movements:
                # Adding "-" or "|" to bread on coordinates
                if k == "U":
                    board[x_coor - 2][y_coor - 1] = "|"
                    x_coor = x_coor - 2
                elif k == "D":
                    board[x_coor][y_coor - 1] = "|"
                    x_coor = x_coor + 2
                elif k == "R":
                    board[x_coor - 1][y_coor] = "_"
                    y_coor = y_coor + 2
                elif k == "L":
                    board[x_coor - 1][y_coor - 2] = "_"
                    y_coor = y_coor - 2
            for x in board:
                print(*x, sep='')
        elif parts[0] == "SAME":
            # The basic idea for that, keeping ((x1,y1),((x2,y2)) coordinates to find same lines .
            # Adding movements into move list.
            sameMovements1[:] = logoMoveList[logoNamelist.index(parts[1])]
            sameMovements2[:] = logoMoveList[logoNamelist.index(parts[2])]
            for k in sameMovements1:
                if k == "U":
                    y_r2 = y_r2 + 1
                    p1 = [x_r1, y_r1]
                    p2 = [x_r2, y_r2]
                    # ziplist=zip(p1,p2)
                    zipped.append([p1, p2])
                    allvalues.extend(zipped)
                    zipped *= 0

                    x_r1 = x_r2
                    y_r1 = y_r2



                elif k == "D":
                    y_r2 = y_r1 - 1
                    p1 = [x_r1, y_r1]
                    p2 = [x_r2, y_r2]
                    # allvalues = list(zip(p1,p2))
                    zipped.append([p1, p2])
                    allvalues.extend(zipped)
                    zipped *= 0

                    x_r1 = x_r2
                    y_r1 = y_r2
                elif k == "R":
                    x_r2 = x_r2 + 1
                    p1 = [x_r1, y_r1]
                    p2 = [x_r2, y_r2]
                    zipped.append([p1, p2])
                    allvalues.extend(zipped)
                    zipped *= 0

                    x_r1 = x_r2
                    y_r1 = y_r2
                elif k == "L":
                    x_r2 = x_r2 - 1
                    p1 = [x_r1, y_r1]
                    p2 = [x_r2, y_r2]
                    zipped.append([p1, p2])
                    allvalues.extend(zipped)
                    zipped *= 0

                    x_r1 = x_r2
                    y_r1 = y_r2

            x_r1 = 0
            x_r2 = 0
            y_r1 = 0
            y_r2 = 0
            for k in sameMovements2:
                if k == "U":
                    y_r2 = y_r2 + 1
                    p1 = [x_r1, y_r1]
                    p2 = [x_r2, y_r2]
                    zipped2.append([p1, p2])
                    allvalues2.extend(zipped2)
                    zipped2 *= 0

                    x_r1 = x_r2
                    y_r1 = y_r2

                elif k == "D":
                    y_r2 = y_r1 - 1
                    p1 = [x_r1, y_r1]
                    p2 = [x_r2, y_r2]
                    zipped2.append([p1, p2])
                    allvalues2.extend(zipped2)
                    zipped2 *= 0

                    x_r1 = x_r2
                    y_r1 = y_r2
                elif k == "R":
                    x_r2 = x_r1 + 1
                    p1 = [x_r1, y_r1]
                    p2 = [x_r2, y_r2]
                    zipped2.append([p1, p2])
                    allvalues2.extend(zipped2)
                    zipped2 *= 0

                    x_r1 = x_r2
                    y_r1 = y_r2
                elif k == "L":
                    x_r2 = x_r1 - 1
                    p1 = [x_r1, y_r1]
                    p2 = [x_r2, y_r2]
                    zipped2.append([p1, p2])
                    allvalues2.extend(zipped2)
                    zipped2 *= 0

                    x_r1 = x_r2
                    y_r1 = y_r2
            #print(allvalues)
            #print(allvalues2)



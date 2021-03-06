#!/usr/bin/python3

'''
--- Day 11: Seating System ---

Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.

Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##

After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##

This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##

#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##

#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##

At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?
--- Part Two ---

As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. For example, the empty seat below would see eight occupied seats:

.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....

The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

.............
.L.L.#.#.#.#.
.............

The empty seat below would see no occupied seats:

.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.

Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##

#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#

#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#

Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?
'''

import os
import copy

DAY = "DAY 11"

def PrepareList(aList):
    # handle additional list preparation/manipulation
    # ex: numList = [int(item) for item in aList]
    return aList

def PrintAnswers(aPart1, aPart2):
    print (DAY)
    print ("  Part 1:  {}".format(aPart1))
    print ("  Part 2:  {}".format(aPart2))

def AdjacentOccupiedSeats(aMatrix, aRow, aCol):
    prevRow = aRow - 1
    nextRow = aRow + 1
    prevCol = aCol - 1
    nextCol = aCol + 1
    maxRow = len(aMatrix) - 1
    maxCol = len(aMatrix[aRow]) - 1

    seats = 0
    if (prevRow >= 0 and aMatrix[prevRow][aCol] == "#"):
        seats += 1
    if (prevRow >= 0 and nextCol <= maxCol and aMatrix[prevRow][nextCol] == "#"):
        seats += 1
    if (nextCol <= maxCol and aMatrix[aRow][nextCol] == "#"):
        seats += 1
    if (nextRow <= maxRow and nextCol <= maxCol and aMatrix[nextRow][nextCol] == "#"):
        seats += 1
    if (nextRow <= maxRow and aMatrix[nextRow][aCol] == "#"):
        seats += 1
    if (nextRow <= maxRow and prevCol >= 0 and aMatrix[nextRow][prevCol] == "#"):
        seats += 1
    if (prevCol >= 0 and aMatrix[aRow][prevCol] == "#"):
        seats += 1  
    if (prevRow >= 0 and prevCol >= 0 and aMatrix[prevRow][prevCol] == "#"):
        seats += 1
        
    return seats

def ExtendedAdjacentOccupiedSeats(aMatrix, aRow, aCol):
    maxRow = len(aMatrix) - 1
    maxCol = len(aMatrix[aRow]) - 1
    seats = 0
    multiplier = 1
    exitBool = False
    foundList = ['?'] * 8
    
    while not exitBool:
        prevRow = aRow - (1 * multiplier)
        nextRow = aRow + (1 * multiplier)
        prevCol = aCol - (1 * multiplier)
        nextCol = aCol + (1 * multiplier)
        if (prevRow >= 0 and aMatrix[prevRow][aCol] != '.' and foundList[0] == '?'):
            foundList[0] = aMatrix[prevRow][aCol]
        if (prevRow >= 0 and nextCol <= maxCol and aMatrix[prevRow][nextCol] != '.' and foundList[1] == '?'):
            foundList[1] = aMatrix[prevRow][nextCol]
        if (nextCol <= maxCol and aMatrix[aRow][nextCol] != '.' and foundList[2] == '?'):
            foundList[2] = aMatrix[aRow][nextCol]
        if (nextRow <= maxRow and nextCol <= maxCol and aMatrix[nextRow][nextCol] != '.' and foundList[3] == '?'):
            foundList[3] = aMatrix[nextRow][nextCol]
        if (nextRow <= maxRow and aMatrix[nextRow][aCol] != '.' and foundList[4] == '?'):
            foundList[4] = aMatrix[nextRow][aCol]
        if (nextRow <= maxRow and prevCol >= 0 and aMatrix[nextRow][prevCol] != '.' and foundList[5] == '?'):
            foundList[5] = aMatrix[nextRow][prevCol]
        if (prevCol >= 0 and aMatrix[aRow][prevCol] != '.' and foundList[6] == '?'):
            foundList[6] = aMatrix[aRow][prevCol]
        if (prevRow >= 0 and prevCol >= 0 and aMatrix[prevRow][prevCol] != '.' and foundList[7] == '?'):
            foundList[7] = aMatrix[prevRow][prevCol]
        multiplier += 1

        if multiplier >= max(maxRow, maxCol) or '?' not in foundList:
            exitBool = True
            
    seats = foundList.count('#')
    return seats

def Answer(aList):
    part1 = "?"
    part2 = "?"

    # DO IT
    # part 1
    seatingMatrix = []
    for line in aList:
        row = [char for char in line]
        seatingMatrix.append(row)

    changes = 1
    while changes > 0:
        changes = 0
        newSeatingMatrix = copy.deepcopy(seatingMatrix)
        row = 0
        while row < len(seatingMatrix):
            col = 0
            while col < len(seatingMatrix[row]):
                if seatingMatrix[row][col] == "L" and AdjacentOccupiedSeats(seatingMatrix, row, col) == 0:
                    newSeatingMatrix[row][col] = "#"
                    changes += 1
                elif seatingMatrix[row][col] == "#" and AdjacentOccupiedSeats(seatingMatrix, row, col) >= 4:
                    newSeatingMatrix[row][col] = "L"
                    changes += 1
                col += 1
            row += 1
        seatingMatrix = copy.deepcopy(newSeatingMatrix)
    part1 = sum(row.count('#') for row in seatingMatrix)

    # part 2
    seatingMatrix = []
    for line in aList:
        row = [char for char in line]
        seatingMatrix.append(row)

    changes = 1
    while changes > 0:
        changes = 0
        newSeatingMatrix = copy.deepcopy(seatingMatrix)
        row = 0
        while row < len(seatingMatrix):
            col = 0
            while col < len(seatingMatrix[row]):
                if seatingMatrix[row][col] == "L" and ExtendedAdjacentOccupiedSeats(seatingMatrix, row, col) == 0:
                    newSeatingMatrix[row][col] = "#"
                    changes += 1
                elif seatingMatrix[row][col] == "#" and ExtendedAdjacentOccupiedSeats(seatingMatrix, row, col) >= 5:
                    newSeatingMatrix[row][col] = "L"
                    changes += 1
                col += 1
            row += 1
        seatingMatrix = copy.deepcopy(newSeatingMatrix)
    part2 = sum(row.count('#') for row in seatingMatrix)
    #

    PrintAnswers(part1, part2)
    
def Main():
    inputFileName = __file__.replace(".py", ".input")
    if not os.path.isfile(inputFileName):
        print ("Input file ({}) does not exist.".format(inputFileName))
        return
    with open(inputFileName, 'r') as fh:
        lines = [line.strip() for line in fh]
    
    # Prepare line list (as necessary)
    modList = PrepareList(lines)
    # Part 1/2 function call(s)
    Answer(modList)

# if run stand-alone
if __name__ == '__main__':
    Main()

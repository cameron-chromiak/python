#cameron
#28 November
#tic tac toe?



def showGameBoard(gb): #gb refrences grid
    for row in gb: #iterate thru rows
        for value in row: #go thru colums
            print(value, " | ", end='') 
        print()
        print("-" * 15)

def getInput(gb):
    while True:
        try:
            userRow = int(input("Enter row 1, 2, or 3: "))-1 #to prevent off by 1 error
            userCol = int(input("Enter column 1, 2, or 3: "))-1
            # NEED to edit bc row and col will show error if just one is invalid bc they are dependent on eachother
            if userRow in range(0,3):
                if userCol in range(0,3):
                    if gb[userRow][userCol] == " ": #
                        break
                    else:
                        print("That square is already taken")

                else:
                    print("Illegal row or colum")

        except ValueError:
            print("Please use numeric entries")
    return userRow, userCol


def main():
    turn = "X" 
    grid = [[" "," "," ",],
            [" "," "," ",],
            [" "," "," ",]
            ]

    while True:
        showGameBoard(grid)
        print(turn,"'s turn")
        userRow, userCol = getInput(grid)
        grid[userRow][userCol] = turn
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
            
    

main()

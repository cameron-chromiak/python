#Cameron Chromiak
#25 November
#change x's to o's in a table. If you input 5 that will produce an error
#but any other number it will work...

def changeData(table, newRow, newCol):
        try:
            if newRow in range(5): #test if row/colum exist
                if newCol in range(5):
                    if table[newRow][newCol] == "X":
                        table[newRow][newCol] = "O"
                        print("**********")
                    else:
                        print("how did you get here? Please leave")#error msg

                else:
                    print("Column must be between 1 and 4")
            else:       #inputs are not valid msg
                print("Row must be between 1 and 4")
            printData(table)
        except ValueError:
            print("Please use a valid number")

def printData(table):
    for row in table: #iterate thru rows
        for i in row: #go thru colums
            print(i,  " ", end='') 
        print()
        print()


def main():
    end = False
    while not end:
        newRow = int(input("What row do you want to change?"))-1 # prevents off by one error
        newCol = int(input ("What colum do you want to change? "))-1

        table = [ ["X", "X", "X", "X"],
                  ["X", "X", "X", "X"],
                  ["X", "X", "X", "X"],
                  ["X", "X", "X", "X"],
                  ]
        
        printData(table)
        changeData(table, newRow, newCol)


main()

#Cameron Chromiak
#21 November
#2d arrays for rain data
'''
def smooth(rainfall):
    for i in range(len(rainfall)):
        rainfall[0] = rainfall[0][0]+ rainfall[0][1]+rainfall[0][2]/len(rainfall[0])
        print(rainfall,'**')'''
        
def showData(rainfall):
    for i in range(0,len(rainfall)): #go thru all rows
        print("Week" + str(i+1) + ":\t" ,end="")
        for j in range(0,len(rainfall[i])):
            print("%.1f"%rainfall[i][j],"\t",end="")
        print()

def sumWeeklyData(rainfall):
    print("Weekly Totals")
    count = 1 #what row we are on
    for i in rainfall:
        total = sum(i)
        print("Week",count, ":   ","%.1f"%total)

def main():
    rainfall = [ [.5, 0, .1],
                    [0, 0, 1],
                    [0, 0, 0],
                [.5,.6,1]
                   ]
    
    showData(rainfall)
    print()
    sumWeeklyData(rainfall)
    #change(2,2,5,rainfall)
    #smooth(rainfall)
main()

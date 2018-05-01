#Cameron Chromiak
#11/14
#create a list of score, calc average, average w lowest dropped show all gredes 70 or higher


#insert scorews into list, set MAX. make sure input is int type and in 0-100 range
def inputScores(scores):
    MAX = 5
    for count in range(1,MAX): 
        user = int(input("Enter score " +str(count)+":"))
        while user not in range(0, 101):
            user = int(input("Error, Enter score " + str(count) + ": "))
        scores.append(user)

#will show high scores defined in parameter in main()
def showHighScores(scores, HIGH):
    print("Scores greater than " + str(HIGH) + " are the top scores")
    for number in scores:
        if number >= HIGH:
            print(number, "   ",end="")
    print()
    
#print statements      
def showScores(scores):
    print("Your scores: ",end="")
    for number in scores:
        print(number, "  ", end="")
    print()
    print()

#finds average. it is scaleable and takes list elements/length of list
def calAvg(scores):
    total = sum(scores)
    avg = total/len(scores)
    return avg

#create dummy list to manipulate data
def calcAvgWithDrop(scores):
    dummyList = list(scores)
    dummyList.sort() #sorts list low to high
    print(dummyList)
    dummyList.pop(0)#removes first element after sortaion
    return sum(dummyList)/len(dummyList)
              
def main():
    scores = []
    inputScores(scores)
    showScores(scores)
    avg = calAvg(scores)
    print("Average: %.1f" % avg)
    showHighScores(scores, 80)
    avgDrop = calcAvgWithDrop(scores)
    print("Average with drop ",avgDrop)

main()

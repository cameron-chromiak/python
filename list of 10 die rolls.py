#Cameron Chromiak
#11-15-17
#fill list with dice rolls, display 10 roll, number of 6's, the sum and first and last

from random import randint

def getSix(rolls):
    copy = list(rolls)
    copy.sort() #create a dummy list then print it for testing purposes
    print("Sorted: ",copy)
    count = copy.count(6) #there is a count method that counts occourece of 
    print("Six's: ", count)#something

def firstAndLast(rolls):
    print("First value: ",rolls[0])#select 0 value, then -1 will always be last value so its 
    print("Last value: ",rolls[-1])#scaleable
          
def getSum(rolls): #sum of elements in the list 
    print('Sum',sum(rolls))
    
    
def printAll(rolls): #i planned on having all print statements going here
    print(rolls)
    

def rollDie(rolls): #generate 10 rolls, insert them into the list
    i= 0
    while i < 10: #roll 10 die 10 times
        ranNum = randint(0,6)
        rolls.append(ranNum)
        i+= 1  

    printAll(rolls)
        
    
def main():
    rolls = [] #create list, call functions

    rollDie(rolls)
    getSum(rolls)
    getSix(rolls)
    firstAndLast(rolls)
main()

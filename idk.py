
from sys import argv

def readSayings(sayings, meanings):
    try:
        filename = argv[1] #first argument is in second element
        try:
            fileptr = open(filename,"r")
            line = fileptr.readline() #open file and read
            while line != "":
                lines.append(line)
                line = fileptr.readline()
            fileptr.close()
        except IOError:
            print("Error opening",filename)
    except :#handles most errors
        print("Name of file missing from command line")
        

def showLines(lines):
    for index in range(0,len(sayings)):
        print(lines[index])
        

def main():
    lines = []

    readSayings(lines)
    showLines(sayings, meanings)
main()

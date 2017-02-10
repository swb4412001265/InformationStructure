import os
import csv

def writeIntofile(filePath, inPut):
    with open(filePath,"w") as writeFile:   #open file as writable
        inPut_length = len(inPut)
        for index in range(inPut_length):
            writeFile.write("{},{}\n".format(inPut[index],index+1))   #write number with line number to right
    writeFile.close()
    return writeFile

currDir = os.getcwd()
print(currDir)
filePath = os.path.join(currDir,"user.csv")     #create file's path
print(os.path.exists(filePath))
print(os.path.isfile(filePath))
print(filePath)

writeIntofile(filePath,range(11))

def readIntoFile(filePath):
    tup_list = []
    with open(filePath,'r') as readFile:
        #readContent = csv.reader(readFile)
        #contentList = contentList.append(int(readContent))
        #print(type(readContent))
        #contentList = list(readContent)
        #contentList = contentList[0]
        for line in readFile:
            #print(type(line))
            #print(line)
            line = list(map(int, line.split(",")))      #convert string into int and store in a list
            tup_list.append(line[0])    #only put the numbers into list
            #line = int(line)
            #print(type(line))
    readFile.close()
    return tup_list

readIntoFile(filePath)

def printIntoFile(inputList):
    for item in inputList:
        print(item)

printIntoFile(readIntoFile(filePath))

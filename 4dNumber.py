import random
import collections

'''
def generateNum():
    digit=str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
    return digit
'''

numberList=[]
brokenUp=[]
sortedNum=[]

'''
#Generate random numbers
for i in range (10000):
    numberList.append(generateNum())
'''

#Get data from csv file
# *File to be placed in same location as script*
# *DO NOT EDIT CSV FILE*
dataFile=open("Results.csv","r")
for data4d in dataFile:
    data4d=data4d.strip()
    dataList=data4d.split(",")
    intData=dataList[3]
    #removes "Digit" found on 1st line of csv
    if intData!="Digit":
        numberList.append(intData)

#break up into list
for digit4 in numberList:
    digit4=digit4.split()
    for singleNum in digit4:
        singleNum=list(singleNum)
        brokenUp.append(singleNum)

#Sort numbers in ascending order
for i in brokenUp:
    i.sort()
    i="".join(i)
    sortedNum.append(i)
#Compare how namy times it appears
numDict=collections.Counter(sortedNum)

print("Top Occurance:" + str(numDict))

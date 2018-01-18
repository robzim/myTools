#import csv
import openpyxl
myDebugFlag = True
def myPrint(theParams):
    if myDebugFlag == True:
        print(theParams)

def myGetSheetData(theFilePath):
    myFilePath = theFilePath
    myWorkbook = openpyxl.load_workbook(myFilePath)
    mySheet = myWorkbook.active
    mySheetData = []
    for myCol in ['A','B']:
        for i in range(1,15):
            myIndex = myCol + str(i)
            if mySheet[myIndex].value:
                mySheetItem = myCol + str(i) + ' ' +   str(mySheet[myIndex].value)
                print(mySheetItem)
                mySheetData.append(mySheetItem)
    return mySheetData




print('getting sheet data')
print(myGetSheetData('myTestInfo.xlsx'))

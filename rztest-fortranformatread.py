import fortranformat as ff
import vpython as vp

from tkinter import filedialog
from tkinter import *
x = [] ; y = [] ; z = [] ; myLabels = []
xNorm = [] ; yNorm = [] ; zNorm = []
def myNormalize():
	myMaxVal=0
	for i in x:
		if i > myMaxVal:
			myMaxVal = i
	for i in y:
		if i > myMaxVal:
			myMaxVal = i
	for i in z:
		if i > myMaxVal:
			myMaxVal = i
	print(myMaxVal)
	myMultiplier = 100.0 / myMaxVal
	print("Multiply by " + str(myMultiplier))
	for i in x:
		xNorm.append(i*myMultiplier)
	for i in y:
		yNorm.append(i*myMultiplier)
	for i in z:
		zNorm.append(i*myMultiplier)
myRoot = Tk()
myFileName = filedialog.askopenfilename(initialdir='~/',filetypes=(("text files","*.txt"),("all files","*.*")))
myFile = open(myFileName,'r')
myText = myFile.readlines()
print("Line Count = ",len(myText))
myRoot.destroy()
myStartChar = 11
myFortranFormat = myText[0][:9]
print(myFortranFormat)
myConceptCount = int(myText[0][myStartChar:myStartChar+3])
print("concepts=",myConceptCount)
myDimensionString = myText[0][myStartChar+6:myStartChar+9]
print("dimension string is"+myDimensionString)
if myDimensionString.isnumeric():
	myDimensionCount = int(myText[0][myStartChar+6:myStartChar+9])
else:
	myStartChar = 10
	myConceptCount = int(myText[0][myStartChar:myStartChar + 3])
	print("concepts=", myConceptCount)
	myDimensionCount = int(myText[0][myStartChar+6:myStartChar+9])
print("dimensions=",myDimensionCount)
myFirstSplit = myFortranFormat.split('(')
print(myFirstSplit)
myConceptsPerLine = int(myFirstSplit[1].split('F')[0])
myLinesToSkip = int(myDimensionCount / myConceptsPerLine) + 1
myFortranData = ff.FortranRecordReader(myFortranFormat)
myLine = 1
myConceptLoopCounter = 1
while myConceptLoopCounter <= myConceptCount:
	myTempXYZ = myFortranData.read(myText[myLine])
	x.append(myTempXYZ[0])
	y.append(myTempXYZ[1])
	z.append(myTempXYZ[2])
	myLine += myLinesToSkip
	myConceptLoopCounter += 1
myConceptLoopCounter = 1
while myConceptLoopCounter <= myConceptCount:
	myLabel = myText[myLine].strip()
	myLabels.append(myLabel)
	myLine += 1
	myConceptLoopCounter += 1
print("myConceptCount is ",myConceptCount)
print("Labels are ",myLabels)
myNormalize()
a = vp.canvas(title='Simple Galileo Viewer by Rob Zimmelman c. 2018 All Rights Reserved',width=1400, height=700, background=vp.color.black)
myBox = vp.box(length=200,width=200,height=0.01,opacity=0.5)
for i in range(0, myConceptCount):
	print(i, x[i], y[i], z[i])
	a = vp.sphere(pos=vp.vector(xNorm[i], yNorm[i], zNorm[i]),color=vp.color.red,radius=1.0)
	b = vp.label(text=myLabels[i],pos=vp.vector(xNorm[i], yNorm[i], zNorm[i]),color=vp.color.yellow,box=True,line=True,xoffset=75,yoffset=15,radius=12.0)
	c = vp.arrow(pos=vp.vector(xNorm[i], 0 , zNorm[i]),color=vp.color.blue,shaftwidth=0.25,axis=vp.vector(0,yNorm[i],0))

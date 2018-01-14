import fortranformat as ff
import vpython as vp
x = [] ; y = [] ; z = [] ; myLabels = []
myFile = open('fake data.txt','r')
myText = myFile.readlines()
myFirstLineList = myText[0].split(" ",1)
myFortranFormat = myFirstLineList[0]
myTempString = myFirstLineList[1]
myConceptCount = int(myTempString[2:4])
myDimensionCount = int(myTempString[8:10])
myFirstSplit = myFortranFormat.split('(')
myConceptsPerLine = int(myFirstSplit[1].split('F')[0])
myLinesToSkip = (myDimensionCount % myConceptsPerLine) + 2
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
a = vp.canvas(title='Simple Galileo Viewer by Rob Zimmelman c. 2018 All Rights Reserved',width=1400, height=700, background=vp.color.black)
myBox = vp.box(length=200,width=200,height=0.01,opacity=0.5)
for i in range(1, myConceptCount):
	print(i, x[i], y[i], z[i])
	a = vp.sphere(pos=vp.vector(x[i], y[i], z[i]),color=vp.color.red,radius=1.0)
	b = vp.label(text=myLabels[i],pos=vp.vector(x[i], y[i], z[i]),color=vp.color.yellow,box=True,line=True,xoffset=75,yoffset=15,radius=12.0)
	c = vp.arrow(pos=vp.vector(x[i], 0 , z[i]),color=vp.color.blue,shaftwidth=0.25,axis=vp.vector(0,y[i],0))


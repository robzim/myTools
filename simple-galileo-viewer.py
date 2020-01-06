from typing import List, Any

import fortranformat as ff
import vpython as vp

X = []
Y = []
Z = []
My_labels = []
myFile = open('fake data.txt', 'r')
myText = myFile.readlines()
myFirstLineList = myText[0].split(" ", 1)
myFortranFormat = myFirstLineList[0]
myTempString = myFirstLineList[1]
myConceptCount = int(myTempString[2:4])
myDimensionCount = int(myTempString[8:10])
my_first_split = myFortranFormat.split('(')
myConceptsPerLine = int(my_first_split[1].split('F')[0])
myLinesToSkip = (myDimensionCount % myConceptsPerLine) + 2
myFortranData = ff.FortranRecordReader(myFortranFormat)
my_line = 1
myConceptLoopCounter = 1
while myConceptLoopCounter <= myConceptCount:
    myTempXYZ = myFortranData.read(myText[my_line])
    X.append(myTempXYZ[0])
    Y.append(myTempXYZ[1])
    Z.append(myTempXYZ[2])
    my_line += myLinesToSkip
    myConceptLoopCounter += 1
myConceptLoopCounter = 1
while myConceptLoopCounter <= myConceptCount:
    This_label = myText[my_line].strip()
    My_labels.append(This_label)
    my_line += 1
    myConceptLoopCounter += 1
print("myConceptCount is ", myConceptCount)
print("Labels are ", My_labels)
my_sphere = vp.canvas(title='Simple Galileo Viewer by Rob Zimmelman c. 2018 All Rights Reserved',
					  width=1400, height=700, background=vp.color.black)

myBox = vp.box(length=200, width=200, height=0.01, opacity=0.5)
for i in range(1, myConceptCount):
    print(i, X[i], Y[i], Z[i])
    my_sphere = vp.sphere(pos=vp.vector(X[i], Y[i], Z[i]), color=vp.color.red, radius=1.0)
    my_label = vp.label(text=My_labels[i], pos=vp.vector(X[i], Y[i], Z[i]), color=vp.color.yellow, box=True, \
						line=True, xoffset=75, yoffset=15, radius=12.0)
    my_arrow = vp.arrow(pos=vp.vector(X[i], 0, Z[i]), color=vp.color.blue, shaftwidth=0.25, axis=vp.vector(0, Y[i], 0))
    print(f'a={my_sphere}, b={my_label}, c={my_arrow}')

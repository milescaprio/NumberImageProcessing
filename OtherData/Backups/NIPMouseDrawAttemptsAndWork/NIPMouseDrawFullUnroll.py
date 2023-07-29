import math
import sys
from benchmarks import *
import turtle
import time
import threading
returnable = 0;
clickx = 0;
clicky = 0;
wbImage = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]];

pixelInputImage = [
[0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]];



inputPixelsX = [];
inputPixelsY = [];

IMAGESIZE = 16; #16*16 image processing
imagesToCheck = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]];
scores = [];
bsScores = []; #bs is benchmark side!!!

#whiteboard functions
def drawSquare(thex,they):
    global clickx
    global clicky
    global image
    clickx = thex
    clicky = they
    pixelX = round(clickx//16)
    pixelY = round(clicky//16)
    if pixelY < 0 or pixelY > 15 or pixelX < 0 or pixelX > 15:
        return
    currentPixel = wbImage[15 - pixelY][pixelX];
    wbImage[15 - pixelY][pixelX] = 1 - currentPixel;
    lT = turtle.Turtle();
    lT.hideturtle();
    lT.color("red");
    lT.fillcolor("red");
    if currentPixel == 1:
        lT.color("white");
        lT.fillcolor("white");
    print(clickx, clicky)
    lT.speed(100000);
    lT.penup();
    lT.goto((clickx//16)*16, (clicky//16)*16)
    lT.pendown()
    lT.begin_fill()
    lT.seth(90)
    lT.fd(15);
    lT.right(90);
    lT.fd(15);
    lT.right(90);
    lT.fd(15);
    lT.right(90);
    lT.fd(15);
    lT.right(90);
    lT.end_fill();
    lT.penup()
def exitTurtle(dummy = None, dummy2 = None):
    turtle.bye();
    returnable = 1;
def wbStart():
    global wn
    global screen
    wn = turtle.Screen()
    screen = wn.getcanvas()
    turtle.tracer(10,0);
    lT = turtle.Turtle()
    lT.hideturtle();
    wn.bgcolor("black");
    lT.color("white");
    lT.speed(100000);
    turtle.screensize(256,256);
    lT.fillcolor("white");
    lT.goto(0,0);
    lT.pendown();
    lT.begin_fill();
    lT.goto(0,0);
    lT.goto(255,0);
    lT.goto(255,255);
    lT.goto(0,255);
    lT.goto(0,0);
    lT.end_fill();
    lT.penup();
    wn.onclick(drawSquare);
    wn.onkey(exitTurtle,"space");
    wn.listen();
#choose variable based on inputs
def varName(number, variant, variableID):
    varItems = [[["pixelZeroA","zeroAPixelsX","zeroAPixelsY"],["pixelZeroB","zeroBPixelsX","zeroBPixelsY"]],
                [["pixelOneA","oneAPixelsX","oneAPixelsY"],["pixelOneB","oneBPixelsX","oneBPixelsY"]],
                [["pixelTwoA","twoAPixelsX","twoAPixelsY"],["pixelTwoB","twoBPixelsX","twoBPixelsY"]],
                [["pixelThreeA","threeAPixelsX","threeAPixelsY"],["pixelThreeB","threeBPixelsX","threeBPixelsY"]],
                [["pixelFourA","fourAPixelsX","fourAPixelsY"],["pixelFourB","fourBPixelsX","fourBPixelsY"]],
                [["pixelFiveA","fiveAPixelsX","fiveAPixelsY"],["pixelFiveB","fiveBPixelsX","fiveBPixelsY"]],
                [["pixelSixA","sixAPixelsX","sixAPixelsY"],["pixelSixB","sixBPixelsX","sixBPixelsY"]],
                [["pixelSevenA","sevenAPixelsX","sevenAPixelsY"],["pixelSevenB","sevenBPixelsX","sevenBPixelsY"]],
                [["pixelEightA","eightAPixelsX","eightAPixelsY"],["pixelEightB","eightBPixelsX","eightBPixelsY"]],
                [["pixelNineA","nineAPixelsX","nineAPixelsY"],["pixelNineB","nineBPixelsX","nineBPixelsY"]]];
    return(varItems[number][variant][variableID]);

#"slice" all the numbers
def mySlice():
    for i in range(0,10):
        print("\nNumber:",i,"\n")
        inputPixelsX.clear();
        inputPixelsY.clear();
        forLoopY = 0;
        while forLoopY < IMAGESIZE: #forLoop because of preference over python FOR
            forLoopX = 0;
            while forLoopX < IMAGESIZE:
                if eval((varName(i,0,0)+"[forLoopY][forLoopX] == 1")):
                    inputPixelsX.append(forLoopX);
                    inputPixelsY.append(forLoopY);
                    print("Found Pixel at ", forLoopX, forLoopY);
                forLoopX += 1;
            forLoopY += 1;
        print(inputPixelsX,"and",inputPixelsY);

def argSlice(pixelImage, localIMAGESIZE = IMAGESIZE):
    #algorithm one: need to change input image to pixel map in a list: inputPixelsX and inputPixelsY
    imagePixelsX = [];
    imagePixelsY = [];
    forLoopY = 0;
    while forLoopY < localIMAGESIZE: #forLoop because of preference over python FOR
        forLoopX = 0;
        while forLoopX < localIMAGESIZE:
            if pixelImage[forLoopY][forLoopX] == 1:
                imagePixelsX.append(forLoopX);
                imagePixelsY.append(forLoopY);
                print("Found Pixel at ", forLoopX, forLoopY);
            forLoopX += 1;
        forLoopY += 1;
    print(imagePixelsX,"and",imagePixelsY);
    return([imagePixelsX,imagePixelsY]);
    #that was easy

#Shifter Algorithm
def findMeanCenter(imagePixelsX, imagePixelsY, localIMAGESIZE = IMAGESIZE):
    xCenter = sum(imagePixelsX)/len(imagePixelsX);
    yCenter = sum(imagePixelsY)/len(imagePixelsY);
    xOffset = xCenter-7.5;
    yOffset = yCenter-7.5;
    return([xOffset, yOffset]);


#/--------------------------------MAIN--------------------------------\#
run = eval(input("What would you like to do? 1. Start 2. Slice (debug-only)"));
#CHANGE THIS EVAL TO INT BEFORE PUBLISHING! USER CAN RUN COMMANDS

if run == 2:
    mySlice();
    sys.exit();

userInputMethod = int(input("How would you like to select an image? 1.Draw 2.Use internal 3.Paste image array"));
if userInputMethod == 3:
    pixelInputImage = eval(input("Paste array here"));
if userInputMethod == 2:
    pass;
if userInputMethod == 1:
    global wn
    global screen
    wn = turtle.Screen()
    screen = wn.getcanvas()
    turtle.tracer(10,0);
    lT = turtle.Turtle()
    lT.hideturtle();
    wn.bgcolor("black");
    lT.color("white");
    lT.speed(100000);
    turtle.screensize(256,256);
    lT.fillcolor("white");
    lT.goto(0,0);
    lT.pendown();
    lT.begin_fill();
    lT.goto(0,0);
    lT.goto(255,0);
    lT.goto(255,255);
    lT.goto(0,255);
    lT.goto(0,0);
    lT.end_fill();
    lT.penup();
    wn.onclick(drawSquare);
    wn.onkey(exitTurtle,"space");
    wn.listen();
    input("ENTER TO CONTINUE")
    pixelInputImage = wbImage;
    print(pixelInputImage);  
advanced = int(input("Debug info level (Takes more execution time with more info) 1/2/3"));

temp = argSlice(pixelInputImage); #slice input image with argSlice()
inputPixelsX = temp[0];
inputPixelsY = temp[1];

#algorithm two: here we go
bestImage = [255, 255]; #255 is fallback if no image becomes better, in other words, if no images are checked or if there is an error
bestImageScore = 255;
inputOffset = findMeanCenter(inputPixelsX, inputPixelsY);
inputOffset = [round(item,3) for item in inputOffset];
for imageID in imagesToCheck: #imageID is [number,variant]
    imageOffset = eval("findMeanCenter("+varName(imageID[0], imageID[1], 1)+","+varName(imageID[0], imageID[1], 2)+")");
    imageOffset = [round(item,3) for item in imageOffset];
    totalScore = 0; #Score before made into average, take the closest pixel to each input pixel and measure the distance and sum them up
    for inputPixelIndex in range(0, len(inputPixelsX)):
        bestDistance = 255; #same fallback, and by the way 255 has no specific meaning in this context
        for imagePixelIndex in range(0, len(eval(varName(imageID[0], imageID[1], 1)))): 
            distance = math.hypot( ( ((inputPixelsX[inputPixelIndex]) - inputOffset[0]) - ((eval(varName(imageID[0], imageID[1], 1)+"[imagePixelIndex]")) - imageOffset[0]) ) ,
                                   ( ((inputPixelsY[inputPixelIndex]) - inputOffset[1]) - ((eval(varName(imageID[0], imageID[1], 2)+"[imagePixelIndex]")) - imageOffset[1]) )); #this complex line just does the distance formula for two pixels
            if distance < bestDistance:
                bestDistance = distance;
                if advanced > 2:
                    print("Found better distance:", distance);
        if advanced > 1:
            print("Best pixel distance was:", bestDistance);
        totalScore += bestDistance;
    averageScore = totalScore / len(inputPixelsX); #computes distance error Per Pixel with basic mean
    print("Average score is:", averageScore, "\nTotal score is:", totalScore);
    scores.append(averageScore); # adds to the list of scores to view at end
    if averageScore < bestImageScore:
        bestImageScore = averageScore;
        bestImage = imageID;
        print("New best image with an average score of:", averageScore, "and an ID of", imageID);
print("Images Checked:", imagesToCheck);
print("Scores:", scores);
print("The most suitable image for the inputted image is after the input-sided algorithm is:", bestImage);
input("Press ENTER to continue");

#algorithm two: reverse
bsBestImage = [255, 255]; #255 is fallback if no image becomes better, in other words, if no images are checked or if there is an error
bsBestImageScore = 255;
inputOffset = findMeanCenter(inputPixelsX, inputPixelsY);
inputOffset = [round(item,3) for item in inputOffset];
for imageID in imagesToCheck: #imageID is [number,variant]
    imageOffset = eval("findMeanCenter("+varName(imageID[0], imageID[1], 1)+","+varName(imageID[0], imageID[1], 2)+")");
    imageOffset = [round(item,3) for item in imageOffset];
    totalScore = 0; #Score before made into average, take the closest pixel to each input pixel and measure the distance and sum them up
    for imagePixelIndex in range(0, len(eval(varName(imageID[0], imageID[1], 1)))):
        bestDistance = 255; #same fallback, and by the way 255 has no specific meaning in this context
        for inputPixelIndex in range(0, len(inputPixelsX)): 
            distance = math.hypot( ( ((inputPixelsX[inputPixelIndex]) - inputOffset[0]) - ((eval(varName(imageID[0], imageID[1], 1)+"[imagePixelIndex]")) - imageOffset[0]) ) ,
                                   ( ((inputPixelsY[inputPixelIndex]) - inputOffset[1]) - ((eval(varName(imageID[0], imageID[1], 2)+"[imagePixelIndex]")) - imageOffset[1]) )); #this complex line just does the distance formula for two pixels
            if distance < bestDistance:
                bestDistance = distance;
                if advanced > 2:
                    print("Found better distance:", distance);
        if advanced > 1:
            print("Best pixel distance was:", bestDistance);
        totalScore += bestDistance;
    averageScore = totalScore / len(eval(varName(imageID[0], imageID[1], 1))); #computes distance error Per Pixel with basic mean
    print("Average score is:", averageScore, "\nTotal score is:", totalScore);
    bsScores.append(averageScore); # adds to the list of scores to view at end
    if averageScore < bsBestImageScore:
        bsBestImageScore = averageScore;
        bsBestImage = imageID;
        print("New best image with an average score of:", averageScore, "and an ID of", imageID);

print("Images Checked:", imagesToCheck);
print("Scores:", bsScores);
print("The most suitable image for the inputted image after the benchmark-sided algorithm is:", bsBestImage);
combdScores = [sum(x) for x in zip(scores, bsScores)]; #combd is combined
combdBestImage = imagesToCheck[combdScores.index(min(combdScores))];
print("The most suitable image for the inputted image is:", combdBestImage);
input("Press ENTER to exit");

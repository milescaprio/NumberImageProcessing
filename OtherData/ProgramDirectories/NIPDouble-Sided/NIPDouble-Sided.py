import math
import sys
from benchmarks import *

pixelInputImage = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]];

inputPixelsX = [];
inputPixelsY = [];

IMAGESIZE = 16; #16*16 image processing
imagesToCheck = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]];
scores = [];
bsScores = []; #bs is benchmark side!!!

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





#/--------------------------------MAIN--------------------------------\#
run = eval(input("What would you like to do? 1. Start 2. Slice (debug-only)"));
#CHANGE THIS EVAL TO INT BEFORE PUBLISHING! USER CAN RUN COMMANDS

if run == 2:
    mySlice();
    sys.exit();

userInput = input("Put input image here, if you want to use internal input press ENTER")    
if userInput != "":
    pixelInputImage = eval(userInput)

advanced = int(input("Debug info level (Takes more execution time with more info) 1/2/3"));

temp = argSlice(pixelInputImage); #slice input image with argSlice()
inputPixelsX = temp[0];
inputPixelsY = temp[1];

#algorithm two: here we go
bestImage = [255, 255]; #255 is fallback if no image becomes better, in other words, if no images are checked or if there is an error
bestImageScore = 255;
for imageID in imagesToCheck: #imageID is [number,variant]
    totalScore = 0; #Score before made into average, take the closest pixel to each input pixel and measure the distance and sum them up
    for inputPixelIndex in range(0, len(inputPixelsX)):
        bestDistance = 255; #same fallback, and by the way 255 has no specific meaning in this context
        for imagePixelIndex in range(0, len(eval(varName(imageID[0], imageID[1], 1)))): 
            distance = math.hypot( ( (inputPixelsX[inputPixelIndex]) - (eval(varName(imageID[0], imageID[1], 1)+"[imagePixelIndex]")) ) ,
                                   ( (inputPixelsY[inputPixelIndex]) - (eval(varName(imageID[0], imageID[1], 2)+"[imagePixelIndex]")) ) ); #this complex line just does the distance formula for two pixels
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
for imageID in imagesToCheck: #imageID is [number,variant]
    totalScore = 0; #Score before made into average, take the closest pixel to each input pixel and measure the distance and sum them up
    for imagePixelIndex in range(0, len(eval(varName(imageID[0], imageID[1], 1)))):
        bestDistance = 255; #same fallback, and by the way 255 has no specific meaning in this context
        for inputPixelIndex in range(0, len(inputPixelsX)): 
            distance = math.hypot( ( (inputPixelsX[inputPixelIndex]) - (eval(varName(imageID[0], imageID[1], 1)+"[imagePixelIndex]")) ) ,
                                   ( (inputPixelsY[inputPixelIndex]) - (eval(varName(imageID[0], imageID[1], 2)+"[imagePixelIndex]")) ) ); #this complex line just does the distance formula for two pixels
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

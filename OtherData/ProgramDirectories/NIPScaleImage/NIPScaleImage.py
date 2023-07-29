import math
import sys
import tkinter
from PIL import Image
from tkinter.filedialog import askopenfile
from benchmarks import *
import whiteboard

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
DEFAULTIMAGECENTER = (IMAGESIZE-1)/2; #python indices is the -1 and then div by 2 to get the center
ROUNDPRECISION = 3;
imagesToCheck = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]];
scores = [];
bsScores = []; #bs is benchmark side!!!
didShift = 0;
shiftedOffset = 0;

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
def mySlice(localROUNDPRECISION = ROUNDPRECISION):
    benchmarkPixelsX = [];
    benchmarkPixelsY = [];
    for imageID in imagesToCheck:
        print("\nNumber:",imageID[0],"\n")
        benchmarkPixelsX.clear();
        benchmarkPixelsY.clear();
        forLoopY = 0;
        while forLoopY < IMAGESIZE: #forLoop because of preference over python FOR
            forLoopX = 0;
            while forLoopX < IMAGESIZE:
                if eval((varName(imageID[0],imageID[1],0)+"[forLoopY][forLoopX] == 1")):
                    benchmarkPixelsX.append(forLoopX);
                    benchmarkPixelsY.append(forLoopY);
                    print("Found Pixel at ", forLoopX, forLoopY);
                forLoopX += 1;
            forLoopY += 1;
        print("Original:",benchmarkPixelsX,"and",benchmarkPixelsY,"\n");
        benchmarkOffset = eval("findMeanCenter("+varName(imageID[0], imageID[1], 1)+","+varName(imageID[0], imageID[1], 2)+")");
        print(benchmarkOffset);
        benchmarkPixelsX = [i - benchmarkOffset[0] for i in benchmarkPixelsX];
        benchmarkPixelsX = [round(item, localROUNDPRECISION) for item in benchmarkPixelsX];
        benchmarkPixelsY = [i - benchmarkOffset[1] for i in benchmarkPixelsY];
        benchmarkPixelsY = [round(item, localROUNDPRECISION) for item in benchmarkPixelsY];
        print("Shifted:",benchmarkPixelsX,"and",benchmarkPixelsY,"\n");
        

def argSlice(pixelImage, debuginfo = 3, doCenterShift = False, doScale = False, changeLinkedVars = False, localIMAGESIZE = IMAGESIZE, localROUNDPRECISION = ROUNDPRECISION):
    #algorithm one: need to change input image to pixel map in a list: inputPixelsX and inputPixelsY
    imagePixelsX = [];
    imagePixelsY = [];
    global didShift;
    global shiftedOffset;
    forLoopY = 0;
    while forLoopY < localIMAGESIZE: #forLoop because of preference over python FOR
        forLoopX = 0;
        while forLoopX < localIMAGESIZE:
            if pixelImage[forLoopY][forLoopX] == 1:
                imagePixelsX.append(forLoopX);
                imagePixelsY.append(forLoopY);
                if debuginfo > 1:
                    print("Found Pixel at ", forLoopX, forLoopY);
            forLoopX += 1;
        forLoopY += 1;
    #that was easy
    if debuginfo > 1:
            print("After First Slice:")
            print(imagePixelsX,"and",imagePixelsY);
    if doCenterShift:
        shiftedOffset = findMeanCenter(imagePixelsX, imagePixelsY);
        imagePixelsX, imagePixelsY = shiftImagePixels(imagePixelsX, imagePixelsY, shiftedOffset);
        didShift = 1;
        if debuginfo > 1:
            print("After Center Shift:")
            print(imagePixelsX,"and",imagePixelsY);
    if doScale:
        scale = findScaleGoal(imagePixelsX, imagePixelsY);
        #THESE VALUES Are determined by x where: |1-(x/repopulationDensity)| = |1-(x/(repopulationDensity+1))|; the cutoff for which is closer to one; I used wolframalpha.com
        passDoRepopulate = False;
        passRepopulationDensity = 0;
        if scale > (4/3):
            passDoRepopulate = True;
            passRepopulationDensity = 1;
        if scale > (12/5):
            passRepopulationDensity = 2;
        if scale > (24/7):
            passRepopulationDensity = 3;
        if scale > (40/9):
            passRepopulationDensity = 4;
        if scale > (60/11):
            passRepopulationDensity = 5;
        if scale > (84/13):
            passRepopulationDensity = 6;
        imagePixelsX, imagePixelsY = scaleAboutCenter(imagePixelsX, imagePixelsY, pixelImage, scale, doRepopulate = passDoRepopulate, repopulationDensity = passRepopulationDensity, redoRepopulateShift = didShift, repopulateOffset = shiftedOffset)
        if debuginfo > 1:
            print("After Scale:")
    if debuginfo > 0:
        print(imagePixelsX,"and",imagePixelsY);
        input("View Scaled Image? Copy and paste of press ENTER to continue")
    return (imagePixelsX, imagePixelsY);

#Shifter Algorithm
def findMeanCenter(imagePixelsX, imagePixelsY, localIMAGESIZE = IMAGESIZE):
    xCenter = sum(imagePixelsX)/len(imagePixelsX);
    yCenter = sum(imagePixelsY)/len(imagePixelsY);
    xOffset = xCenter-7.5;
    yOffset = yCenter-7.5;
    return([xOffset, yOffset]);

def shiftImagePixels(imagePixelsX, imagePixelsY, offset, localROUNDPRECISION = ROUNDPRECISION):
    imagePixelsX = [i - offset[0] for i in imagePixelsX];
    imagePixelsX = [round(item, localROUNDPRECISION) for item in imagePixelsX];
    imagePixelsY = [i - offset[1] for i in imagePixelsY];
    imagePixelsY = [round(item, localROUNDPRECISION) for item in imagePixelsY];
    return(imagePixelsX, imagePixelsY);

def findScaleGoal(imagePixelsX, imagePixelsY, doHitEdgeMethod = 0, localIMAGESIZE = IMAGESIZE):
    if doHitEdgeMethod:
        pass;
    else:
        return (localIMAGESIZE - 1) / max(max(imagePixelsX) - min(imagePixelsX), max(imagePixelsY) - min(imagePixelsY));
def scaleAboutCenter(imagePixelsX, imagePixelsY, pixelImage, scale, doRepopulate = False, repopulationDensity = 1, center = DEFAULTIMAGECENTER, redoRepopulateShift = 0, repopulateOffset = 0, debuginfo = 2, localIMAGESIZE = IMAGESIZE, localROUNDPRECISION = ROUNDPRECISION):
    if doRepopulate:
        repopulatePixelsX = [];
        repopulatePixelsY = [];
        #Add repopulation pixels in between connected pixels by Y:
        for y in range(localIMAGESIZE - 1):
            for x in range(localIMAGESIZE):
                if pixelImage[y][x] and pixelImage[y+1][x]:
                    for repopulationSpot in range(1, repopulationDensity+1):
                        repopulatePixelsY.append(y + repopulationSpot/(repopulationDensity+1));
                        repopulatePixelsX.append(x);
                    pixelImage[y][x] = 2; #no longer eligible to repop surrounding diagonals
                    pixelImage[y+1][x] = 2; #no longer eligible to repop surrounding diagonals
        #Add repopulation pixels in between connected pixels by X:
        for y in range(localIMAGESIZE):
            for x in range(localIMAGESIZE - 1):
                if pixelImage[y][x] and pixelImage[y][x+1]:
                    for repopulationSpot in range(1, repopulationDensity+1):
                        repopulatePixelsY.append(y);
                        repopulatePixelsX.append(x + repopulationSpot/(repopulationDensity+1));
                    pixelImage[y][x] = 2; #no longer eligible to repop surrounding diagonals
                    pixelImage[y][x+1] = 2; #no longer eligible to repop surrounding diagonals
        #Add repopulation pixels in between connected pixels by Diagonals (slope down then slope up):
        for y in range(localIMAGESIZE - 1):
            for x in range(localIMAGESIZE - 1):
                if pixelImage[y][x] and pixelImage[y+1][x+1] and (not pixelImage[y+1][x] == 2) and (not pixelImage[y][x+1] == 2):
                    for repopulationSpot in range(1, repopulationDensity+1):
                        repopulatePixelsY.append(y + repopulationSpot/(repopulationDensity+1));
                        repopulatePixelsX.append(x + repopulationSpot/(repopulationDensity+1));
        for y in range(localIMAGESIZE - 1):
            for x in range(1, localIMAGESIZE):
                if pixelImage[y][x] and pixelImage[y+1][x-1] and (not pixelImage[y+1][x] == 2) and (not pixelImage[y][x-1] == 2):
                    for repopulationSpot in range(1, repopulationDensity+1):
                        repopulatePixelsY.append(y + repopulationSpot/(repopulationDensity+1));
                        repopulatePixelsX.append(x - repopulationSpot/(repopulationDensity+1));

        
        if redoRepopulateShift:
            repopulatePixelsX, repopulatePixelsY = shiftImagePixels(repopulatePixelsX, repopulatePixelsY, repopulateOffset);
        imagePixelsX = imagePixelsX.copy() + repopulatePixelsX.copy();
        imagePixelsY = imagePixelsY.copy() + repopulatePixelsY.copy();
        if debuginfo > 1:
            print("After Repopulate:");
            print("\n",imagePixelsX, imagePixelsY, "\n");

    #start scaling
    newImagePixelsX = imagePixelsX.copy();
    newImagePixelsY = imagePixelsY.copy();
    for xPixel in range(len(imagePixelsX)):
        oldX = imagePixelsX[xPixel];
        newX = ((oldX - center) * scale) + center; #scale about center
        newImagePixelsX[xPixel] = round(newX, localROUNDPRECISION);
    for yPixel in range(len(imagePixelsY)):
        oldY = imagePixelsY[yPixel];
        newY = ((oldY - center) * scale) + center; #scale about center
        newImagePixelsY[yPixel] = round(newY, localROUNDPRECISION);
    return (newImagePixelsX, newImagePixelsY);
    
def cropToSquare(tocrop):
    """:param Image tocrop: The PIL Image to crop."""
    if tocrop.width % 2:
        print("Odd pixel width. Cutting end column.");
        tocrop = tocrop.crop((0, 0, tocrop.width - 1, tocrop.height));
    if tocrop.height % 2:
        print("Odd pixel height. Cutting end row.");
        tocrop = tocrop.crop((0, 0, tocrop.width, tocrop.height - 1));

    if tocrop.width == tocrop.height:
        return tocrop;
    cropsquare = min(tocrop.size);
        
    if tocrop.width > tocrop.height:
        cropped = tocrop.crop( ( (tocrop.width-cropsquare)/2 , 0 , (tocrop.width+cropsquare)/2, tocrop.height) );
    if tocrop.width < tocrop.height:
        cropped = tocrop.crop( ( 0 , (tocrop.height-cropsquare)/2 , tocrop.width , (tocrop.height+cropsquare)/2) );
    return cropped;

#/--------------------------------MAIN--------------------------------\#
run = eval(input("What would you like to do? 1. Start 2. Slice (debug-only)\n"));
#CHANGE THIS EVAL TO INT BEFORE PUBLISHING! USER CAN RUN COMMANDS

if run == 2:
    mySlice();
    input("Press ENTER to continue...")
    sys.exit();

userInputMethod = int(input("How would you like to select an image? 1.Draw 2.Use internal \n3.Paste image array 4.Open image file\n"));
if userInputMethod == 4:
    img = Image.open(askopenfile().name, 'r');
    img = cropToSquare(img);
    img = img.resize((16,16));
    if input("Show preview image?") == "y":
        img.show();
    imgArr = img.load();
    height = img.height;
    width = img.width;
    isBright = (input("Is the imported image focus bright or dark? b/d") == 'b')
    if isBright:
        rgbSumInput = input("What RGB sum threshold to register as a positive bit would you like to use? \n0-254 (Very tolerant-Very strict)? Press enter to use default of 126\n");
    else:
        rgbSumInput = input("What RGB sum threshold to register as a positive bit would you like to use? \n1-255 (Very strict-Very tolerant)? Press enter to use default of 127\n");
    if rgbSumInput == '':
        rgbSum = 127-isBright;
    else:
        rgbSum = int(rgbSumInput);
    if isBright:
        pixelInputImage = [[(max(imgArr[col,row]) > rgbSum)*1 for col in range(width)] for row in range(height)];
    else:
        pixelInputImage = [[(max(imgArr[col,row]) < rgbSum)*1 for col in range(width)] for row in range(height)];
    print(pixelInputImage);
if userInputMethod == 3:
    pixelInputImage = eval(input("Paste array here"));
if userInputMethod == 2:
    pass;
if userInputMethod == 1:
    print("Draw on whiteboard and press space when complete");
    whiteboard.start()
    pixelInputImage = whiteboard.image;
    print(pixelInputImage);  
advanced = int(input("Debug info level (Takes more execution time with more info) 0/1/2/3"));

if advanced > 0:
    print("Slicing...");
inputPixelsX, inputPixelsY = argSlice(pixelInputImage, debuginfo = advanced, doCenterShift = True, doScale = True); #slice input image with argSlice()
if advanced > 0:
    print("Done Slicing.");
if len(inputPixelsX) < 1:
    input("No pixels determined. No number image to process. Terminating... Press ENTER to continue");
    sys.exit();

#algorithm two: here we go
bestImage = [255, 255]; #255 is fallback if no image becomes better, in other words, if no images are checked or if there is an error
bestImageScore = 255;
for imageID in imagesToCheck: #imageID is [number,variant]
    totalScore = 0; #Score before made into average, take the closest pixel to each input pixel and measure the distance and sum them up
    for inputPixelIndex in range(0, len(inputPixelsX)):
        bestDistance = 255; #same fallback, and by the way 255 has no specific meaning in this context
        for imagePixelIndex in range(0, len(eval(varName(imageID[0], imageID[1], 1)))): 
            distance = math.hypot( ( inputPixelsX[inputPixelIndex] - eval(varName(imageID[0], imageID[1], 1)+"[imagePixelIndex]") ) ,
                                   ( inputPixelsY[inputPixelIndex] - eval(varName(imageID[0], imageID[1], 2)+"[imagePixelIndex]") ) ); #this complex line just does the distance formula for two pixels
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
            distance = math.hypot( ( inputPixelsX[inputPixelIndex] - eval(varName(imageID[0], imageID[1], 1)+"[imagePixelIndex]") ) ,
                                   ( inputPixelsY[inputPixelIndex] - eval(varName(imageID[0], imageID[1], 2)+"[imagePixelIndex]") ) ); #this complex line just does the distance formula for two pixels
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

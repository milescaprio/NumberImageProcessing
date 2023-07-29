IMAGESIZE = 16

def findMeanCenter(imagePixelsX, imagePixelsY, localIMAGESIZE = IMAGESIZE):
    xCenter = sum(imagePixelsX)/len(imagePixelsX);
    yCenter = sum(imagePixelsY)/len(imagePixelsY);
    xOffset = xCenter-7.5;
    yOffset = yCenter-7.5;
    return([xOffset, yOffset]);

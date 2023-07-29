import turtle
wn = turtle.Screen()
screen = wn.getcanvas()
clicking = False
clickx = 0
clicky = 0
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
def start():
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
start();
def drawSquare(thex,they):
    global clickx
    global clicky
    global wbImage
    clickx = thex
    clicky = they
    pixelX = round(clickx//16)
    pixelY = round(clicky//16)
    if pixelY < 0 or pixelY > 15 or pixelX < 0 or pixelX > 15:
        return
    currentPixel = wbImage[pixelY][pixelX];
    wbImage[pixelY][pixelX] = 1 - currentPixel;
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
    del lT
def exitTurtle(dummy = None, dummy2 = None):
    print(wbImage);

wn.onclick(drawSquare);
wn.onkey(exitTurtle,"space");
wn.listen();

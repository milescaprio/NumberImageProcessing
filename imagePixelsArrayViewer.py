import turtle
clickx = 0
clicky = 0
imagePixelsX, imagePixelsY = eval(input("Paste image pixels tuple format here: "))
def drawSquare(pixelX,pixelY):
    lT = turtle.Turtle();
    lT.hideturtle();
    lT.color("red");
    lT.fillcolor("red");
    lT.speed(100000);
    lT.penup();
    lT.goto((pixelX)*16, (pixelY)*16);
    lT.pendown();
    lT.begin_fill();
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
    lT.penup();
    del lT
def exitTurtle(dummy = None, dummy2 = None):
    turtle.bye()
def start():
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
    for i in range(len(imagePixelsY)):
        drawSquare(round(imagePixelsX[i],0),round(15 - imagePixelsY[i],0));
    wn.onkey(exitTurtle,"space");
    wn.listen();
    turtle.done()
start();

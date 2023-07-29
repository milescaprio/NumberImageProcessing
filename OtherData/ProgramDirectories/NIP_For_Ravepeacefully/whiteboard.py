import turtle
returnable = 0;
clickx = 0
clicky = 0
image = [
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
    currentPixel = image[15 - pixelY][pixelX];
    image[15 - pixelY][pixelX] = 1 - currentPixel;
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
    turtle.bye();
    returnable = 1;
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
    wn.onclick(drawSquare);
    wn.onkey(exitTurtle,"space");
    i = 0
    while True:
        i += 1;
        wn.listen();
        if i >= 25:
            break

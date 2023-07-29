import turtle
import time
wn = turtle.Screen()
screen = wn.getcanvas()
clicking = False
clickx = 0
clicky = 0
def start():
    turtle.hideturtle();
    wn.bgcolor("black");
    turtle.color("white");
    turtle.speed(100000);
    turtle.screensize(256,256);
    turtle.fillcolor("white");
    turtle.goto(0,0);
    turtle.pendown();
    turtle.begin_fill();
    turtle.goto(0,0);
    turtle.goto(255,0);
    turtle.goto(255,255);
    turtle.goto(0,255);
    turtle.goto(0,0);
    turtle.end_fill();
    turtle.penup();
    turtle.fillcolor("red");
    turtle.color("red");
start();
def drawSquare(thex,they):
    global clickx
    global clicky
    clickx = thex
    clicky = they
    print(clickx, clicky)
    turtle.goto((clickx//16)*16, (clicky//16)*16)
    turtle.pendown()
    turtle.begin_fill()
    turtle.seth(90)
    turtle.fd(15);
    turtle.right(90);
    turtle.fd(15);
    turtle.right(90);
    turtle.fd(15);
    turtle.right(90);
    turtle.fd(15);
    turtle.right(90);
    turtle.end_fill();
    turtle.penup()
def test(event):
    wn.onclick(drawSquare);
        
screen.bind('<Motion>', test)


import turtle
wn = turtle.Screen()
screen = wn.getcanvas()
def start():
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
start();
def test(event):
##    print("Onscreen Coords",(event.x,event.y))
##    print("Weird Function:",(event.x-screen.width/2, (event.y*-1)+screen.height/2))
    wn.onclick(turtle.goto);
screen.bind('<Motion>', test)
#while True:
#    test();

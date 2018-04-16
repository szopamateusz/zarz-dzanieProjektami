import turtle

def Prostokat(color):
    t.pencolor(color)
    t.forward(100);
    t.right(90);
    t.forward(50);
    t.right(90);
    t.forward(100);
    t.right(90);
    t.forward(50);

def Kwadrat(color):
    t.pencolor(color)
    t.forward(100);
    t.right(90);
    t.forward(100);
    t.right(90);
    t.forward(100);
    t.right(90);
    t.forward(100);

def Trojkat(color):
    t.pencolor(color)
    t.forward(40);
    t.right(90);
    t.forward(40);
    t.right(135);
    t.forward(60);
colors = [
    "#880000", "#884400", "#888800", "#008800",
    "#008888", "#000088", "#440088", "#880088"
]
angle =360/len(colors)
def Okrag():
    for color in colors:
        t.color(color)
        t.circle(150,angle)

figura = raw_input("podaj co narysowac: kwardrat:1,prostokat:2,trojkat:3,kolo:4")
kolor = raw_input("podaj kolor")

wn = turtle.Screen();
wn.bgcolor("white")
t = turtle.Turtle();
t.pensize(9)

if (figura == 1):
    Kwadrat(kolor)
elif (figura == 2):
    Prostokat(kolor)
elif (figura == 3):
    Trojkat(kolor)
elif (figura == 4):
    Kolo()
    

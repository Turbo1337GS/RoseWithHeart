import turtle

def draw_heart(t):
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()

def draw_I(t, x, y):
    # Ustalmy szerokość i wysokość litery I
    width = 20
    height = 80
    horizontal_line_length = 40

    # Rysujemy górną poziomą linię
    t.penup()
    t.goto(x - horizontal_line_length / 2, y)
    t.pendown()
    t.forward(horizontal_line_length)

    # Rysujemy dolną poziomą linię
    t.penup()
    t.goto(x - horizontal_line_length / 2, y - height)
    t.pendown()
    t.forward(horizontal_line_length)

    # Rysujemy pionową linię w środku
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y - height)

def draw_Y(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x + 20, y - 40)
    
    t.goto(x + 40, y)
    t.pendown()
    t.goto(x + 20, y - 40)
    
    t.goto(x + 20, y - 60)
    t.pendown()
    t.goto(x + 20, y - 80)

def draw_O(t, x, y):
    t.penup()
    t.goto(x + 25, y)
    t.pendown()
    t.circle(25)
    
    
def draw_u(t, x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    
    t.setheading(270)
    t.forward(40)
    t.circle(20, 180)
    t.forward(40)
    t.hideturtle()
 

def draw_petal(t):
    """Draw a single petal."""
    t.circle(100, 60)
    t.left(120)
    t.circle(100, 60)
    t.left(120)

def draw_petal(t, color="white"):
    t.fillcolor(color)
    t.begin_fill()

    # flower base
    t.circle(10, 180)
    t.circle(25, 110)
    t.left(50)
    t.circle(60, 45)
    t.circle(20, 170)
    t.right(24)
    t.fd(30)
    t.left(10)
    t.circle(30, 110)
    t.fd(20)
    t.left(40)
    t.circle(90, 70)
    t.circle(30, 150)
    t.right(30)
    t.fd(15)
    t.circle(80, 90)
    t.left(15)
    t.fd(45)
    t.right(165)
    t.fd(20)
    t.left(155)
    t.circle(150, 80)
    t.left(50)
    t.circle(150, 90)

    t.end_fill()


def draw_leaves(t, color="green"):
    t.fillcolor(color)

    # Leaves 1
    t.begin_fill()
    t.fd(30)
    t.left(90)
    t.fd(25)
    t.left(45)
    t.circle(-80, 90)
    t.right(90)
    t.circle(-80, 90)
    t.end_fill()
    t.right(135)
    t.fd(60)
    t.left(180)
    t.fd(85)
    t.left(90)
    t.fd(80)

    # Leaves 2
    t.begin_fill()
    t.right(90)
    t.right(45)
    t.circle(80, 90)
    t.left(90)
    t.circle(80, 90)
    t.end_fill()
    t.left(135)
    t.fd(60)
    t.left(180)
    t.fd(60)
    t.right(90)
    t.circle(200, 60)


def draw_rose(t, x, y, petal_color="white", leaf_color="green"):
    t.penup()
    t.setpos(x, y)
    t.pendown()

    draw_petal(t, petal_color)
    
    # Petal 1
    t.left(150)
    t.circle(-90, 70)
    t.left(20)
    t.circle(75, 105)
    t.setheading(60)
    t.circle(80, 98)
    t.circle(-90, 40)

    # Petal 2
    t.left(180)
    t.circle(90, 40)
    t.circle(-80, 98)
    t.setheading(-83)

    draw_leaves(t, leaf_color)



def draw_message_updated():
    window = turtle.Screen()
    window.colormode(255) 
    window.bgcolor(30, 30, 30) 

    t = turtle.Turtle()
    t.speed(1)
    t.width(3)

    t.color("white")
    draw_I(t, -145, 20)  

    t.penup()
    t.goto(-20, -40)
    t.pendown()
    t.color("red")
    draw_heart(t)

    t.color("white")
    draw_Y(t, 70, 20)
    draw_O(t, 100, -10)
    draw_u(t, 180, 0)
    
    draw_rose(t,0,-300)

    window.mainloop()

draw_message_updated()

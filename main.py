import turtle as t


t.pensize(3)
wn = t.Screen()
wn.bgcolor("light blue")

#make sure that the turtle is facing north first
def draw_tree(x:int = 0, y:int = 0, n_leaves:int = 5):
    #save penstate
    pen_color_state = t.pen().get("pencolor")
    # move to coordinates
    t.penup()
    t.goto(x, y)
    t.pendown()
    # start drawing
    t.pencolor("saddle brown")
    t.forward(30)

    t.pencolor("green")
    #draw leaves for left side
    for i in range(n_leaves):
        t.left(90)
        t.forward(20)
        t.right(140)
        t.forward(30)
        t.left(50)

    for i in range(n_leaves):
        t.right(130)
        t.forward(30)
        t.right(140)
        t.forward(20)
        t.right(90)
    t.pencolor("saddle brown")
    t.right(180)
    t.forward(30)
    # revert pencolor to whatever color it was before drawing tree
    t.pencolor(pen_color_state)

def draw_sun(x: int = 0, y:int = 0, radius: int = 10):
    pen_color_state = t.pen().get("pencolor")
    t.pencolor("yellow")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(radius)
    # revert pencolor
    t.pencolor(pen_color_state)


t.left(90)
# draw_tree()
draw_sun(radius=20)
t.done()
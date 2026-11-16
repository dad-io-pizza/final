import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(20)
t.color("red")

if __name__=="__main__":

    t.teleport(-500,0)

    for i in range(100):
        t.circle(10)
        t.forward(10)

    t.teleport(0,500)
    t.right(90)

    for i in range(500):
        t.circle(10)
        t.forward(10)

    t.teleport(-600,600)
    t.left(45)
    t.color("green")

    for i in range(500):
        t.circle(10)
        t.forward(10)

    t.teleport(600,600)
    t.right(90)

    for i in range(500):
        t.circle(10)
        t.forward(10)

    def draw_bow(x,y):
        t.color("red")
        t.fillcolor("red")
        t.begin_fill()
        t.speed(2)
        t.teleport(x,y)
        t.right(15)
        t.forward(200)
        t.right(120)
        t.forward(200)
        t.right(120)
        t.forward(400)
        t.left(120)
        t.forward(200)
        t.left(120)
        t.forward(200)
    
    draw_bow(0,0)
    t.teleport(-3,10)
    t.circle(20)
    t.end_fill()

    


turtle.done()

import turtle as te

te.speed(20)
te.bgcolor('black')
te.pensize(5)


def func():
    for i in range(300):
        te.right(1)
        te.forward(1)

te.color('yellow', 'orange')
te.begin_fill()


te.left(70)
#te.forward(111,65)

func()
te.left(140)
func()
te.forward(200,89)
te.end_fill()
te.hideturtle()
te.done()


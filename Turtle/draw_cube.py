import turtle

sc = turtle.Screen()
cb = turtle.Turtle()


# method to draw square
def draw():
    for i in range(4):
        cb.forward(40)
        cb.left(90)

    cb.forward(40)


# Driver Code
if __name__ == "__main__":

    # set screen
    sc.setup(800, 800)

    # set turtle object speed
    cb.speed(100)

    # loops for board
    for i in range(10):

        # not ready to draw
        cb.up()

        # set position for every row
        cb.setpos(-100, 40 * i)

        # ready to draw
        cb.down()

        # row
        for j in range(10):

            # conditions for alternative color
            if (i + j) % 2 == 0:
                col = 'blue'

            else:
                col = 'yellow'

            # fill with given color
            cb.fillcolor(col)

            # start filling with colour
            cb.begin_fill()

            # call method
            draw()
            # stop filling
            cb.end_fill()

            # hide the turtle
    cb.hideturtle()
    turtle.done()
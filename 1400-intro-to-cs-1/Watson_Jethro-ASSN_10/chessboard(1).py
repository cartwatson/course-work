import turtle

tr = turtle.Turtle()


def drawChessboard(startX, startY, width=250, height=250):
    tr.hideturtle()
    tr.pu()
    tr.setpos(startX, startY)
    tr.pd()
    tr.pos()
    # draw outside of chessboard
    tr.seth(0)
    tr.fd(width)
    tr.right(90)
    tr.fd(height)
    tr.right(90)
    tr.fd(width)
    tr.right(90)
    tr.fd(height)
    tr.right(90)
    # draw mini squares
    drawMini(startX, startY, width, height)
    turtle.done()


def drawMini(startX, startY, width, height):
    smallW = width / 8
    smallH = height / 8
    tr.pu()
    tr.home()
    tr.setpos(startX, startY - smallH * 8)
    # draw all rectangles
    for x in range(2):
        # draw rectangle
        for h in range(4):
            # draw columns
            for w in range(4):
                # draw rows
                tr.seth(0)
                tr.begin_fill()
                tr.fd(smallW)
                tr.left(90)
                tr.fd(smallH)
                tr.left(90)
                tr.fd(smallW)
                tr.left(90)
                tr.fd(smallH)
                tr.left(90)
                tr.end_fill()
                tr.fd(smallW * 2)
            tr.seth(90)
            tr.fd(smallH * 2)
            tr.seth(180)
            tr.fd(width)
        tr.setpos(startX + smallW, startY - smallH * 7)

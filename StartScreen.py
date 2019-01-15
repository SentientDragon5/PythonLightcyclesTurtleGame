import turtle
turtle.bgcolor("black")
start = turtle.Turtle()
start.hideturtle()
start.color('white')
def TR():
    left_T = [(-85,50),(-75,50),(-75,40),(-85,40)]
    start.up()
    start.goto(-85,40)
    start.down()
    for left_Tvar in left_T:
        start.goto(left_Tvar)

    top_R = [(-70,40),(-60,50),(-20,50),(-5,45),(0,40),(-55,40),(-60,35),(-60,5),(-70,5)]
    start.up()
    start.goto(-70,5)
    start.down()
    for top_Rvar in top_R:
        start.goto(top_Rvar)

    left_R = [(-35,35),(-35,5),(-45,5),(-45,35)]
    start.up()
    start.goto(-45,35);
    start.down()
    for left_Rvar in left_R:
        start.goto(left_Rvar)

    right_R = [(0,35),(-5,30),(-20,25),(0,5),(-10,5),(-30,25),(-30,35)]
    start.up()
    start.goto(-30,35);
    start.down()
    for right_Rvar in right_R:
        start.goto(right_Rvar)

def O():
    out_O = [(10,45),(20,50),(35,50),(45,45),(50,35),(50,20),(45,10),(35,5),(20,5),(10,10),(5,20),(5,35)]
    start.up()
    start.goto(5,35);
    start.down()
    for out_Ovar in out_O:
        start.goto(out_Ovar)

    in_O = [(25,40),(30,40),(40,30),(40,25),(30,15),(25,15),(15,25),(15,30)]
    start.up()
    start.goto(15,30);
    start.down()
    for in_Ovar in in_O:
        start.goto(in_Ovar)

def N():
    left_N = [(55,50),(60,50),(70,30),(70,25),(63,25),(63,5),(55,5)]
    start.up()
    start.goto(55,5);
    start.down()
    for left_Nvar in left_N:
        start.goto(left_Nvar)

    right_N = [(70,25),(80,5),(85,5),(85,50),(77,50),(77,30),(70,30)]
    start.up()
    start.goto(70,30);
    start.down()
    for right_Nvar in right_N:
        start.goto(right_Nvar)

def spell_TRON():
    TR()
    O()
    N()

spell_TRON()

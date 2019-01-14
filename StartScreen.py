import turtle
turtle.bgcolor("black")
start = turtle.Turtle()
start.hideturtle()
start.color('white')

#top left of T
start.up()
start.goto(-85,40)
start.down()

start.goto(-85,50);
start.goto(-75,50);
start.goto(-75,40);
start.goto(-85,40);

#bottom of T, top right of T, Top of R
start.up()
start.goto(-70,5)
start.down()

start.goto(-70,40)
start.goto(-60,50);
start.goto(-20,50);
start.goto(-5,45);
start.goto(0,40);
start.goto(-55,40);
start.goto(-60,35);
start.goto(-60,5);
start.goto(-70,5);

#bottom left of R
start.up()
start.goto(-45,35);
start.down()

start.goto(-35,35);
start.goto(-35,5);
start.goto(-45,5);
start.goto(-45,35);

#bottom right of R
start.up()
start.goto(-30,35);
start.down()

start.goto(0,35);
start.goto(-5,30);
start.goto(-20,25);
start.goto(0,5);
start.goto(-10,5);
start.goto(-30,25);
start.goto(-30,35);

#outside of O
start.up()
start.goto(5,35);
start.down()

start.goto(10,45);
start.goto(20,50);
start.goto(35,50);
start.goto(45,45);
start.goto(50,35);
start.goto(50,20);
start.goto(45,10);
start.goto(35,5);
start.goto(20,5);
start.goto(10,10);
start.goto(5,20);
start.goto(5,35)

#inside of O
start.up()
start.goto(15,30);
start.down()

start.goto(25,40);
start.goto(30,40);
start.goto(40,30);
start.goto(40,25);
start.goto(30,15);
start.goto(25,15);
start.goto(15,25);
start.goto(15,30);
start.up()
start.goto(15,30);
start.down()

#left N
start.up()
start.goto(55,5);
start.down()

start.goto(55,50);
start.goto(60,50);
start.goto(70,30);
start.goto(70,25);
start.goto(63,25);
start.goto(63,5);
start.goto(55,5);

#right N 3 away
start.up()
start.goto(73,30);
start.down()

start.goto(73,25);
start.goto(83,5);
start.goto(88,5);
start.goto(88,50);
start.goto(80,50);
start.goto(80,30);
start.goto(73,30);

#right N up close
start.up()
start.goto(70,30);
start.down()

start.goto(70,25);
start.goto(80,5);
start.goto(85,5);
start.goto(85,50);
start.goto(77,50);
start.goto(77,30);
start.goto(70,30);

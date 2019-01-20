import turtle
from random import randint
turtle.bgcolor("black")
startScreen = turtle.Turtle()
startScreen.hideturtle()
startScreen.color('white')

def draw_TRON_word():
  skip = False
  big = [("liftup"),(-85,40),(-85,50),(-75,50),(-75,40),(-85,40),
         ("liftup"),(-70,5),(-70,40),(-60,50),(-20,50),(-5,45),(0,40),(-55,40),(-60,35),(-60,5),(-70,5),
         ("liftup"),(-45,35),(-35,35),(-35,5),(-45,5),(-45,35),
         ("liftup"),(-30,35),(0,35),(-5,30),(-20,25),(0,5),(-10,5),(-30,25),(-30,35),
         ("liftup"),(5,35),(10,45),(20,50),(35,50),(45,45),(50,35),(50,20),(45,10),(35,5),(20,5),(10,10),(5,20),(5,35),
         ("liftup"),(15,30),(25,40),(30,40),(40,30),(40,25),(30,15),(25,15),(15,25),(15,30),
         ("liftup"),(55,5),(55,50),(60,50),(70,30),(70,25),(63,25),(63,5),(55,5),
         ("liftup"),(70,30),(70,25),(80,5),(85,5),(85,50),(77,50),(77,30),(70,30),
         ]
  for i in big:
      if skip == True:
        startScreen.up(); startScreen.goto(i); startScreen.down()
      skip = False
      if i == "liftup":
        skip = True
      else:
        startScreen.goto(i)
#init
def init():
  draw_TRON_word()
  introQuest = input("Welcome to TRON! \n press ENTER to start game \n press H for help\n")
  if introQuest == "h":
    print ("\n press enter to move forward \n press a to turn left \n press d to turn right \n press q to turn off trail \n press e to turn on trail \n press o to restart game \n press p to quit game")
  

def RoundToNearest(value, roundTarget):
  iValue = int(value)
  iRound = int(roundTarget)
  tmp = abs(iValue)
  tmp = tmp + int(iRound/2)
  tmp = int(tmp / iRound)
  
  tmp = int(tmp * iRound)
  if (iValue < 0):
    tmp = tmp * -1
  return tmp

def main():
  init()
  startScreen.clear()
  #tron initialize
  tron = turtle.Turtle()
  tron.down()
  tron.color('white')
  tron.goto(0,0)
  tron.clear()
  tronlog = True
  foe = turtle.Turtle()
  foe.goto(0,100)
  foe.clear()
  foe.down()
  foex = 0
  foey = 0
  foe.color('orange')
  pointing = 0
  tronpast = [(0,0)]
  
  #game begin
  loop = True;
  while loop == True:
    
    quest = input()
    forward = False
    liftup = False
    if quest == "w":
      forward = True
    elif quest == "a":
      forward = True
      tron.left(45)
    elif quest == "d":
      forward = True
      tron.right(45)
    elif quest == "q":
      tron.up()
      print ("up")
      tronlog = False
      liftup = True
    elif quest == "e":
      tron.down()
      print ("down")
      tronlog = True
    elif quest == "o":
      tron.goto(0,0)
      tron.clear()
      foe.goto(0,100)
      foe.clear()
      print ("~~~~~~~~~~~~~~~  RESTART GAME  ~~~~~~~~~~~~~~~~")
      tronpast = []
    elif quest == "p":
      loop = False
    elif quest == "":
      forward = True
    else:
      print ("invalid")

    if forward == True:
      tron.forward(50)
    tronx = RoundToNearest(tron.xcor(), 50)
    trony = RoundToNearest(tron.ycor(), 50)
    if forward == True:
      tron.goto(tronx,trony)
    if liftup == False:
      if (tronx,trony) in tronpast:
        print ("you crashed into a wall!\nRestart?(y/n)")
        restart = input()
        if restart == "y":
          tron.goto(0,0)
          tron.clear()
          foe.goto(0,100)
          foe.clear()
          print ("~~~~~~~~~~~~~~~  RESTART GAME  ~~~~~~~~~~~~~~~~")
          tronpast = []
        else:
          loop = False
    if tronlog == True:
      tronpast.append((tronx,trony))
    print ('You at',tronx,",",trony)

    #foe turn

    rotate = randint(1,4)
    direction = 0
    foeLeft = True
    foeForward = True
    foeRight = True
    LR = ('r')
    for tempPoint in  ['l','f','r']:
#    270
# 180 + 000
#    090
      if pointing == 0:
        if tempPoint == 'l':
           if (foex + 50,foey + 50) in tronpast:
             print ( "not left, pointing: ", pointing)
             foeLeft = False
        if tempPoint == 'f':
           if (foex + 50,foey) in tronpast:
             print ( "not forward, pointing: ", pointing)
             foeForward = False
        if tempPoint == 'r':
           if (foex + 50,foey - 50) in tronpast:
             print ( "not right, pointing: ", pointing)
             foeRight = False
    
    if pointing == 45:
        if tempPoint == 'l':
           if (foex + 50,foey) in tronpast:
             print ( "not left, pointing: ", pointing)
             foeLeft = False
        if tempPoint == 'f':
           if (foex - 50,foey - 50) in tronpast:
             print ( "not forward, pointing: ", pointing)
             foeForward = False
        if tempPoint == 'r':
           if (foex - 50,foey) in tronpast:
             print ( "not right, pointing: ", pointing)
             foeRight = False
             
    if pointing == 90:
        if tempPoint == 'l':
           if (foex + 50,foey - 50) in tronpast:
             print ( "not left, pointing: ", pointing)
             foeLeft = False
        if tempPoint == 'f':
           if (foex,foey - 50) in tronpast:
             print ( "not forward, pointing: ", pointing)
             foeForward = False
        if tempPoint == 'r':
           if (foex - 50,foey - 50) in tronpast:
             print ( "not right, pointing: ", pointing)
             foeRight = False
             
    if pointing == 135:
        if tempPoint == 'l':
           if (foex,foey - 50) in tronpast:
             print ( "not left, pointing: ", pointing)
             foeLeft = False
        if tempPoint == 'f':
           if (foex - 50,foey - 50) in tronpast:
             print ( "not forward, pointing: ", pointing)
             foeForward = False
        if tempPoint == 'r':
           if (foex - 50,foey) in tronpast:
             print ( "not right, pointing: ", pointing)
             foeRight = False
             
    if pointing == 180:
        if tempPoint == 'l':
           if (foex - 50,foey - 50) in tronpast:
             print ( "not left, pointing: ", pointing)
             foeLeft = False
        if tempPoint == 'f':
           if (foex - 50,foey) in tronpast:
             print ( "not forward, pointing: ", pointing)
             foeForward = False
        if tempPoint == 'r':
           if (foex - 50,foey + 50) in tronpast:
             print ( "not right, pointing: ", pointing)
             foeRight = False
             
    if pointing == 225:
        if tempPoint == 'l':
           if (foex - 50,foey) in tronpast:
             print ( "not left, pointing: ", pointing)
             foeLeft = False
        if tempPoint == 'f':
           if (foex - 50,foey + 50) in tronpast:
             print ( "not forward, pointing: ", pointing)
             foeForward = False
        if tempPoint == 'r':
           if (foex,foey + 50) in tronpast:
             print ( "not right, pointing: ", pointing)
             foeRight = False

    if pointing == 270:
        if tempPoint == 'l':
           if (foex - 50,foey + 50) in tronpast:
             print ( "not left, pointing: ", pointing)
             foeLeft = False
        if tempPoint == 'f':
           if (foex,foey + 50) in tronpast:
             print ( "not forward, pointing: ", pointing)
             foeForward = False
        if tempPoint == 'r':
           if (foex + 50,foey + 50) in tronpast:
             print ( "not right, pointing: ", pointing)
             foeRight = False
             
    if pointing == 315:
        if tempPoint == 'l':
           if (foex,foey + 50) in tronpast:
             print ( "not left, pointing: ", pointing)
             foeLeft = False
        if tempPoint == 'f':
           if (foex + 50,foey + 50) in tronpast:
             print ( "not forward, pointing: ", pointing)
             foeForward = False
        if tempPoint == 'r':
           if (foex + 50,foey) in tronpast:
             print ( "not right, pointing: ", pointing)
             foeRight = False
    
    foeforward = False
    if rotate >= (2):
      direction = randint(1,3)
      if LR == ('l'):
        if foeLeft == False:
          direction = (2)
        if direction == (1) or (3) or (4):
          foe.left(45)
          pointing -= 45
          LR = ('l')
        elif direction == (2):
          foe.right(45)
          pointing += 45
          LR = ('r')
      else:
        if foeRight == False:
          direction = (1)
        if direction == (1):
          foe.left(45)
          pointing -= 45
          LR = ('l')
        elif direction == (2) or (3) or (4):
          foe.right(45)
          pointing += 45
          LR = ('r')
    if pointing >= 360:
      pointing -= 360
    elif pointing < 0:
      pointing += 360
    print ("rotate: ",rotate)
    print ("direction: ",direction)
    print ("pointing: ",pointing)
    foe.forward(50)
    foex = RoundToNearest(foe.xcor(), 50)
    foey = RoundToNearest(foe.ycor(), 50)
    foe.goto(foex,foey)
    if (foex,foey) in tronpast:
      print ("Foe crashed into a wall!\nRestart?(y/n)")
      restart = input()
      if restart == "y":
        tron.goto(0,0)
        tron.clear()
        foe.goto(0,100)
        foe.clear()
        print ("~~~~~~~~~~~~~~~  RESTART GAME  ~~~~~~~~~~~~~~~~")
        tronpast = []
      else:
        loop = False
    
    tronpast.append((foex,foey))
    print ('Foe at',foex,",",foey)

main()
print ("exiting")
exit()

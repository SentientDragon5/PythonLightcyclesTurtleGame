import turtle
from random import randint
turtle.bgcolor("black")

def init():
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
  #tron initialize
  tron = turtle.Turtle()
  tron.down()
  tron.color('blue')
  tron.goto(0,0)
  tron.clear()
  tronlog = True
  tronpast = [(0,0)]
  foe = turtle.Turtle()
  foe.goto(0,100)
  foe.clear()
  foe.down()
  foe.color('red')
  
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

    rotate = randint(1,3)
    direction = 0
    foeforward = False
    if rotate == (1):
      direction = randint(1,2)
      if direction == (1):
        foe.left(45)
      elif direction == (2):
        foe.right(45)
    print ("rotate: ",rotate)
    print ("direction: ",direction)
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

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
  tronlog = True
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
          print ("~~~~~~~~~~~~~~~  RESTART GAME  ~~~~~~~~~~~~~~~~")
          tronpast = []
        else:
          loop = False
    if tronlog == True:
      tronpast.append((tronx,trony))
    print ('at',tronx,",",trony)
    #foe turn

main()
print ("exiting")
exit()

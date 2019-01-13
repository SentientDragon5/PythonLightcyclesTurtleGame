import turtle
import time
from random import randint

turtle.bgcolor("black")

# Init
def init():
  introQuest = input("Welcome to TRON! \n press ENTER to start game \n press H for help\n")
  if introQuest == "h":
    print ("\n press enter to move forward \n press a to turn left \n press d to turn right \n press q to turn off trail \n press e to turn on trail \n press o to restart game \n press p to quit game") 
    returnoutput = False
  elif introQuest == "f":
    returnoutput = True
  print ("Let the games...")
  time.sleep(0.16)
  print ("BEGIN")
  

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

def EndGame(Winner, Loser, askForRestart):
  
  if askForRestart == True:
    restart = input()
    print (Loser, " crashed into a wall! ",Winner," wins!\nRestart?(y/n)")
    if restart == "y":
      print ("~~~~~~~~~~~~~~~  RESTART GAME  ~~~~~~~~~~~~~~~~")
      user.goto(0,0)
      program.goto(0,0)
      user.clear()
      program.clear()
      lightWall = []
    else:
      print ("Exiting...")
      time.sleep(0.15)
      loop = False

def main():
  init()
  #Alan Bradley
  #user initialize
  user = turtle.Turtle()
  user.down()
  user.color('white')
  user.goto(0,0)
  userlog = (1)
  lightWall = [(0,0)]
  #program initialize
  program = turtle.Turtle()
  program.down()
  program.color('red')
  program.goto(100,0)
  program.clear()

  #game begin
  loop = True;
  while loop == True:
    quest = input()
    forward = (0)
    if quest == "w":
      forward = (1)
    elif quest == "a":
      forward = (1)
      user.left(45)
    elif quest == "d":
      forward = (1)
      user.right(45)
    elif quest == "q":
      user.up()
      print ("up")
      userlog = (0)
    elif quest == "e":
      user.down()
      print ("down")
      userlog = (1)
    elif quest == "o":
      EndGame()
    elif quest == "p":
      print ("exit")
      loop = False
    elif quest == "":
      forward = (1)
    else:
      print ("invalid")

    if forward == (1):
      user.forward(50)

    userx = RoundToNearest(user.xcor(), 50)
    usery = RoundToNearest(user.ycor(), 50)

    if forward == (1):
      user.goto(userx,usery)

    if (userx,usery) in lightWall:
      
      EndGame("Foe","User",True)
    
    if userlog == (1):
      lightWall.append((userx,usery))
    print ('You are at',userx,",",usery)
    
    #program turn
    
    direction = randint(1,3)
    forward = (0)
    if direction == (1):
      program.left(45)
      
    elif direction == (2):
      program.right(45)
      
    program.forward(50)
    programx = RoundToNearest(program.xcor(), 50)
    programy = RoundToNearest(program.ycor(), 50)
    program.goto(programx,programy)
      
    
    print ('Foe is at',programx,",",programy)
    if (programx,programy) in lightWall:

      EndGame("User","Foe",True)
      
    lightWall.append((userx,usery))

    print(lightWall)


#    if returnoutput == True:
#      print(lightWall)
#      print(direction)
#Start
main()
exit()

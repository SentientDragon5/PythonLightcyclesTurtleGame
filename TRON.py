import turtle
turtle.bgcolor("black")

# Init
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
  tronlog = (1)
  tronpast = [(0,0)]

  #game begin
  loop = True;
  while loop == True:
    quest = input()
    forward = (0)
    if quest == "w":
      forward = (1)
    elif quest == "a":
      forward = (1)
      tron.left(45)
    elif quest == "d":
      forward = (1)
      tron.right(45)
    elif quest == "q":
      tron.up()
      print ("up")
      tronlog = (0)
    elif quest == "e":
      tron.down()
      print ("down")
      tronlog = (1)
    elif quest == "o":
      tron.goto(0,0)
      tron.clear()
      print ("~~~~~~~~~~~~~~~  RESTART GAME  ~~~~~~~~~~~~~~~~")
      tronpast = []
    elif quest == "p":
      print ("exit")
      loop = False
    elif quest == "":
      forward = (1)
    else:
      print ("invalid")

    if forward == (1):
      tron.forward(50)

    tronx = RoundToNearest(tron.xcor(), 50)
    trony = RoundToNearest(tron.ycor(), 50)

    if forward == (1):
      tron.goto(tronx,trony)


    if (tronx,trony) in tronpast:
      print ("you crashed into a wall!\nRestart?(y/n)")
      restart = input()
      if restart == "y":
        tron.goto(0,0)
        tron.clear()
        print ("~~~~~~~~~~~~~~~  RESTART GAME  ~~~~~~~~~~~~~~~~")
        tronpast = []
    if tronlog == (1):
      tronpast.append((tronx,trony))
    print ('at',tronx,",",trony)
    print (tronpast)


#Start
main()
exit()

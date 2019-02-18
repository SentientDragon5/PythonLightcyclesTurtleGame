import turtle
from random import randint
grestart = True
turtle.bgcolor("black")
startScreen = turtle.Turtle()
startScreen.hideturtle()
startScreen.color('white')
pen = turtle.Turtle()
pen.hideturtle()
gOutput = False#Change for outputs
def printText(inStr,size,startx,starty,output,color):
    #START SPOT
    x = startx
    y = starty
    #RENDER INIT
    pen.color(color)
    skip = False
    placeAt = {'x':x,'y':y,'size':size}
    lettLoop = 1
    #STRING PREP
    myStr = []
    for c in range(0,len(inStr),1):
        myStr.append(inStr[c])
    outList = []
    #LOOP
    for char in myStr:
        letter = {' ':[]}
        #A-Z
        letter['a'] = [("l"),(x,y - size*1),(x + size*2,y - size*1),(x + size*2,y - size*4),(x,y - size*4),(x,y - size*2),(x + size*2,y - size*2)]
        letter['b'] = [("l"),(x,y),(x,y - size*4),(x + size*2,y - size*4),(x + size*2,y - size*2),(x,y - size*2)]
        letter['c'] = [("l"),(x + size*2,y - size*2),(x,y - size*2),(x,y - size*4),(x + size*2,y - size*4)]
        letter['d'] = [("l"),(x + size*2,y),(x + size*2,y - size*4),(x,y - size*4),(x,y - size*2),(x + size*2,y - size*2)]
        letter['e'] = [("l"),(x + size*2,y - size*4),(x,y - size*4),(x,y - size*2),(x + size*2,y - size*2),(x + size*2,y - size*3),(x,y - size*3)]
        letter['f'] = [("l"),(x + size,y - size*4),(x + size,y),(x + size*2,y),(x + size*2,y - size*1),("l"),(x + size*2,y - size*2),(x,y - size*2)]
        letter['g'] = [("l"),(x,y - size*4),(x + size*2,y - size*4),(x + size*2,y - size*1),(x,y - size*1),(x,y - size*3),(x + size*2,y - size*3)]
        letter['h'] = [("l"),(x + size*2,y - size*4),(x + size*2,y - size*2),(x,y - size*2),(x,y - size*4),(x,y)]
        letter['i'] = [("l"),(x + size*2,y - size*4),(x,y - size*4),(x + size*1,y - size*4),(x + size*1,y - size*2),(x + size*2,y - size*2),(x,y - size*2),("l"),(x + size*1,y - size*1),("d")]
        letter['j'] = [("l"),(x + size*1,y - size*3),(x,y - size*3),(x,y - size*4),(x + size*2,y - size*4),(x + size*2,y - size*1),("l"),(x + size*2,y),("d")]
        letter['k'] = [("l"),(x,y - size*4),(x,y - size*3),(x + size*2,y - size*4),(x,y - size*3),(x + size*2,y - size*2),(x,y - size*3),(x,y)]
        letter['l'] = [("l"),(x + size*1,y - size*4),(x + size*1,y)]
        letter['m'] = [("l"),(x,y - size*1),(x,y - size*4),(x,y - size*2),(x + size*2,y - size*2),(x + size*2,y - size*4),("l"),(x + size,y - size*2),(x + size,y - size*4)]
        letter['n'] = [("l"),(x,y - size*1),(x,y - size*4),(x,y - size*2),(x + size*2,y - size*2),(x + size*2,y - size*4)]
        letter['o'] = [("l"),(x,y - size*2),(x + size*2,y - size*2),(x + size*2,y - size*4),(x,y - size*4),(x,y - size*2)]
        letter['p'] = [("l"),(x,y - size*4),(x,y),(x + size*2,y),(x + size*2,y - size*2),(x,y - size*2)]
        letter['q'] = [("l"),(x + size*2,y - size*4),(x + size*2,y),(x,y),(x,y - size*2),(x + size*2,y - size*2)]
        letter['r'] = [("l"),(x,y - size*4),(x,y - size*2),(x,y - size*3),(x + size*2,y - size*2)]
        letter['s'] = [("l"),(x + size*2,y - size*2),(x,y - size*2),(x + size*2,y - size*4),(x,y - size*4)]
        letter['t'] = [("l"),(x + size,y - size*4),(x + size,y),("l"),(x + size*2,y - size*2),(x,y - size*2)]
        letter['u'] = [("l"),(x,y - size*2),(x,y - size*4),(x + size*2,y - size*4),(x + size*2,y - size*2)]
        letter['v'] = [("l"),(x,y - size*2),(x + size,y - size*4),(x + size*2,y - size*2)]
        letter['w'] = [("l"),(x,y - size*2),(x,y - size*4),(x + size*2,y - size*4),(x + size*2,y - size*2),("l"),(x + size,y - size*4),(x + size,y - size*2)]
        letter['x'] = [("l"),(x + size*2,y - size*4),(x,y - size*2),("l"),(x,y - size*4),(x + size*2,y - size*2)]
        letter['y'] = [("l"),(x,y),(x,y - size*2),(x + size*2,y - size*2),(x + size*2,y),(x + size*2,y - size*4),(x + size,y - size*4)]
        letter['z'] = [("l"),(x,y - size*2),(x + size*2,y - size*2),(x,y - size*4),(x + size*2,y - size*4)]
        #OTHER CHARS
        letter['`'] = [("ENTER")]
        #RENDER
        for num in letter[char]:
            if skip == True:
                pen.up(); pen.goto(num); pen.down()
            skip = False
            if num == "d":
                pen.dot(size/2)
                skip = True
            if num == "ENTER":
                y -= size *6
                x = startx - (size *3)
                skip = True
            if num == "l":
                skip = True
            elif num == "d":
                skip = False
            elif num == "ENTER":
                skip = False
            else:
                pen.goto(num)
            if output == True:
                outList.append(num)
        x += size *3
        lettLoop += 1
    if output == True:
        outList.append(myStr)
        return outList
    else:
        return ()
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
  printText('press enter to start game',4,-150,-20,False,'cyan')
  introQuest = input("Welcome to TRON! \n press ENTER to start game \n press H for help\n")
  if introQuest == "h":
    print ("\n press enter to move forward \n press a to turn left \n press d to turn right \n press q to turn off trail \n press e to turn on trail \n press o to restart game \n press p to quit game \n on game launch press r to  get variable output \n")
    return False
  elif introQuest == "r":
    return True
    print ("RETURN ON")
def dotBack():
  grid = turtle.Turtle();grid.hideturtle();grid.up();grid.color('cyan');grid.goto(0,0);
  ready = turtle.Turtle();ready.hideturtle();ready.up();ready.color('blue');ready.goto(300,-300);ready.dot(50)
  for gridx in range(-300,300,50):
      for gridy in range(-300,300,50):
          grid.goto(gridx,gridy);grid.dot(5);
  ready.clear()
def border():
  border = turtle.Turtle();border.hideturtle();border.up();border.color('cyan');border.goto(-300,-300);border.down();
  border.goto(-300,250);border.goto(250,250);border.goto(250,-300);border.goto(-300,-300);

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
  turnCounter = 1
  grestart = True
  gOutput = init()
  startScreen.clear()
  pen.clear()
  #dotBack() #Change For dotted Background!
  border()
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
  for m in range(-300,250,50):
    tronpast.append((-300,m))
  for m in range(-300,250,50):
    tronpast.append((m,250))
  for m in range(250,-300,-50):
    tronpast.append((250,m))
  for m in range(250,-300,-50):
    tronpast.append((m,-300))
  
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
        print ("~~~~~~~~~~~~~~~  RESTART GAME  ~~~~~~~~~~~~~~~~")
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
        restartyn = input()
        if restartyn == "y":
          print ("~~~~~~~~~~~~~~~  RESTART GAME  ~~~~~~~~~~~~~~~~")
        else:
          loop = False
          grestart = False
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
             AIchoice = ( "not left, pointing: ", pointing)
             foeLeft = False
        if tempPoint == 'f':
           if (foex + 50,foey) in tronpast:
             AIchoice = ( "not forward, pointing: ", pointing)
             foeForward = False
        if tempPoint == 'r':
           if (foex + 50,foey - 50) in tronpast:
             AIchoice = ( "not right, pointing: ", pointing)
             foeRight = False
    
    if pointing == 45:
        if tempPoint == 'l':
           if (foex + 50,foey) in tronpast:
             AIchoice = ( "not left, pointing: ", pointing)
             foeLeft = False
        if tempPoint == 'f':
           if (foex - 50,foey - 50) in tronpast:
             AIchoice = ( "not forward, pointing: ", pointing)
             foeForward = False
        if tempPoint == 'r':
           if (foex - 50,foey) in tronpast:
             AIchoice = ( "not right, pointing: ", pointing)
             foeRight = False
             
    if pointing == 90:
        if tempPoint == 'l':
           if (foex + 50,foey - 50) in tronpast:
             AIchoice = ( "not left, pointing: ", pointing)
             foeLeft = False
        if tempPoint == 'f':
           if (foex,foey - 50) in tronpast:
             AIchoice = ( "not forward, pointing: ", pointing)
             foeForward = False
        if tempPoint == 'r':
           if (foex - 50,foey - 50) in tronpast:
             AIchoice = ( "not right, pointing: ", pointing)
             foeRight = False
             
    if pointing == 135:
        if tempPoint == 'l':
           if (foex,foey - 50) in tronpast:
             AIchoice = ( "not left, pointing: ", pointing)
             foeLeft = False
        if tempPoint == 'f':
           if (foex - 50,foey - 50) in tronpast:
             AIchoice = ( "not forward, pointing: ", pointing)
             foeForward = False
        if tempPoint == 'r':
           if (foex - 50,foey) in tronpast:
             AIchoice = ( "not right, pointing: ", pointing)
             foeRight = False
             
    if pointing == 180:
        if tempPoint == 'l':
           if (foex - 50,foey - 50) in tronpast:
             AIchoice = ( "not left, pointing: ", pointing)
             foeLeft = False
        if tempPoint == 'f':
           if (foex - 50,foey) in tronpast:
             AIchoice = ( "not forward, pointing: ", pointing)
             foeForward = False
        if tempPoint == 'r':
           if (foex - 50,foey + 50) in tronpast:
             AIchoice = ( "not right, pointing: ", pointing)
             foeRight = False
             
    if pointing == 225:
        if tempPoint == 'l':
           if (foex - 50,foey) in tronpast:
             AIchoice = ( "not left, pointing: ", pointing)
             foeLeft = False
        if tempPoint == 'f':
           if (foex - 50,foey + 50) in tronpast:
             AIchoice = ( "not forward, pointing: ", pointing)
             foeForward = False
        if tempPoint == 'r':
           if (foex,foey + 50) in tronpast:
             AIchoice = ( "not right, pointing: ", pointing)
             foeRight = False

    if pointing == 270:
        if tempPoint == 'l':
           if (foex - 50,foey + 50) in tronpast:
             AIchoice = ( "not left, pointing: ", pointing)
             foeLeft = False
        if tempPoint == 'f':
           if (foex,foey + 50) in tronpast:
             AIchoice = ( "not forward, pointing: ", pointing)
             foeForward = False
        if tempPoint == 'r':
           if (foex + 50,foey + 50) in tronpast:
             AIchoice = ( "not right, pointing: ", pointing)
             foeRight = False
             
    if pointing == 315:
        if tempPoint == 'l':
           if (foex,foey + 50) in tronpast:
             AIchoice = ( "not left, pointing: ", pointing)
             foeLeft = False
        if tempPoint == 'f':
           if (foex + 50,foey + 50) in tronpast:
             AIchoice = ( "not forward, pointing: ", pointing)
             foeForward = False
        if tempPoint == 'r':
           if (foex + 50,foey) in tronpast:
             AIchoice = ( "not right, pointing: ", pointing)
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
    foe.forward(50)
    foex = RoundToNearest(foe.xcor(), 50)
    foey = RoundToNearest(foe.ycor(), 50)
    foe.goto(foex,foey)
    if (foex,foey) in tronpast:
      print ("Foe crashed into a wall!\nRestart?(y/n)")
      restartyn = input()
      if restartyn == "y":
          print ("~~~~~~~~~~~~~~~  RESTART GAME  ~~~~~~~~~~~~~~~~")
      else:
          loop = False
          grestart = False
    tronpast.append((foex,foey))
    print ('Foe at',foex,",",foey)
    
    if gOutput == True:
      print ("rotate: ",rotate)
      print ("direction: ",direction)
      print ("pointing: ",pointing)
      print ("Foe Left-Forward-Right: ",foeLeft,"-",foeForward,"-",foeRight)
      print ("tronpast: {",tronpast,"}\n")
      print ("turn: ", turnCounter)
      print (gOutput)
      print (grestart)
    print (AIchoice)
    if grestart == False:
        tron.hideturtle()
        foe.hideturtle()
        tron.clear()
        foe.clear()
    turnCounter += 1
while grestart == True:
    main()
print ("exiting")
exit()

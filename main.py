from turtle import *
from random import random, randint
import time

#### CLASS AND FUNCTION DEFINITIONS #####
def playing_area():
	t = Turtle()
	t.speed(0)
	t.ht()
	t.pu()
	t.goto(-250,250)
	t.color("light blue")
	t.pd()
	t.begin_fill()
	for i in range(4):
		t.forward(500)
		t.right(90)
	t.end_fill()

'''
Player() Class

Constructor( def __init__(self)):
- player should be shaped like a turtle.
- will take in the x and y coordinates for where the player will initially appear.
- will take in a color for the player
- will take in keys to turn left, turn right and shoot bullets.
- player will have an attribute that is a list that stores bullets


move(self):
- moves object forward five pixels

fire(self):
- creates a Bullet object
- appends the Bullet object to the players's bullet list
'''

class Player(Turtle):
	def __init__(self,x,y,leftkey,rightkey,firekey,bombkey,color):
		super().__init__()
		self.ht()
		self.penup()
		self.goto(x,y)
		self.speed(0)
		self.shape("turtle")
		self.color(color)
		self.bullets=[]
		self.bombs=[]
		self.leftkey=leftkey
		self.rightkey=rightkey
		self.firekey=firekey
		self.bombkey=bombkey
		self.point=0
		self.st()

	def move(self):
		self.forward(10)
	
	def right(self):
		self.right(10)
	
	def left(self):
		self.left(10)
	
	def fire(self):
		self.bullets.append(Bullet(self))
	
	def bomb(self):
		self.bombs.append(Bomb(self))

	def die(self):
		self.ht()
		kill=Turtle()
		kill.home()
		kill.ht()
		kill.speed(0)

class zombie(Turtle):
	def __init__(self,x,y,target):
		super().__init__()
		self.ht()
		self.speed(0)
		self.target = target
		self.color("green")
		self.shape("turtle")
		self.penup()
		self.goto(x,y)
		self.setheading(self.towards(self.target))
		self.st()
	
	def move(self):
		self.forward(random.randint(3,5))
		self.setheading(self.towards(self.target))
	
	def die(self):
		self.ht()
		zombies.remove(self)

'''
Bullet() Class
Constructor ( def __init__(self) ):
- Input: player object
- Attributes:
	- Position: same as player
	- Heading: same as player
	- Player: the player
 
move(self):
- move 15 or more pixels forward
- should call on the die() method when the bullet leaves the playing area

die()
- hides the object. 
- removes object from the player's bullet list
'''

class Bullet(Turtle):
    def __init__(self, player):
        super().__init__()
        self.ht()
        self.speed(0)
        self.shape("circle")
        self.pu()
        self.goto(player.xcor(),player.ycor())
        self.color(player.playercolor)
        self.setheading(player.heading())
        self.forward(15)
        self.player = player
        self.showturtle()

    def move(self):
        self.forward(10)
        if self.xcor() > 230 or self.xcor() < -230 or self.ycor() > 230 or self.ycor() < -230:
            self.kill()
    
    def kill(self):
        if self in self.player.bullets:
            self.ht()
            self.player.bullet.remove(self)

class Bomb(Turtle):
	def __init__(self,player):
		super().__init__()
		self.ht()
		self.speed(0)
		self.penup()
		self.player = player
		self.shape("circle")
		self.color(player.color()[0])
		self.goto(player.position())
		self.detonationtimer=0
		self.st()
	
	def explode(self):
		self.ht()
		self.goto(self.xcor(),self.ycor()+50)
		self.pendown()
		self.begin_fill()
		self.circle(-50)
		self.end_fill()
		self.penup()
		self.goto(self.xcor(),self.ycor()-50)
		exploded=[]
		for i in range(len(zombies)-1):
			if self.xcor()-50 < zombies[i].xcor() and self.ycor()-50 < zombies[i].ycor() and self.xcor()+50 > zombies[i].xcor() and self.ycor()+50 > zombies[i].ycor():
				exploded.append(zombies[i])
		for deadzombie in exploded:
			deadzombie.die()
		self.clear()
		self.player.bombs.remove(self)


#### DRIVER CODE ####
screen = Screen()
screen.bgcolor("black")

playing_area()
playing_area()
global p1
p1=Player(10,0,'right','left','dp','down','red')
global p2
p2=Player(10,0,'a','d','w','s','blue')

global zombies
zombies = []

prize = Turtle()
prize.ht()
prize.speed(0)
prize.penup()
prize.shape("circle")
prize.color('yellow')
prize.goto(random.randint(-200,200),random.randint(-200,200))
prize.setheading(random.randint(0,359))
prize.st()
prizesCollected = 0

alive = True
won = False

onkeypress(p1.left,p1.leftkey)
onkeypress(p1.right,p1.rightkey)
onkeypress(p1.fire,p1.firekey)
onkeypress(p1.bomb,p1.bombkey)
onkeypress(p2.left,p2.leftkey)
onkeypress(p2.right,p2.rightkey)
onkeypress(p2.fire,p2.firekey)
onkeypress(p2.bomb,p2.bombkey)
screen.listen()

while alive == True:
    player.move


screen.mainloop()

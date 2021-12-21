from turtle import Turtle

FONT_SIZE = 20

class Score(Turtle):
	
	def __init__(self):
		super().__init__()
		self.penup()
		self.hideturtle()
		self.color('white')
		self.goto(-60,300)
	
	def show_value(self, val):
		self.write(val, font=("Arial", FONT_SIZE, "normal"))
		
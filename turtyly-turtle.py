#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s, c in zip(turtle_shapes, turtle_colors):
  t = trtl.Turtle(shape=s)
  t.color(c)
  my_turtles.append(t)

    

#  
startx = 0
starty = 0
change = 45

#
for t in my_turtles:
  t.penup()
  t.goto(startx, starty)   
  t.pendown()
  t.setheading(change)
  t.forward(50)
  change -= 45
  startx = t.xcor()
  starty = t.ycor()




wn = trtl.Screen()
wn.mainloop()

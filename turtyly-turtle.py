#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl


class turtly:
    def __init__(self):
        self.my_turtles = []

        self.turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
        self.turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]
        
        for s, c in zip(self.turtle_shapes, self.turtle_colors):
            t = trtl.Turtle(shape=s)
            t.color(c)
            t.speed(10)
            self.my_turtles.append(t)
        
    def norm(self):

        startx = 0
        starty = 0
        change = 45

        

        for t in self.my_turtles:
            t.penup()
            t.goto(startx, starty)   
            t.pendown()
            t.setheading(change)
            t.forward(50)
            change -= 45
            startx = t.xcor()
            starty = t.ycor()
    
    def spiral(self):

        startx = 0
        starty = 0
        spiral_distance = 5  

        for i in range(40):  
            for t in self.my_turtles:
                t.pensize(40)
                t.penup()
                t.goto(startx, starty)
                t.pendown()
                t.right(45)  
                t.forward(spiral_distance)
                spiral_distance += 1 
                startx = t.xcor() 
                starty = t.ycor()

turts = turtly()

turts.norm()
    




wn = trtl.Screen()
wn.mainloop()

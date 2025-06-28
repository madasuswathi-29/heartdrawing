import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
pen = turtle.Turtle()
pen.color("red")
pen.pensize(2)
pen.speed(2)

# Draw heart shape
pen.begin_fill()
pen.fillcolor("red")

pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)

pen.end_fill()

# Add custom text inside the heart
pen.up()
pen.goto(-30, 130)
pen.down()
pen.color("white")
pen.write("Made with ❤️", font=("Arial", 14, "bold"))

# Hide turtle and finish
pen.hideturtle()
screen.mainloop()
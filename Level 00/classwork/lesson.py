from turtle import *
speed (30)
width(4)


# დავხაზოთ კვადრატი
color("brown")
begin_fill() # შიგნით გაფერადება
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill() # გაფერადება დასრულებულია


# კარები
forward(70)
color("gray")
begin_fill()
left(90)
forward(110) # კარების სიმაღლე
right(90)
forward(60)
right(90)
forward(110)
end_fill()

penup() # კალმის აღება
goto(200, 200)
pendown() # კალმის ჩამოღება

# სახურავი 
color("saddle brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()







exitonclick()
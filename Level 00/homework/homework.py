from turtle import *

#კვადრატი
color("brown")
begin_fill()
width(3)
speed(30)
forward(220)
left(90)
forward(220)
left(90)
forward(220)
left(90)
forward(220)
left(90)
end_fill()

#კარები
forward(80)
color("gray")
begin_fill()
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()

#სახურავი
penup()
goto(220, 220)
pendown()

color("saddle brown")
begin_fill()
right(150)
forward(220)
left(120)
forward(220)
end_fill()
 
penup()
goto(20, 140)
pendown()

#ფანჯარა
color("cyan")
begin_fill()

right(150)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)

penup()
goto(140, 140)
pendown()


#ფანჯარა 2 

left(90)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
end_fill()

exitonclick()



import turtle

# ფუნქცია სამკუთხედის დასახაზად
def draw_triangle(color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(50)
        turtle.left(120)
    turtle.end_fill()

# ფუნქცია სამკუთხედების ხატვისთვის
def draw_120_triangles():
    for i in range(1, 121):  # ინდექსები 1-დან 120-მდე
        if i % 2 == 1:  # კენტი ინდექსი
            draw_triangle("green")
        else:  # ლუწი ინდექსი
            draw_triangle("blue")
        turtle.penup()
        turtle.forward(60)  # გადადგას 60 პიქსელი შემდეგი სამკუთხედის დასახატად
        turtle.pendown()

# ტურტლის კონფიგურაცია
turtle.speed(0)
turtle.penup()
turtle.goto(-300, 0)  # კოორდინატების დაწყება მარცხნიდან
turtle.pendown()

# ფუნქციის გამოძახება
draw_120_triangles()

# ეკრანის დახურვა მომხმარებლის მხრიდან
turtle.done()

import turtle

# ფუნქცია, რომელიც გადაადგილებს კუს წინ 200 პიქსელით
def walk():
    turtle.forward(200)

# ფუნქცია, რომელიც ატრიალებს კუს და აბრუნებს უკან 200 პიქსელით
def fall_back():
    turtle.right(180)
    turtle.forward(200)

# ფუნქცია, რომელიც აერთიანებს ორივე მოქმედებას
def go_and_back():
    walk()       # კუს წინ გადაადგილება
    fall_back()  # კუს უკან დაბრუნება

# კუს ეკრანის შექმნა
screen = turtle.Screen()
screen.title("Turtle Walk and Back")

# მთავარი ფუნქციის გამოძახება
go_and_back()

# ეკრანის დახურვა მომხმარებლის მხრიდან
screen.mainloop()

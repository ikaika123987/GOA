from turtle import *

def triangle():
    for i in range(3):
        forward(50)
        left(120)
        forward(50)
        left(120)
        forward(50)

triangle()

exitonclick()




# from turtle import *

# def walk_and_back():

#     for i in range(120):
#         walk()
#         back()

# walk_and_back()
# x = 120
# exitonclick()


# from turtle import * 

# speed(10)  


# def draw_triangle(side_length):
#     for _ in range(3):
#         forward(side_length)
#         left(120)
        

# for i in range(0, 121):
#     if i % 2 != 0:  
#         begin_fill()
#         draw_triangle(i *10)  
#         penup()
#         forward(100)
#         pendown()
        
#         color('green')
       
#         end_fill()
#     else:
#        color('blue')
#        begin_fill() 
#        draw_triangle(i *10)  
#        penup()
#        forward(100)  
#        pendown()
      
       
       
#        end_fill()
# exitonclick()
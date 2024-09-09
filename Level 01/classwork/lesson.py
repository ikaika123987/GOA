name = "irakli"
#name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
# "irakli" არის ცვლადისთვის მნიშვნელობა
surname = "ozashvili"

print(name)
# print ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი

# name = "irakli" - ეს არის str(string)
#სტრინგი არის ბრჭყალებში მოქცეული სიმბოლოები

age = 15 # ეს არის int(integer) მთელი რიცხვი
height = 1.75 # ეს არის float ტიპის ცვლადი ათწილადი

knows_programming = True 
# True or false - ეს არის bool(boolean)  ტიპის ცვლადი.

#  print(type(age)) # age გადაეცა type ფუნქციას, რომელმაც დააბრუნა მისი ტიპი 
# და დაბრუნებული ნებიესმიერი სიტყვა დაპრინტეთ, რომელმაც გაგვაგებინა, რომ 
# print(type(age)) - ის ტიპი არის int(integer) -მთელი რიცხვი.

print(type(age)) 
print(type(name)) 
print(type(surname)) 
print(type(height)) 
print(type(knows_programming))

print(name + " " + surname + " " + str(age) + " " + str(knows_programming))
print(name, surname)



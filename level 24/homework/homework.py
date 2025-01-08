#split() ფუნქიცია დაწერეთ split() ფუნქციის გარეშე

sentence = "იხვის ტოლმა არ არის ბატის ტოლმა"

symbol = " "

test = ""
res = []

for i in sentence:
    if i != symbol:
        test += i
    else:
        res.append(test)
        test = ""
if test:
    res.append(test)
    
print(res)

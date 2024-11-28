def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return a / b
        else:
            return "შეუძლებელია გაყოფა ნულზე"
    else:
        return "არასწორი ოპერაცია"

# გამოყენების მაგალითები:
print(calculator(10, 5, "+"))  # 15
print(calculator(10, 5, "-"))  # 5
print(calculator(10, 5, "*"))  # 50
print(calculator(10, 0, "/"))  # "შეუძლებელია გაყოფა ნულზე"
print(calculator(10, 5, "%"))  # "არასწორი ოპერაცია"

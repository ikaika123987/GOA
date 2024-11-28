def manual_join(iterable, delimiter=""):
    result = ""  # ცარიელი სტრიქონი, რომელიც საბოლოოდ შეიქმნება
    for index, item in enumerate(iterable):
        result += str(item)  # ელემენტის დამატება
        if index < len(iterable) - 1:  # გამყოფი არ უნდა დაემატოს ბოლო ელემენტს
            result += delimiter
    return result

# გამოყენების მაგალითები:
words = ["ეს", "არის", "მაგალითი", "ტექსტი"]
print(manual_join(words, " "))  # "ეს არის მაგალითი ტექსტი"

numbers = [1, 2, 3, 4, 5]
print(manual_join(numbers, "-"))  # "1-2-3-4-5"

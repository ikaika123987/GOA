# ფუნქცია, რომელიც ითვლის ელემენტის რაოდენობას მასივში
def count_occurrences(arr, element):
    return arr.count(element)

# მაგალითი
arr = ["davit", "gio", "davit", "gio", "davit"]
element = "davit"

# შედეგის გამოტანა
count = count_occurrences(arr, element)
print(f"ელემენტი '{element}' მასივში გვხვდება {count}-ჯერ.")

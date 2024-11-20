# სია სხვადასხვა სიტყვებით
words = ["საქართველო", "მთა", "სიხარული", "გაზაფხული", "მერანი", "ცხოვრება", "პალიტრა", "მასწავლებელი", "მობილური", "ტელეფონი"]

# ხმოვნების სია
vowels = "აეიოუ"

# ხმოვნების დათვლის ფუნქცია
def count_vowels(word):
    return sum(1 for letter in word if letter in vowels)

# ხმოვნების რაოდენობა თითოეულ სიტყვაში
vowel_counts = {word: count_vowels(word) for word in words}

# შედეგის ჩვენება
for word, count in vowel_counts.items():
    print(f"{word}: {count} ხმოვანი")




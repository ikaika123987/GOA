# ხელთ არსებული წინადადება
sentence = "იხვის ტოლმა არ არის ბატის ტოლმა"

# წინადადების გაყოფა სიტყვებად (split)
words = sentence.split()

# გაყოფილი სიტყვების შეცვლა და გაერთიანება (join)
# ვცვლით "ტოლმა"-ს "საუკეთესო"-თი, და ვაერთიანებთ ტექსტს
modified_sentence = " ".join([word if word != "ტოლმა" else "საცივი" for word in words])

# შედეგის ბეჭდვა
print("შესწორებული წინადადება:")
print(modified_sentence)

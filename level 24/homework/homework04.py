# მომხმარებლის შეყვანა სიტყვების რაოდენობისთვის
count = int(input("რამდენი სიტყვა გსურთ დაამატოთ? "))

# მასივი სიტყვების შესანახად
words = []

# სიტყვების დამატება მასივში
for i in range(count):
    word = input(f"შეიყვანეთ სიტყვა {i + 1}: ")
    words.append(word)

# სიტყვების გაერთიანება (join)
result = " ".join(words)

# შედეგის გამოყვანა ტერმინალში
print("შედეგი:")
print(result)

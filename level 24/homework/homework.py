def manual_split(string, delimiter=" "):
    result = []  # შედეგების სია
    current_word = ""  # დროებითი სია თითოეული სიტყვისთვის

    for char in string:  # ვმუშაობთ სტრიქონის თითოეულ სიმბოლოზე
        if char == delimiter:  # თუ სიმბოლო არის გამყოფი
            if current_word:  # თუ დროებითი სიტყვა ცარიელი არ არის
                result.append(current_word)  # ვამატებთ სიაში
                current_word = ""  # ვცლით დროებით სიტყვას
        else:
            current_word += char  # ვამატებთ სიმბოლოს სიტყვაში

    # ბოლო სიტყვის დამატება, თუ არსებობს
    if current_word:
        result.append(current_word)

    return result

# გამოყენების მაგალითები:
text = "ეს არის მაგალითი ტექსტი"
print(manual_split(text))  # ['ეს', 'არის', 'მაგალითი', 'ტექსტი']

text_with_comma = "სახელი,გვარი,ასაკი"
print(manual_split(text_with_comma, ","))  # ['სახელი', 'გვარი', 'ასაკი']

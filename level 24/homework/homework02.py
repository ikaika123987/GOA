def manual_replace(string, old, new):
    result = ""  # საბოლოო შედეგის შესანახად
    i = 0

    while i < len(string):
        # თუ ვპოულობთ `old` სტრიქონს
        if string[i:i+len(old)] == old:
            result += new  # ვამატებთ ახალ სტრიქონს
            i += len(old)  # გადავდივართ `old`-ის სიგრძეზე
        else:
            result += string[i]  # ვამატებთ მიმდინარე სიმბოლოს
            i += 1

    return result

# გამოყენების მაგალითები:
text = "ეს არის მაგალითი ტექსტი. მაგალითი მნიშვნელოვანია."
print(manual_replace(text, "მაგალითი", "ნიმუში"))
# შედეგი: "ეს არის ნიმუში ტექსტი. ნიმუში მნიშვნელოვანია."

text2 = "abababab"
print(manual_replace(text2, "ab", "cd"))
# შედეგი: "cdcdcdcd"

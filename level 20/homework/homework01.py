# რიცხვების სია
numbers = list(range(1, 101))  # 1-დან 100-მდე რიცხვები

# 5-ისა და 3-ის ჯერადების პოვნა
multiples_of_5_and_3 = [num for num in numbers if num % 5 == 0 and num % 3 == 0]

# შედეგის ჩვენება
print("5-ისა და 3-ის ჯერადები:", multiples_of_5_and_3)

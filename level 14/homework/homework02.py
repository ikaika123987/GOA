result = 0

for i in range(5):
    num = int(input(f"გთხოვთ შეიყვანოთ ციფრი #{i + 1}: "))
    result += num  

average = result / 5

print(f"ციფრების საშუალო არითმეტიკული: {average}")

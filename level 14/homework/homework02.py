# ცვლადი შედეგის შესანახად
result = 0

# 5-ჯერ შეკითხვა მომხმარებლისგან
for i in range(5):
    num = int(input(f"გთხოვთ შეიყვანოთ ციფრი #{i + 1}: "))
    result += num  # ციფრის დამატება საბოლოო შედეგში

# საშუალო არითმეტიკული
average = result / 5

# შედეგის გამოტანა
print(f"ციფრების საშუალო არითმეტიკული: {average}")

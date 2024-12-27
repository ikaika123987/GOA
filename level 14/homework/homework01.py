start = int(input("გთხოვთ შეიყვანოთ საწყისი რიცხვი: "))
end = int(input("გთხოვთ შეიყვანოთ დასრულების რიცხვი: "))

for num in range(start, end + 1):
    if num % 2 == 0 and num % 3 == 0:
        print(f"{num} არის 3-ისა და 2-ის ჯერადი")
    else:
        print("არ არის 3-ისა და 2-ის ჯერადი ")

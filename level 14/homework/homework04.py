while True:
    num = int(input("გთხოვთ, შეიტანოთ დადებითი ციფრი: "))
    
    if num > 0:  
        print("შეკითხვა დასრულებულია.")
        break
    elif num < 0:  
        print(f"ციფრი {num} არ არის დადებითი!!!")

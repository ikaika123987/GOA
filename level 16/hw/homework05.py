# შემოიტანეთ რიცხვი მომხმარებლიდან
number = int(input("შეიყვანეთ რიცხვი: "))

# შეამოწმეთ, არის თუ არა რიცხვი 5-ის ან 10-ის ჯერადი
if number % 5 == 0 or number % 10 == 0:
    print("რიცხვი არის 5-ის ან 10-ის ჯერადი.")
else:
    print("რიცხვი არ არის 5-ის ან 10-ის ჯერადი.")

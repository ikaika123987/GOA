list_of_odd = []
list_of_even = []

for number in range(1, 1001):
    if number % 2 == 0:  # თუ რიცხვი ლუწია
        list_of_even.append(number)
    else:  # თუ რიცხვი კენტია
        list_of_odd.append(number)

# შედეგის გამოტანა
print("კენტი რიცხვები:", list_of_odd)
print("ლუწი რიცხვები:", list_of_even)

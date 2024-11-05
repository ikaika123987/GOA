# რეგისტრაცია
def registration_form():
    users = []  # რეგისტრირებული მომხმარებლები

    while True:
        name = input("შეიყვანეთ სახელი: ")
        email = input("შეიყვანეთ ელექტრონული ფოსტა: ")
        password = input("შეიყვანეთ პაროლი: ")

        users.append({
            'name': name,
            'email': email,
            'password': password
        })

        print(f"მომხმარებელი {name} წარმატებით რეგისტრირდა!")

        # კითხვას დავუსვამთ, თუ კიდევ ერთი რეგისტრაცია სურს
        another = input("გსურთ კიდევ ერთი რეგისტრაციის დამატება? (კი/არა): ").lower()
        if another != 'კი':
            break

    print("რეგისტრირებული მომხმარებლები:")
    for user in users:
        print(f"სახელი: {user['name']}, ელექტრონული ფოსტა: {user['email']}")

registration_form()




















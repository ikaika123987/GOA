# 10 ხაზის შესაქმნელად
for i in range(1, 11):
    # პირველი ნაწილის "*" -ები
    stars_left = "*" * i
    
    # სივრცეები (10 - i)
    spaces = " " * (10 - i)
    
    # მეორე ნაწილის "*" -ები
    stars_right = "*" * i
    
    # დაბეჭდვა
    print(stars_left + spaces + stars_right)

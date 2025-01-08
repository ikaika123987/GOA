st = "I am programmer"

char_for_replace = "m"

char_replace_with = "s"

res = ""

for i in st:
    if i == char_for_replace:
        i = char_replace_with
        res += i
    else:
        res += i
print(res)
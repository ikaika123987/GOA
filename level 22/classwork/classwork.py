#list_of_odd = []
#list_of_even = []
# classwork 1 დან 1000 მდე ციფრები გვაქვს შემდეგ ამ ციფრებიდან გამომიტანეთ კენტიც და ლუწი


list_of_odd = []
list_of_even = []

for i in range(1, 1001):
    if i % 2 == 0:
        list_of_even.append(i)
    else:
        list_of_odd.append(i)

print(list_of_odd)

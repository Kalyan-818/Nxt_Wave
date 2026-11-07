a = input()
list_1 = []

for char in a:
    list_1 +=[char]


for i in range(len(list_1)):
    for j in range(i+1,len(list_1)):
        if list_1[i] == list_1[j]:
            print(list_1[i])
            break
        else:
            continue
    break
list_1 = input().split()
list_2 = input().split()
intersection = []
for i in list_1:
    for j in list_2:
        if i == j:
            intersection += [int(i)]
print(intersection)
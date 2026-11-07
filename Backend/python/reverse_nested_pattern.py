n = int(input())
for i in range(1,n+1):
    row = ""
    seq_num = n
    while seq_num >= i:
        row = row + str(seq_num)
        seq_num = seq_num - 1
    print(row)
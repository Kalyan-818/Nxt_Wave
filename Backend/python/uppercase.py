a = input()
s = ""
for char in a:

    if char == " ":
        break
    b = char.upper()
    s = s + b
c = len(s)

print(s + a[c:])
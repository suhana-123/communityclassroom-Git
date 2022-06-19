n = input()
string = input()
s = string.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    if char not in s:
        print("NO")
        break

else:
    print("YES")
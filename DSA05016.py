ug = [1]
i = 0
while len(ug) <= 10000:
    if ug[i] * 2 not in ug:
        ug.append(ug[i] * 2)
    if ug[i] * 3 not in ug:
        ug.append(ug[i] * 3)
    if ug[i] * 5 not in ug:
        ug.append(ug[i] * 5)
    i += 1
ug.sort(reverse=False)
print(*ug)
t = int(input())
for x in range(t):
    n = int(input())
    print(ug[n - 1])

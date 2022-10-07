tc = int(input())
for t in range(tc):
    n = int(input())
    for i in range(1, n + 1):
        print(bin(i)[2::], end=' ')
    print()

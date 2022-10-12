tc = int(input())
for t in range(tc):
    q = []
    n = int(input())
    for i in range(n):
        a = [int(x) for x in input().split()]
        if a[0] == 1:
            print(len(q))
        elif a[0] == 2:
            if len(q) == 0:
                print("YES")
            else:
                print("NO")
        elif a[0] == 3:
            q.append(a[1])
        elif a[0] == 4:
            if len(q) != 0:
                q = q[1::]
        elif a[0] == 5:
            if len(q) != 0:
                print(q[0])
            else:
                print(-1)
        elif a[0] == 6:
            if len(q) != 0:
                print(q[-1])
            else:
                print(-1)

def schnekel(x:int, y:int):
    total = x * y
    a = [[0] * x for _ in range(y)]

    counter(total, a, x, y)


def counter(total, a, x, y):
    num = 0
    for _ in range(x):
        num = _ + 1
        a[0][_] = num
    c = x - 1
    l = 0
    y -= 1
    x -= 1
    while total != num:
        for _ in range(y):
            if num == total:
                break
            l += 1
            num += 1
            a[l][c] = num
        for _ in range(x):
            if num == total:
                break
            c -= 1
            num += 1
            a[l][c] = num
        for _ in range(y-1):
            if num == total:
                break
            l -= 1
            num += 1
            a[l][c] = num
        for k in range(x-1):
            if num == total:
                break
            c += 1
            num += 1
            a[l][c] = num
        x -= 2
        y -= 2

    print_schnekel(a)


def print_schnekel(a):
    for i in a:
        for j in i:
            print(j, end=' ')
        print()


schnekel(10, 10)

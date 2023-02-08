def snowball(n, k):
    base = 0.5
    r = n / 2
    for x in range(n):
        print(k * " ", end="")
        for y in range(n):
            if (x + base - r) ** 2 + (y + base - r) ** 2 <= r ** 2:
                print("#", end="")
            else:
                print(" ", end="")
        print()


def snowman(n):
    snowball(n, 2)
    snowball(n + 2, 1)
    snowball(n + 4, 0)

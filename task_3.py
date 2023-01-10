def envelope(n):
    print((2 * n + 1) * "*")
    for i in range(n - 1):
        print("*" + i * " " + "*" + ((2 * n + 1) - (4 + 2 * i)) * " " + "*" + i * " " + "*")
    print("*" + (2 * n - 2) // 2 * " " + "*" + (2 * n - 2) // 2 * " " + "*")
    for i in range(n - 1):
        print("*" + (n - 1 - i - 1) * " " + "*" + (2 * i + 1) * " " + "*" + (n - 1 - i - 1) * " " + "*")
    print((2 * n + 1) * "*")

envelope(4)

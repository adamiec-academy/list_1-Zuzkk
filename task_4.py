def snowball(n, k):
    for i in range(n // 2):
        print(k * " " + (n // 2 - 1 - i) * " " + (n - 2 * (n // 2 - 1 - i)) * "#" + (n // 2 - 1 - i) * " ")
    print(k * " " + n * "#")
    for i in range(n // 2):
        print(k * " " + i * " " + (n - 2 * i) * "#" + i * " ")

def snowman(n):
    snowball(n, 2)
    snowball(n + 2, 1)
    snowball(n + 4, 0)
    
snowman(7)

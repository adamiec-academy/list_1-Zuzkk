def cross(n):
    for i in range(n):
        print(n * " ", n * "*", n * " ", sep = "")
    for i in range(n):
        print(n * "*", n * "*", n * "*", sep = "")
    for i in range(n):
        print(n * " ", n * "*", n * " ", sep = "")

cross(4)

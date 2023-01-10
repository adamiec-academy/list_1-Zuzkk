def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

def report():
    n = 100
    for i in range(n + 1):
        number = len(str(factorial(i)))
        print(f"{i : >3}! is {number : >3} digits long")

report()

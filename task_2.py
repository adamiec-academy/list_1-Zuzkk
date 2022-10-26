def chess_board(n,k):
    for h in range (n):
        for i in range(k):
            for j in range (2 * n):
                if j % 2 == 0:
                    print(k*" ", end="")
                else:
                    print(k*"#", end="")
            print()
        for i in range(k):
            for j in range (2 * n):
                if j % 2 != 0:
                    print(k*" ", end="")
                else:
                    print(k*"#", end="")
            print()

chess_board(4,2)

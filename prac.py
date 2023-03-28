a, b = map(int, input().split())

while True:
    if a > 1 and a < 10 and b > 1 and b < 10:
        if a > b:
            for i in range(1, 10):
                for j in range(a, b-1, -1):
                    print(f"{j} * {i} = {i*j:>2}", end="   ")
                print()
            break
        else:
            for i in range(1, 10):
                for j in range(a, b+1):
                    print(f"{j} * {i} = {i*j:>2}", end="   ")
                print()
            break
    else:
        print("INPUT ERROR!")
        a, b = map(int, input().split())

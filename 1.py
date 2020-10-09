import time


def next_random_number(x, a, c, m):
    return (a * x + c) % m


def generate_sequence(n):
    m = 2 ** 21 - 1
    a = 8 ** 3
    c = 144
    x0 = 3
    x = x0
    for i in range(1, n + 1):
        # x = int(round(time.time() * 1000) + x) % m
        x = next_random_number(x, a, c, m) % 100
        yield x
        if x == x0:
            print("Period " + str(i))
            break


def print_and_save(n, file_name):
    with open(file_name, "w") as f:
        for i in generate_sequence(n):
            print(i)
            f.write(str(i) + "\n")


n = int(input("n = "))
print_and_save(n, "text.txt")
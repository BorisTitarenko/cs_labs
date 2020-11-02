import time


def next_random_number(x, a, c, m):
    return (a * x + c) % m


def generate_sequence(n):
    m = 2 ** 21 - 1
    a = 8 ** 3
    c = 144
    x = 3
    for i in range(1, n + 1):
        x = (x + int(round(time.time() * 1000))) % m
        x = next_random_number(x, a, c, m)
        yield x


def print_and_save(n, file_name):
    with open(file_name, "w") as f:
        for i in generate_sequence(n):
            print(i)
            f.write(str(i) + "\n")

if __name__ == "__main__":
    n = int(input("n = "))
    print_and_save(n, "text.txt")
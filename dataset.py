from random import randint


def make(file, n, start, stop, unique=False):
    done = {}
    while n > 0:
        x = randint(start, stop)
        if not unique or x not in done:
            file.write(str(x) + '\n')
            if unique:
                done[x] = True
            n -= 1


def worst(file, n):
    while n > 0:
        file.write(str(n) + '\n')
        n -= 1


if __name__ == '__main__':
    make(open('data_sets/data', 'w'), 100000, 0, 1000000, True)
    # worst(open('data_sets/data', 'w'), 100000)

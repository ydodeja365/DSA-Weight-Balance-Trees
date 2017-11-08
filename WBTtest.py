from Tree.WBTree import *
from time import time


def main():
    tree = WBT()
    data = open('data_sets/data')
    count = 0
    start_time = time()
    for val in data:
        tree.insert(int(val))
        count += 1
    else:
        stop_time = time()
        print('Inserted %d elements in %fs' % (count, stop_time - start_time))
    data.close()
    data = open('data_sets/data')
    start_time = time()
    for val in data:
        if not tree.present(int(val)):
            print('Search Failed')
            break
    else:
        stop_time = time()
        print('Searched %d elements in %fs' % (count, stop_time - start_time))
    data.close()


if __name__ == '__main__':
    main()

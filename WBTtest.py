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
    data = open('data_sets/data')
    start_time = time()
    for val in data:
        if tree.delete(int(val)) is None:
            print('Delete Failed')
            break
    else:
        stop_time = time()
        print('Deleted  %d elements in %fs' % (count, stop_time - start_time))
    data.close()
    tree.print_tree()


def delete_test():
    tree = WBT()
    store = []
    data = open('data_sets/data')
    for val in data:
        store.append(int(val))
        tree.insert(int(val))
    data.close()
    for i in range(len(store)):
        if tree.delete(store[i]) is None:
            print('Delete Failed')
            break
        for j in range(i + 1, len(store)):
            if not tree.present(store[j]):
                print('Delete Failed')
                break
    print(tree.root)


if __name__ == '__main__':
    # delete_test()
    main()

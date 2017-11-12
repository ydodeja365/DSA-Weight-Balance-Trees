from Tree.WBTree import *


def main(n):
    tree = WBT()
    for i in range(1, n + 1):
        tree.insert(i)
    print('Done inserting')
    for i in range(1, n + 1):
        if i != tree.kth(i).val:
            break
    else:
        print('Done kth-ing')


if __name__ == '__main__':
    main(100000)

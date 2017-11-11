from Tree.WBTree import *


def main():
    tree = WBT()
    n = 100000
    for i in range(1, n + 1):
        tree.insert(i)
    print('Done inserting')
    for i in range(1, n + 1):
        # print(tree.kth(i))
        if i != tree.kth(i).val:
            break
    else:
        print('Done kth-ing')


if __name__ == '__main__':
    main()

from Tree.WBTree import *


def main(n):
    tree = WBT()
    for i in range(1, n + 1):
        tree.insert(i)
    print(tree)
    print('Height :', tree.height())
    print('\nPre-order: ', end=' ')
    for val in tree.pre_order():
        print(val, end=' ')
    print('\nIn-order:  ', end=' ')
    for val in tree.in_order():
        print(val, end=' ')
    print('\nRin-order: ', end=' ')
    for val in tree.reverse_in_order():
        print(val, end=' ')
    print('\nPost-order:', end=' ')
    for val in tree.post_order():
        print(val, end=' ')


if __name__ == '__main__':
    main(0)

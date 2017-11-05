from WBTree import WBT


def main():
    tree = WBT()
    data = open('data')
    for val in data:
        print('\r' + val[:-1], end='')
        tree.insert(int(val))
    data.close()
    data = open('data')
    for val in data:
        if not tree.present(int(val)):
            print('\n:(')
            break
    else:
        print('\nDone')
    data.close()


if __name__ == '__main__':
    main()

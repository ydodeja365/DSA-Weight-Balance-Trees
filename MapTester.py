from time import time

import pandas as pd
from HashMaps.HashMap import *
from HashMaps.ChainedMap import *


class Passenger(Pair):
    def __init__(self, details):
        Pair.__init__(self, details[-1])
        self.details = details


def main(H):
    data = pd.read_csv('data_sets/titanic.csv')
    keys = []
    start_time = time()
    count = 0
    for index, row in data.iterrows():
        passenger = Passenger(tuple(row))
        keys.append(passenger.key)
        H.insert(passenger)
        count += 1
    else:
        stop_time = time()
        print('Inserted %d elements in %fs' % (count, stop_time - start_time))
    start_time = time()
    for key in keys:
        try:
            x = H.search(key).details
            # print(str(H.search(key).details))
        except AttributeError:
            print(key + ' not found')
    else:
        stop_time = time()
        print('Searched %d elements in %fs' % (count, stop_time - start_time))


if __name__ == '__main__':
    print('WBT HashMap')
    main(HashMap(5))
    print('SLL HashMap')
    main(ChainedHashMap(5))

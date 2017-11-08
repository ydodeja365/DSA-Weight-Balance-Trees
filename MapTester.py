import pandas as pd
from HashMaps.HashMap import *
from HashMaps.ChainedMap import *


class Passenger(Pair):
    def __init__(self, details):
        Pair.__init__(self, details[-1])
        self.details = details


def main():
    data = pd.read_csv('data_sets/titanic.csv')

    H = HashMap(20)
    keys = []
    for index, row in data.iterrows():
        passenger = Passenger(tuple(row))
        keys.append(passenger.key)
        H.insert(passenger)
    for key in keys:
        try:
            print(str(H.search(key).details[:])[1:-1])
        except AttributeError:
            print(key + ' not found')


if __name__ == '__main__':
    main()

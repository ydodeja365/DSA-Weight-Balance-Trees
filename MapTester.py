from HashMap import *


class Passenger(Pair):
    def __init__(self, details):
        Pair.__init__(self, details[-1])
        self.details = details

def main():
    data = open('dataset.csv')
    H = HashMap(20)
    keys = []
    passenger = None
    for line in data:
        passenger = Passenger(tuple(line.split(',')[1:]))
        keys.append(passenger.key)
        H.insert(passenger)
    for key in keys:
        try:
            print(H.search(key).details[5])
        except:
            print(key + ' not found')


if __name__ == '__main__':
    main()

from HashMap import *
# from ChainedMap import *
import pandas as  pd
class Passenger(Pair):
    def __init__(self, details):
        Pair.__init__(self, details[-1])
        self.details = details

def main():
    # data = open('dataset.csv')
    data=pd.read_csv('dataset.csv')
     
    H = HashMap(20)
    keys = []
    passenger = None
    for index,row in data.iterrows():
        passenger = Passenger(tuple(row))
        keys.append(passenger.key)
        H.insert(passenger)
    for key in keys:
        try:
            print(str(H.search(key).details[:])[1:-1])
        except:
            print(key + ' not found')


if __name__ == '__main__':
    main()

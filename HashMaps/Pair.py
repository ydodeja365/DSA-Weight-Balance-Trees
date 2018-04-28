class Pair:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __le__(self, other):
        return self.key <= other.key

    def __lt__(self, other):
        return self.key < other.key

    def __ne__(self, other):
        return self.key != other.key

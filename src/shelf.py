class Shelf:
    def __init__(self, name):
        self.name = name
        self.count = 0

    def add(self, n=1):
        self.count += n

    def remove(self, n=1):
        self.count = max(0, self.count - n)

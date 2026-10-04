from src.shelf import Shelf

LOW_STOCK = 3


def low_shelves(shelves):
    return [s.name for s in shelves if s.count <= LOW_STOCK]

from src.shelf import Shelf


def test_double_removal_stops_at_zero():
    shelf = Shelf("pantry")
    shelf.remove()
    shelf.remove()
    assert shelf.count == 0

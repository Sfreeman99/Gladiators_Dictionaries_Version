import core


def test_new_gladiator():
    assert core.new_gladiator(15, 0, 1, 5) == {
        'health': 15,
        'rage': 0,
        'damage low': 1,
        'damage high': 5
    }
    assert core.new_gladiator(100, 100, 0, 0) == {
        'health': 100,
        'rage': 100,
        'damage low': 0,
        'damage high': 0
    }
    assert core.new_gladiator(100, 0, 0, 0) == {
        'health': 100,
        'rage': 0,
        'damage low': 0,
        'damage high': 0
    }
    assert core.new_gladiator(0, 100, 0, 0) == {
        'health': 0,
        'rage': 100,
        'damage low': 0,
        'damage high': 0
    }
    assert core.new_gladiator(0, 0, 100, 0) == {
        'health': 0,
        'rage': 0,
        'damage low': 100,
        'damage high': 0
    }
    assert core.new_gladiator(0, 0, 0, 100) == {
        'health': 0,
        'rage': 0,
        'damage low': 0,
        'damage high': 100
    }
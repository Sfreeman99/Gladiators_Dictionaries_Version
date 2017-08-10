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


def test_is_dead():
    assert core.is_dead({
        'health': 10,
        'rage': 0,
        'damage low': 0,
        'damage high': 0
    }) == False
    assert core.is_dead({
        'health': 0,
        'rage': 0,
        'damage low': 0,
        'damage high': 0
    }) == True
    assert core.is_dead({
        'health': -10,
        'rage': 0,
        'damage low': 0,
        'damage high': 0
    }) == True


def test_heal_with_less_than_100():
    assert core.heal({
        'health': 90,
        'rage': 20,
        'damage low': 10,
        'damage high': 15
    }) == {
        'health': 95,
        'rage': 10,
        'damage low': 10,
        'damage high': 15
    }


def test_heal_with_100():
    assert core.heal({
        'health': 100,
        'rage': 20,
        'damage low': 10,
        'damage high': 15
    }) == 'MAX HEALTH!!'


def test_heal_with_not_enough_rage():
    assert core.heal({
        'health': 90,
        'rage': 5,
        'damage low': 10,
        'damage high': 15
    }) == 'NOT ENOUGH RAGE!!'


def test_heal_with_99_health():
    core.heal({
        'health': 99,
        'rage': 20,
        'damage low': 10,
        'damage high': 15
    }) == {
        'health': 106,
        'rage': 10,
        'damage low': 10,
        'damage high': 15
    }
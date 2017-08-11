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
    }) == 'Success'


def test_heal_with_100():
    assert core.heal({
        'health': 100,
        'rage': 20,
        'damage low': 10,
        'damage high': 15
    }) == 'Full Health'


def test_heal_with_not_enough_rage():
    assert core.heal({
        'health': 90,
        'rage': 5,
        'damage low': 10,
        'damage high': 15
    }) == 'Insufficient Rage'


def test_heal_with_99_health():
    glad = {'health': 99, 'rage': 20, 'damage low': 10, 'damage high': 15}
    core.heal(glad)
    assert glad['health'] == 100
    assert glad['rage'] == 10


def test_heal_with_96_health():
    glad = {'health': 96, 'rage': 20, 'damage low': 10, 'damage high': 15}
    core.heal(glad)
    assert glad['health'] != 101
    assert glad['rage'] == 10


def test_regular_attack():
    attacker = {'health': 100, 'rage': 0, 'damage low': 20, 'damage high': 20}
    defender = {'health': 100, 'rage': 1, 'damage low': 1, 'damage high': 1}
    attacker, defender = core.attack(attacker, defender)
    assert defender['health'] == 80
    assert attacker['rage'] == 15
    attacker = {
        'health': 100,
        'rage': 100,
        'damage low': 20,
        'damage high': 20
    }
    defender = {'health': 100, 'rage': 1, 'damage low': 1, 'damage high': 1}
    attacker, defender = core.attack(attacker, defender)
    assert defender['health'] == 60
    assert attacker['rage'] == 0
    attacker = {'health': 80, 'rage': 50, 'damage low': 10, 'damage high': 20}
    defender = {'health': 80, 'rage': 1, 'damage low': 1, 'damage high': 1}
    start_rage = attacker['rage']
    start_health = defender['health']
    attacker, defender = core.attack(attacker, defender)
    assert defender['health'] < start_health
    assert attacker['rage'] == 65 or attacker['rage'] == 0

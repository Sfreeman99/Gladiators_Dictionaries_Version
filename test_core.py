import core
import random


def test_new_gladiator():
    assert core.new_gladiator(15, 0, 1, 5, 'bloop') == {
        'name': 'bloop',
        'health': 15,
        'rage': 0,
        'damage low': 1,
        'damage high': 5,
        'blocking': False,
        'dodging': False,
        'healing': 'healing',
        'attacking': 'attacking'
    }
    assert core.new_gladiator(100, 100, 0, 0, 'bloop') == {
        'name': 'bloop',
        'health': 100,
        'rage': 100,
        'damage low': 0,
        'damage high': 0,
        'blocking': False,
        'dodging': False,
        'healing': 'healing',
        'attacking': 'attacking'
    }
    assert core.new_gladiator(100, 0, 0, 0, 'bloop') == {
        'name': 'bloop',
        'health': 100,
        'rage': 0,
        'damage low': 0,
        'damage high': 0,
        'blocking': False,
        'dodging': False,
        'healing': 'healing',
        'attacking': 'attacking'
    }
    assert core.new_gladiator(0, 100, 0, 0, 'bloop') == {
        'name': 'bloop',
        'health': 0,
        'rage': 100,
        'damage low': 0,
        'damage high': 0,
        'blocking': False,
        'dodging': False,
        'healing': 'healing',
        'attacking': 'attacking'
    }
    assert core.new_gladiator(0, 0, 100, 0, 'bloop') == {
        'name': 'bloop',
        'health': 0,
        'rage': 0,
        'damage low': 100,
        'damage high': 0,
        'blocking': False,
        'dodging': False,
        'healing': 'healing',
        'attacking': 'attacking'
    }
    assert core.new_gladiator(0, 0, 0, 100, 'bloop') == {
        'name': 'bloop',
        'health': 0,
        'rage': 0,
        'damage low': 0,
        'damage high': 100,
        'blocking': False,
        'dodging': False,
        'healing': 'healing',
        'attacking': 'attacking'
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
    core.attack(attacker, defender)
    assert defender['health'] == 80
    assert attacker['rage'] == 15
    attacker = {
        'health': 100,
        'rage': 100,
        'damage low': 20,
        'damage high': 20
    }
    defender = {'health': 100, 'rage': 1, 'damage low': 1, 'damage high': 1}
    core.attack(attacker, defender)
    assert defender['health'] == 60
    assert attacker['rage'] == 0
    attacker = {'health': 80, 'rage': 50, 'damage low': 10, 'damage high': 20}
    defender = {'health': 80, 'rage': 1, 'damage low': 1, 'damage high': 1}
    start_rage = attacker['rage']
    start_health = defender['health']
    core.attack(attacker, defender)
    assert defender['health'] < start_health
    assert attacker['rage'] == 65 or attacker['rage'] == 0


def test_super_heal():
    gladiator = {
        'health': 70,
        'rage': 100,
        'damage low': 20,
        'damage high': 20
    }
    phrases = [
        'This is super heal', 'Type this fast enough and you get super heal',
        'YOu GoT tO bE qUiCkeR ThaN ThAT', 'You WiLl NeVeRR GeT SupER HEaL',
        'YoU WiLl LoSe HeaLtH iF yoU do Not TypE ThiS fAsT EnoUgH',
        'You got lucky because this is an easy One',
        'How Much Wood Can A Wood Chuck CHUCK'
    ]
    assert core.super_heal(gladiator) in phrases
    gladiator = {'health': 70, 'rage': 29, 'damage low': 20, 'damage high': 20}
    assert core.super_heal(gladiator) == 'Not enough Rage...'


def test_checking_of_super_heal():
    gladiator = {
        'health': 70,
        'rage': 100,
        'damage low': 20,
        'damage high': 20
    }

    password = 'This is super heal'
    print(password)
    start = 10
    passkey = 'This is super heal'
    end = 21
    core.check_superheal(passkey, password, start, end, gladiator)
    assert gladiator['health'] == 60
    gladiator = {
        'health': 60,
        'rage': 100,
        'damage low': 20,
        'damage high': 20
    }
    password = 'This is super heal'
    passkey = 'This is Super heal'
    start = 10
    end = 20
    core.check_superheal(passkey, password, start, end, gladiator)
    assert gladiator['health'] == 50
    gladiator = {
        'health': 60,
        'rage': 100,
        'damage low': 20,
        'damage high': 20
    }
    password = 'This is super heal'
    passkey = 'This is super heal'
    start = 10
    end = 20
    core.check_superheal(passkey, password, start, end, gladiator)
    assert gladiator['health'] == 90
    assert gladiator['rage'] == 70
    gladiator = {
        'health': 80,
        'rage': 100,
        'damage low': 20,
        'damage high': 20
    }
    password = 'This is super heal'
    passkey = 'This is super heal'
    start = 10
    end = 20
    core.check_superheal(passkey, password, start, end, gladiator)
    assert gladiator['health'] == 100


def test_dodge_attack():
    defender = {'health': 60, 'rage': 100, 'damage low': 20, 'damage high': 20}
    phrases = {
        'd': 'He is attacking from the left',
        'a': 'He is attacking from the right',
        'w': 'He is attacking from below',
        's': 'He is attacking from above'
    }
    assert core.dodge_attack(defender) == phrases
    defender = {'health': 60, 'rage': 14, 'damage low': 20, 'damage high': 20}
    assert core.dodge_attack(defender) == False


def test_check_dodge():
    defender = {'health': 60, 'rage': 100, 'damage low': 20, 'damage high': 20}
    pass_amount = 3
    assert core.check_dodge_attack(
        pass_amount, defender) == ('You did not dodge!! You lose', False)

    assert defender['rage'] == 85
    pass_amount = 4
    assert core.check_dodge_attack(
        pass_amount, defender) == ('You Successfully dodged all four attacks',
                                   True)

    assert defender['rage'] == 70

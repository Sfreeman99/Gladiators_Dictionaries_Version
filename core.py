from random import randint, choice
import time


def heal(gladiator):
    if (gladiator['health'] < 100) and (gladiator['rage'] >= 10):
        gladiator['health'] += 5
        gladiator['rage'] -= 10
        if gladiator['health'] > 100:
            gladiator['health'] = 100
        return 'Success'
    elif gladiator['rage'] < 10:
        message = 'NOT ENOUGH RAGE!!'
        return 'Insufficient Rage'
    else:
        message = 'Full Health'
        return message


def is_dead(gladiator):
    if gladiator['health'] <= 0:
        return True
    return False


def attack(attacker, defender):
    attack = randint(attacker['damage low'], attacker['damage high'])
    if randint(1, 100) <= attacker['rage']:
        defender['health'] -= (2 * attack)
        attacker['rage'] = 0
        message = 'Critical Hit of {} damage'.format(attack)
    else:
        defender['health'] -= attack
        attacker['rage'] += 15
        message = 'You hit of {} damage'.format(attack)
    return message


def new_gladiator(health, rage, damage_low, damage_high, name):
    return {
        'name': name,
        'health': health,
        'rage': rage,
        'damage low': damage_low,
        'damage high': damage_high,
        'blocking': 'blocking',
        'dodging': 'dodging',
        'healing': 'healing',
        'attacking': 'attacking'
    }


def dodge_attack(defender, attacker, previous_attack):
    dodge = choice(['a', 's', 'd', 'w'])
    decision = input(
        'W = Up; S = Down; D = Left; A = Right\n Which way would you like to dodge?\n>>>'
    ).lower()
    if decision == dodge:
        defender['health'] += attack
    else:
        defender['health'] -= attack


def super_heal(gladiator):

    phrases = [
        'This is super heal',
        'Type this fast enough and you get super heal',
        'YOu GoT tO bE qUiCkeR ThaN ThAT',
        'You WiLl NeVeRR GeT SupER HEaL',
        'YoU WiLl LoSe HeaLtH iF yoU do Not TypE ThiS fAsT EnoUgH',
        'You got lucky because this is an easy One',
    ]
    password = choice(phrases)
    print(password)
    start = time.time()
    passkey = input()
    end = time.time()

    if (end - start < 10) and (passkey == password) and (gladiator['rage'] >=
                                                         30):
        gladiator['rage'] -= 30
        gladiator['health'] += 30
        if gladiator['health'] > 100:
            gladiator['health'] = 100
        message = 'You Healed for 30 points'
    else:
        gladiator['health'] -= 10
        gladiator['rage'] -= 30
        message = 'You lost 10 Health'
    return message
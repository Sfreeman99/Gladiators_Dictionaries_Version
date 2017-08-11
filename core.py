from random import randint


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
        'damage high': damage_high
    }

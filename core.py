import random
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
    attack = random.randint(attacker['damage low'], attacker['damage high'])
    if random.randint(1, 100) <= attacker['rage']:
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
        'blocking': False,
        'dodging': False,
        'healing': 'healing',
        'attacking': 'attacking'
    }


def dodge_attack(defender):
    # has to be able to dodge 4 times
    phrases = {
        'd': 'He is attacking from the left',
        'a': 'He is attacking from the right',
        'w': 'He is attacking from below',
        's': 'He is attacking from above'
    }
    pass_amount = 0
    while pass_amount != 4:
        choose = random.choice(
            [phrases['d'], phrases['a'], phrases['w'], phrases['s']])
        print(choose)
        decision = phrases[input()]
        if decision == choose:
            pass_amount += 1
            message = 'You dodged the attack!! Get ready for the next one...\n'
            print(message)
        else:
            break
    if pass_amount == 4:
        defender['dodge'] = True
        message = 'You Successfully dodged all four attacks'
    else:
        defender['dodge'] = False
        message = 'You did not dodge!! You lose'
    return message

    # if the attacker misses its plus one
    #if he doesnt miss its minus one
    # has to get atleast 4 dodges for attack to miss
    # has 6 chances


def super_heal(gladiator):
    if gladiator['rage'] >= 30:
        phrases = [
            'This is super heal',
            'Type this fast enough and you get super heal',
            'YOu GoT tO bE qUiCkeR ThaN ThAT',
            'You WiLl NeVeRR GeT SupER HEaL',
            'YoU WiLl LoSe HeaLtH iF yoU do Not TypE ThiS fAsT EnoUgH',
            'You got lucky because this is an easy One',
            'How Much Wood Can A Wood Chuck CHUCK'
        ]
        password = random.choice(phrases)
        return password
    else:
        message = 'Not enough Rage...'
        return message


def check_superheal(passkey, password, start, end, gladiator):
    if (end - start <= 10) and (passkey == password):
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

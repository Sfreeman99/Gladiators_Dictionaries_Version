import core
from random import randint
from time import sleep
import time, sys
typing_speed = 12


def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)
    return print()


def shell_superheal(password):
    print(password)
    start = time.time()
    passkey = input()
    end = time.time()
    return passkey, start, end


def battle(attacker, defender):
    while True:
        decision = input(
            '{}\n----------\n[A]ttack\n[H]eal\n[S]uper Heal\n----------\n>>> '.
            format(attacker['name'])).upper().strip()
        if decision == 'A':
            attack = core.attack(attacker, defender)
            return '{}: \n{}\n'.format(attacker['name'], attack)
        elif decision == 'H':
            heal = core.heal(attacker)
            return '{}: \n{}\n'.format(attacker['name'], heal)
        elif decision == 'S':
            password = core.super_heal(attacker)
            passkey, start, end = shell_superheal(password)
            s_heal = core.check_superheal(passkey, password, start, end)
            return '{}: \n{}\n'.format(attacker['name'], s_heal)

        else:
            print('INVALID CHOICE... TRY AGAIN')


def game_play(gladiator_1, gladiator_2):
    s = '{}: {}HP|| RAGE!! {}  |||   {}:   {}HP || RAGE  {}  \n'.format(
        gladiator_1['name'], gladiator_1['health'], gladiator_1['rage'],
        gladiator_2['name'], gladiator_2['health'],
        gladiator_2['rage']).center(100)
    return s


def get_damages(a, b):
    """ num, num -> num, num """
    x, y = randint(a, b), randint(a, b)
    return min(x, y), max(x, y)


def introduce_gladiator(gladiator):
    sleep(1.5)
    slow_type('{} has a minimal damage of {} and maximum damage of {}\n'.
              format(gladiator['name'], gladiator['damage low'], gladiator[
                  'damage high']).center(100))


def winners_and_losers(dead, alive):
    print('WINNER: {}\nLOSER: {}'.format(alive['name'], dead['name']))


def main():
    print('Welcome To Gladiators!!'.center(100))
    health = 100
    rage = 0
    min_damage = 5
    max_damage = 20

    damage_low, damage_high = get_damages(min_damage, max_damage)
    gladiator_1 = core.new_gladiator(health, rage, damage_low, damage_high,
                                     'Carpophorus')

    damage_low, damage_high = get_damages(min_damage, max_damage)
    gladiator_2 = core.new_gladiator(health, rage, damage_low, damage_high,
                                     'Spartacus')

    introduce_gladiator(gladiator_1)
    introduce_gladiator(gladiator_2)
    sleep(1)
    slow_type('READY...'.center(100))
    sleep(1)
    print('FIGHT!!'.center(100))

    while True:
        print(game_play(gladiator_1, gladiator_2))
        # attacker_decision(gladiator_1)
        # defender_decision(gladiator_2)
        print(battle(gladiator_1, gladiator_2))
        sleep(1)
        print(game_play(gladiator_1, gladiator_2))
        winners_and_losers(gladiator_2, gladiator_1)
        if core.is_dead(gladiator_2):
            exit()
        print(battle(gladiator_2, gladiator_1))
        sleep(1)
        print(game_play(gladiator_1, gladiator_2))
        winners_and_losers(gladiator_1, gladiator_2)
        if core.is_dead(gladiator_1):
            exit()


def attacker_decision(gladiator):
    while True:
        decision = input(
            '{}\n----------\n[A]ttack\n[H]eal\n[S]uper Heal\n----------\n>>> '.
            format(gladiator['name'])).upper().strip()
        if decision == 'A':
            return decision
        if decision == 'H':
            return decision
        if decision == 'S':
            return decision

        else:
            print('Invalid Choice... Try again')


def defender_decision(gladiator):
    while True:
        decision = input(
            '{}\n----------\n[H]eal\n[S]uper Heal\n[D]odge\n----------\n>>> '.
            format(gladiator['name'])).upper().strip()
        if decision == 'H':
            return decision
        if decision == 'S':
            return decision
        if decision == 'D':
            return decision
        else:
            print('Invalid Choice... Please Try Again')


if __name__ == '__main__':
    main()
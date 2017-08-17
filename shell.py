import core
import random
from time import sleep
import time, sys


def slow_type(t):
    typing_speed = 12
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)
    return print()


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
            '{}\n----------\n[H]eal\n[S]uper Heal\n[D]odge\n[W]ait for your turn to attack\n----------\n>>> '.
            format(gladiator['name'])).upper().strip()
        if decision == 'H':
            return decision
        elif decision == 'S':
            return decision
        elif decision == 'D':
            gladiator['dodging'] = True
            return decision
        elif decision == 'W':
            return decision
        else:
            print('Invalid Choice... Please Try Again')


def shell_superheal(password):
    print(password)
    start = time.time()
    passkey = input()
    end = time.time()
    return passkey, start, end


def shell_dodge(password):
    lines = '\n-------------------------------------------------------\n'
    phrases = password
    pass_amount = 0
    while pass_amount != 4:
        sleep(2)
        choose = random.choice(
            [phrases['d'], phrases['a'], phrases['w'], phrases['s']])
        print(choose)
        decision = phrases[input()]
        if decision == choose:
            pass_amount += 1
            message = 'You dodged the attack!!...\n'
            print(lines + message + lines)
        else:
            break
    return pass_amount


def battle(attacker, defender, glad_1, glad_2):
    while True:
        # decision = input(
        #     '{}\n----------\n[A]ttack\n[H]eal\n[S]uper Heal\n[D]odge\n----------\n>>> '.
        #     format(attacker['name'])).upper().strip()
        if attacker == 'A':
            # hit = core.attack(attacker, defender)
            if glad_2['dodging'] == True:
                password = core.dodge_attack(glad_2)
                if password == False:
                    core.attack(glad_1, glad_2)
                    return 'Not enough Rage... You lose a turn'
                pass_amount = shell_dodge(password)
                passer = core.check_dodge_attack(pass_amount, glad_2)
                if pass_amount == 4:
                    glad_2['dodging'] = False
                    return '{} dodged {}\'s attack'.format(
                        glad_2['name'], glad_1['name'])
                else:
                    attack = core.attack(glad_1, glad_2)
                    return '{}: \n{}\n'.format(glad_1['name'], attack)
            elif glad_2['dodging'] == False:
                return '{}: \n{}\n'.format(glad_1['name'],
                                           core.attack(glad_1, glad_2))
        elif attacker == 'H':
            heal = core.heal(glad_1)
            return '{}: \n{}\n'.format(glad_1['name'], heal)
        elif defender == 'H':
            heal = core.heal(glad_2)
            return '{}: \n{}\n'.format(glad_2['name'], heal)
        elif attacker == 'S':
            password = core.super_heal(glad_1)
            if password == 'Not enough Rage...':
                return 'Not enough Rage... You lose a turn'
            else:
                passkey, start, end = shell_superheal(password)
                s_heal = core.check_superheal(passkey, password, start, end)
                return '{}: \n{}\n'.format(glad_1['name'], s_heal)
        elif defender == 'S':
            password = core.super_heal(glad_2)
            if password == 'Not enough Rage...':
                return 'Not enough Rage... You lose a turn'
            else:
                passkey, start, end = shell_superheal(password)
                s_heal = core.check_superheal(passkey, password, start, end)
                return '{}: \n{}\n'.format(glad_2['name'], s_heal)
        elif defender == 'D':
            glad_2['dodging'] = True
        elif defender == 'W':
            glad_2['rage'] += 15
            return '{} is waiting for his turn to attack..\n'

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
    x, y = random.randint(a, b), random.randint(a, b)
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
        attacker = attacker_decision(gladiator_1)
        defender = defender_decision(gladiator_2)
        print(battle(attacker, defender, gladiator_1, gladiator_2))
        # sleep(1)
        # print(game_play(gladiator_1, gladiator_2))
        # winners_and_losers(gladiator_2, gladiator_1)
        # if core.is_dead(gladiator_2):
        #     exit()
        # print(battle(gladiator_2, gladiator_1))
        # sleep(1)
        # print(game_play(gladiator_1, gladiator_2))
        # winners_and_losers(gladiator_1, gladiator_2)
        # if core.is_dead(gladiator_1):
        #     exit()


if __name__ == '__main__':
    main()
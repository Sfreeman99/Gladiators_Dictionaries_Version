import core, random, time, sys
from time import sleep

# def computer_defense():
#     decision = random.choice(['H', 'S', 'D', 'W'])
#     #Make new function for computer in core for question marks
#     if decision = 'H':
#         computer_message = ????
#     elif decision = 'H':
#         computer_message = ????
#     elif decision = 'H':
#         computer_message = ????
#     elif decision = 'H':
#         computer_message = ????
# def computer_offense():
#     #Make new function for computer in core for question marks
#     decision = random.choice(['A'])
#     if decision == 'A':
#         computer_message = ????


def slow_type(t):
    typing_speed = 12
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)
    return print()


def attacker_decision(gladiator, play_2):
    s = ''
    if play_2:
        s = 25 * ' '
    message = '\n{}Attacker:{}\n'.format(s, gladiator['name'])
    message += s + '-------------------------\n'
    message += s + '[A]ttack \n'
    message += s + '[H]eal \n'
    message += s + '[S]uper Heal\n'
    message += s + '-------------------------\n>>> '
    while True:
        decision = input(message).upper().strip()
        if decision == 'A':
            return decision
        if decision == 'H':
            return decision
        if decision == 'S':
            return decision

        else:
            print('Invalid Choice... Try again')


def defender_decision(gladiator, play_2):
    s = ''
    if play_2:
        s = 25 * ' '
    message = '\n{}Defender:{}\n'.format(s, gladiator['name'])
    message += s + '-------------------------\n'
    message += s + '[H]eal \n'
    message += s + '[S]uper Heal\n'
    message += s + '[D]odge\n'
    message += s + '[W]ait\n'
    message += s + '-------------------------\n>>> '
    while True:
        decision = input(message).upper().strip()
        if decision == 'H':
            return decision
        elif decision == 'S':
            return decision
        elif decision == 'D':
            return decision
        elif decision == 'W':
            return decision
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
    input(
        'Keys:\n W = up\n S = down\n A = left\n D = right\n You have to press the opposite for what the message says\nEx: He is attacking from the right:\n [A] would be the answer...\nPress Enter when Ready\n'
    )
    while pass_amount != 4:
        sleep(2)
        choose = random.choice(
            [phrases['d'], phrases['a'], phrases['w'], phrases['s']])
        print(choose)
        start = time.time()
        decision = phrases[input()]
        end = time.time()
        if decision == choose and (end - start < 1.5):
            pass_amount += 1
            message = 'You dodged the attack!!...\n'
            print(lines + message + lines)
        else:
            break
    return pass_amount


def battle(attacker, defender):
    attacker_message = ''
    defender_message = ''

    if (attacker['decision'] == 'A') and (defender['decision'] == 'D'):
        password = core.dodge_attack(defender)
        if not password:
            attacker_message = core.attack(attacker, defender)
            defender_message = '{} did not have enough rage to dodge. '.format(
                defender['name'])
            return '\n'.join([defender_message, attacker_message])

        pass_amount = shell_dodge(password)
        passer, dodged = core.check_dodge_attack(pass_amount, defender)
        if dodged:
            return '{} dodged {}\'s attack'.format(defender['name'],
                                                   attacker['name'])
        attack = core.attack(attacker, defender)
        attacker_message = '{}: {}'.format(attacker['name'], attack)
        defender_message = '{} did not dodge!'.format(defender['name'])
        return '\n'.join([defender_message, attacker_message])

    if attacker['decision'] == 'A':
        attacker_message = core.attack(attacker, defender)
    elif attacker['decision'] == 'H':
        heal = core.heal(attacker)
        attacker_message = '{}: \n{}\n'.format(attacker['name'], heal)
    elif attacker['decision'] == 'S':
        password = core.super_heal(attacker)
        if password == 'Not enough Rage...':
            defender_message = '{} not enough Rage to Super Heal...'.format(
                attacker['name'])
        else:
            passkey, start, end = shell_superheal(password)
            s_heal = core.check_superheal(passkey, password, start, end,
                                          attacker)
            defender_message = '{} Super healed {}...'.format(
                defender['name'], s_heal)
    if defender['decision'] == 'S':
        password = core.super_heal(defender)
        if password == 'Not enough Rage...':
            defender_message = '{} not enough Rage to Super Heal...'.format(
                defender['name'])
        else:
            passkey, start, end = shell_superheal(password)
            s_heal = core.check_superheal(passkey, password, start, end,
                                          attacker)

            defender_message = '{}: {}...'.format(defender['name'], s_heal)
    elif defender['decision'] == 'H':
        heal = core.heal(defender)
        defender_message = '{} healed {}...'.format(defender['name'], heal)
    elif defender['decision'] == 'W':
        defender['rage'] += 5
        defender_message = '{} waited and added 5 Rage...'.format(
            defender['name'])

    return '\n'.join([defender_message, attacker_message])


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
    player_1_name = input('Player 1 what is your name?\n: ').title()
    health = 100
    rage = 0
    min_damage = 5
    max_damage = 20

    damage_low, damage_high = get_damages(min_damage, max_damage)
    gladiator_1 = core.new_gladiator(health, rage, damage_low, damage_high,
                                     player_1_name)
    player_2_name = input('Player 2 what is your name?\n: ').title()
    damage_low, damage_high = get_damages(min_damage, max_damage)
    gladiator_2 = core.new_gladiator(health, rage, damage_low, damage_high,
                                     player_2_name)

    introduce_gladiator(gladiator_1)
    introduce_gladiator(gladiator_2)
    sleep(.5)
    slow_type('READY...'.center(100))
    sleep(.5)
    print('''
Attackers can:
--------------------------------------------------------------------------------------------------
[A]ttack [Regular attack]
[H]eal [Health goes up 5 points]
[S]uper Heal [if you have 30 rage and you type the passcode under 10 seconds, You get 30 Health]
--------------------------------------------------------------------------------------------------'''
          )
    sleep(.5)
    print('''
Defender: {}
--------------------------------------------------------------------------------------------------            
[H]eal [Health goes up 5 points]
[S]uper Heal [if you have 30 rage and you type the passcode under 10 seconds, You get 30 Health]
[D]odge [if you have 15 Rage you have the chance to dodge... if you can beat it]
[W]ait for your turn to attack [You wait for your turn to attack and add 5 Rage]
--------------------------------------------------------------------------------------------------'''
          )
    sleep(.5)
    print('FIGHT!!'.center(100))

    while True:
        print(game_play(gladiator_1, gladiator_2))
        gladiator_1['decision'] = attacker_decision(gladiator_1, False)
        gladiator_2['decision'] = defender_decision(gladiator_2, True)
        print(battle(gladiator_1, gladiator_2))
        sleep(1)
        print(game_play(gladiator_1, gladiator_2))
        if core.is_dead(gladiator_2):
            print(game_play(gladiator_1, gladiator_2))
            print(winners_and_losers(gladiator_1, gladiator_2))
            exit()
        gladiator_2['decision'] = attacker_decision(gladiator_2, True)
        gladiator_1['decision'] = defender_decision(gladiator_1, False)
        print(battle(gladiator_2, gladiator_1))
        sleep(1)
        if core.is_dead(gladiator_1):
            print(game_play(gladiator_1, gladiator_2))
            print(winners_and_losers(gladiator_1, gladiator_2))
            exit()


if __name__ == '__main__':
    main()
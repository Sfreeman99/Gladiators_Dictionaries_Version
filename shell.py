import core
from random import randint
print('Welcome To Gladiators!!'.center(100))
health = 100
rage = 0
damage_low = randint(1, 10)
damage_high = randint(10, 20)
gladiator_1 = core.new_gladiator(health, rage, damage_low, damage_high)
health = 100
rage = 0
damage_low = randint(1, 10)
damage_high = randint(10, 20)
gladiator_2 = core.new_gladiator(health, rage, damage_low, damage_high)

print(
    'gladiator 1: health   {} ||rage    {}  |||   gladiator 2: health   {} || rage  {}  '.
    center(100).format(gladiator_1['health'], gladiator_1['rage'], gladiator_2[
        'health'], gladiator_2['rage']))

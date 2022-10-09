from random import randrange, randint
import random


class TBattleField:
#    def __init__(self,):
    pass


class TPeople:
    def __init__(self, c):
        self.id = randint(0, 100)
        self.command = c


class TSoldiers(TPeople):
    id_ = 1

    def __init__(self):
        self.id_ = TSoldiers.id_
        TSoldiers.id_ += 1

    def go_hero(self, hero):
        print(f'Солдат {self.id_} идёт за героем {hero.id_}')

    def __str__(self):
        return f'{self.id_}'


class THeroes(TPeople):

    def __init__(self, team):
        TSoldiers.__init__(self)
        self.team = team
        self.level = 0

    def level_up(self):
        self.level += 1
        print(f'Герой {self.id_} повышен {self.level} уровня')


heroes = THeroes('red')
heroes_2 = THeroes('blue')
list_heroes = []
list_heroes_2 = []
for _ in range(50):
    if random.choice(['red', 'blue']) == 'red':
        list_heroes.append(TSoldiers())
    else:
        list_heroes_2.append(TSoldiers())

len_heroes = len(list_heroes)
len_heroes_2 = len(list_heroes_2)
print(f'У первого героя - {len_heroes} солдат')
print(f'У второго героя - {len_heroes_2} солдат')
if len_heroes > len_heroes_2:
    heroes.level_up()
else:
    heroes_2.level_up()

random.choice(list_heroes).go_hero(heroes)
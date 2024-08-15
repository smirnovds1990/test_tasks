from random import choices, randint

from toads import ArtisanToad, AssassinToad, BaseToad, RecklessToad

from constants import FIGHT_NUMBERS


TOAD_CHOICES = [ArtisanToad, AssassinToad, RecklessToad]


async def choose_toads_to_fight() -> tuple[BaseToad, BaseToad]:
    toad_classes = choices(TOAD_CHOICES, k=2)
    toad_1 = toad_classes[0]()
    toad_2 = toad_classes[1]()
    return toad_1, toad_2


async def fight(toads: tuple[BaseToad, BaseToad]) -> str:
    while toads[0].health > 0 and toads[1].health > 0:
        index = randint(0, 1)
        attacker = toads[index]
        defender = toads[1 - index]
        damage = attacker.attack()
        armor = defender.defend()
        defender.health -= (damage - armor)
    if toads[0].health <= 0:
        winner = 'Toad_2'
    else:
        winner = 'Toad_1'
    return winner


async def start_fight() -> dict[str, int]:
    victories = {'Toad_1': 0, 'Toad_2': 0}
    for _ in range(FIGHT_NUMBERS):
        toads = await choose_toads_to_fight()
        winner = await fight(toads)
        victories[winner] += 1
    return victories

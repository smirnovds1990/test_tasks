from abc import ABC
from random import randrange

from constants import (
    ARMOR_START, ARTISAN_COEFFICIENT, ASSASSIN_COEFFICIENT,
    ATTACK_DELIMETER, DEFAULT_ARMOR_LEVEL, DEFAULT_DAMAGE_LEVEL,
    DEFAULT_HEALTH_LEVEL, RECKLESS_COEFFICIENT
)


class BaseToad(ABC):

    def __init__(self):
        self.damage = DEFAULT_DAMAGE_LEVEL
        self.health = DEFAULT_HEALTH_LEVEL
        self.armor = DEFAULT_ARMOR_LEVEL

    def attack(self) -> int:
        return randrange(self.damage // ATTACK_DELIMETER, self.damage)

    def defend(self) -> int:
        return randrange(ARMOR_START, self.armor)


class AssassinToad(BaseToad):

    def __init__(self):
        super().__init__()
        self.health = round(self.health * ASSASSIN_COEFFICIENT)


class RecklessToad(BaseToad):

    def __init__(self):
        super().__init__()
        self.damage = round(self.damage * RECKLESS_COEFFICIENT)


class ArtisanToad(BaseToad):

    def __init__(self):
        super().__init__()
        self.armor = self.armor * ARTISAN_COEFFICIENT

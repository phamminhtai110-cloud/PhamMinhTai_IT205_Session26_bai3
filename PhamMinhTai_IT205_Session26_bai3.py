from abc import ABC, abstractmethod


class Champion(ABC):
    def __init__(self, champion_id, name, base_hp, base_atk):
        self.champion_id = champion_id
        self.name = name
        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self):
        pass

    def get_combat_power(self):
        return self.base_hp + self.calculate_skill_damage() * 1.5

    def __add__(self, other):
        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()
        return self.get_combat_power() + other

    def __radd__(self, other):
        return other + self.get_combat_power()

    def __gt__(self, other):
        return self.get_combat_power() > other.get_combat_power()


class Warrior(Champion):
    def __init__(self, champion_id, name, base_hp, base_atk, shield_bonus):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.shield_bonus = shield_bonus

    def calculate_skill_damage(self):
        return self.base_atk * 2 + self.shield_bonus


class Mage(Champion):
    def __init__(self, champion_id, name, base_hp, base_atk, ability_power):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.ability_power = ability_power

    def calculate_skill_damage(self):
        return self.base_atk * self.ability_power


champion_pool = [
    Warrior("WAR01", "Rikkei Knight", 1200, 300, 150),
    Warrior("WAR02", "Steel Guardian", 1500, 250, 200),
    Mage("MAG01", "Rikkei Wizard", 800, 500, 2.0)
]

c1 = champion_pool[0]
c2 = champion_pool[2]

if c1 > c2:
    print(f"{c1.name} mạnh hơn")
else:
    print(f"{c2.name} mạnh hơn")

team_power = sum(champion_pool)
print("Tổng chiến lực:", team_power)
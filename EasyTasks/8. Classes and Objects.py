class Avenger:

    def __init__(self, name, age, superpower, gender, weapon):
        self.name = name
        self.age = age
        self.superpower = superpower
        self.gender = gender
        self.weapon = weapon

    def get_info(self):
        return (f"name:{self.name},"
                f"age:{self.age}, "
                f"super:{self.superpower},"
                f"gender:{self.gender},"
                f"weapon:{self.weapon},")

    def isleader(self):
        if self.name == "Captain America":
            return f"{self.name} , is a Leader of the Avengers."
        return f"{self.name} , is not a Leader of the Avengers."


super_heroes = [
    {"name": "Captain America", "age": 100, "gender": "Male", "super_power": "Super strength", "weapon": "Shield"},
    {"name": "Iron Man", "age": 40, "gender": "Male", "super_power": "Technology", "weapon": "Armor"},
    {"name": "Black Widow", "age": 35, "gender": "Female", "super_power": "Superhuman", "weapon": "Batons"},
    {"name": "Hulk", "age": 45, "gender": "Male", "super_power": "Unlimited Strength", "weapon": "No Weapon"},
    {"name": "Thor", "age": 1500, "gender": "Male", "super_power": "Super Energy", "weapon": "Mjölnir"},
    {"name": "Hawkeye", "age": 45, "gender": "Male", "super_power": "Fighting skills", "weapon": "Bow and Arrows"}
]
# list of avenger objects
avengers = [Avenger(hero["name"], hero["age"], hero["gender"], hero["super_power"], hero["weapon"]) for hero in
            super_heroes]

for avenger in avengers:
    print(avenger.get_info())

    # Check if each Avenger is a leader or not
for avenger in avengers:
    print(avenger.isleader())

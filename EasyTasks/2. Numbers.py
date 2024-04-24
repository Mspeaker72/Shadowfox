
# 1. Write a function that takes two arguments, 145 and 'o', and
# uses the `format` function to return a formatted string. Print the
# result. Try to identify the representation used.
def create_string(char: str, num: int):
    return ("{} is a string argument and {}"
            " is an int but this formatted string is a string type.").format(char, num)


print(create_string("o", 145))

# 2. In a village, there is a circular pond with a radius of 84 meters.
# Calculate the area of the pond using the formula: Circle Area = π
# r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly
# 1.4 liters of water in a square meter, what is the total amount of
# water in the pond? Print the answer without any decimal point in
# it. Hint: Circle Area = π r^2 Water in the pond = Pond Area
# Water per Square Meter

r = 84
pi = 3.14
Area = pi * r ** 2

water_per_sq_meter = 1.4
total_water = Area * water_per_sq_meter

print(f"{int(total_water)} L")

# 3. If you cross a 490m meter long street in 7 minutes, calculate your
# speed in meters per second. Print the answer without any decimal
# point in it. Hint: Speed = Distance / Time

distance = 490
time = 7 * 60
speed = distance // time
print(f"{speed} m/s")

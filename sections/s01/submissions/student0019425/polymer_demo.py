polymers = {
    "PE": -125,
    "PS": 100,
    "PET": 70,
}
number_of_polymers = len(polymers)
print('Number of polymers =', number_of_polymers)
average_temperature = sum(polymers.values()) / len(polymers)

print('Average temperature =', average_temperature)

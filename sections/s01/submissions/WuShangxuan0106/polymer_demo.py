polymers = {
    "PE": -125,
    "PS": 100,
    "PET": 70,
}
polymer_count = len(polymers)
average_Tg = sum(polymers.values()) / len(polymers)
print(f"Number of polymers: {polymer_count}")
print(f"Average Tg: {average_Tg:.1f} C")

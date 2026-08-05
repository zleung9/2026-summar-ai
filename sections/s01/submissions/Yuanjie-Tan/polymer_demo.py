# polymer_demo.py
"""Small demonstration: average glass-transition temperature (Tg) of polymers.

Day 2 task for Section 1: create and run a simple script and notebook,
then practise debugging with the VS Code debugger.
"""

# Tiny dataset: polymer name -> glass-transition temperature Tg in Celsius
polymers = {
    "PE": -125,
    "PS": 100,
    "PET": 70,
}


def average_tg(polymer_data):
    """Return the mean glass-transition temperature of the given polymers."""
    return sum(polymer_data.values()) / len(polymer_data)


def main():
    print("Polymer glass-transition temperature (Tg) demo")
    print("-" * 45)

    num_polymers = len(polymers)
    mean_tg = average_tg(polymers)

    print(f"Number of polymers: {num_polymers}")
    for name, tg in polymers.items():
        print(f"  {name:>4}: {tg} C")
    print(f"Average Tg: {mean_tg:.1f} C")


if __name__ == "__main__":
    main()

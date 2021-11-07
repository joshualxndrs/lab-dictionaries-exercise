favorite_cars = {
    "Uncle Jeje": ["Golf", "Camry", "LFA"],
    "Nicklas": ["Innova", "Panther", "Fortuner"],
    "Andy": ["BMW M3", "Z4", "Cayman"],
    "Matt": ["GR Yaris", "Corolla", "Supra"],
    "Fitra": ["S-Class", "CLA-45-S", "Landcruiser"]
}

for name, cars in favorite_cars.items():
    print("\n" + name.title() + " likes these cars:")
    for car in cars:
        print("- " + car.title())
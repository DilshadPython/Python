"""
Demonstrates key-based sorting on complex tuple structures stored in a list.
"""

def demo_planet_sorting():
    # Format: (Name, Radius km, Density g/cm3, Distance AU)
    my_planets = [
        ('Mercury', 2440, 5.43, 0.395),
        ('Venus', 6125, 5.27, 0.723),
        ('Earth', 6325, 5.11, 1.002),
        ('Mars', 3390, 3.93, 1.524),
        ('Jupiter', 69911, 1.33, 5.204),
        ('Saturn', 58232, 0.69, 9.582),
        ('Uranus', 25362, 1.27, 19.201),
        ('Neptune', 24622, 1.64, 30.047),
    ]

    # Sort planets by radius (index 1) descending
    by_size = sorted(my_planets, key=lambda planet: planet[1], reverse=True)
    print('Planets sorted by size (Radius km, descending):')
    for p in by_size:
        print(f'  {p[0]:<10}: {p[1]} km')

    # Sort planets by distance from Sun (index 3) ascending
    by_distance = sorted(my_planets, key=lambda planet: planet[3])
    print('\nPlanets sorted by distance from Sun (AU):')
    for p in by_distance:
        print(f'  {p[0]:<10}: {p[3]} AU')

    return by_size, by_distance

if __name__ == '__main__':
    demo_planet_sorting()

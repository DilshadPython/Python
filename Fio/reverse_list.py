names = []

with open("cities.txt") as f:
    for line in f:
        names.append(line.strip())

for name in sorted(names, reverse=True):
    print(f"Hi, {name}")
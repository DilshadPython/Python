with open('names.csv') as csvfile:
    for line in csvfile:
        city, county = line.rstrip().split(',')
        print(f"{city},{county}")
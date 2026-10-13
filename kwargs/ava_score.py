def avarage_score(*scores):
    if len(scores) == 0:
        return 0
    # return sum of all divide by the len of numbers
    return sum(scores) / len(scores)

print(avarage_score(66,74, 85, 89))
print(avarage_score(95, 84, 71, 89, 69))
print(avarage_score())
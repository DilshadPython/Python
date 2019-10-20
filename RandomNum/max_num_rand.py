import random

# 10 bins in histogram
Number = 10
# repeats
Numbers = 10000
# minumum randon number
Max = 1000

hist = [0] * Number  # histogram

for _ in range(Numbers):
    ran = random.randint(0, Max - 1)
    bin = ran / (Max / Number)
    hist[int(bin)] += 1
# all bins should more or less equal
print('Result: ', hist)

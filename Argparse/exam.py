import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', default=1, help='number of times Messages')
args = parser.parse_args()

for _ in range(args.n):
    print('Messages')
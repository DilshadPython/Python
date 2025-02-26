import argparse

parser = argparse.ArgumentParser(description='Argument Parser Messages in print')
parser.add_argument('-n')
args = parser.parse_args()

for _ in range(int(args.n)):
    print('Messages')
from argparse import ArgumentParser


def avg(*args):
    return sum(args) / len(args)


parser = ArgumentParser()
parser.add_argument('--numbers', nargs='+', type=float)
args = parser.parse_args()

output = avg(*args.numbers)
print(output)

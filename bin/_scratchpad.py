import argparse

parser = argparse.ArgumentParser(
    prog='PROGRAM NAME',
    description='A foo that bars',
    epilog="And that's how you'd foo a bar")

parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum,
                    default=max, help='sum the integers (default: find the max)')

parser.add_argument('--foo', nargs='?', help='foo help')
parser.add_argument('--bar', nargs='+', help='bar help')
parser.add_argument('--foobar', nargs='*', default=[1, 2, 3], help='BAR!')

parser.add_argument('--integers', metavar='int', type=int, choices=range(10),
                    nargs='+', help='an integer in the range 0..9')

parser.add_argument('--baz', nargs='?', type=int, default=42,
                    help='the bar to %(prog)s (default: %(default)s)')

parser.add_argument('--move', choices=['rock', 'paper', 'scissors'])

parser.add_argument('--length', default='10', type=int, required=True)
parser.add_argument('--width', default=10.5, type=int,
                    help='foo the bars before frobbling')

parser.add_argument('--input', default='input.csv', type=argparse.FileType('r'))
parser.add_argument('--output', default='output.c', type=argparse.FileType('w'))

script = parser.parse_args()

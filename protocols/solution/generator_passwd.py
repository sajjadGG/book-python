import sys


FILE = '../assignment/etc-passwd.txt'


def function():
    accounts = []

    with open(FILE) as file:
        for line in file:
            if line.isspace() or line.startswith('#'):
                continue

            username, _, uid, *_ = line.split(':')

            if int(uid) < 1000:
                accounts.append(username)

        return accounts


def generator():
    with open(FILE) as file:
        for line in file:
            if line.isspace() or line.startswith('#'):
                continue

            username, _, uid, *_ = line.split(':')

            if int(uid) < 1000:
                yield username


if __name__ == '__main__':
    fn = function()
    gene = generator()

    print(f'Function: {sys.getsizeof(fn)}')
    print(f'Generator: {sys.getsizeof(gene)}')

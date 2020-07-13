import sys

FILE = '../data/hosts.txt'


def function():
    accounts = []

    with open(FILE, encoding='utf-8') as file:
        for line in file:
            line = line.strip()

            if len(line) == 0 or line.startswith('#'):
                continue

            username, _, uid, *_ = line.split(':')

            if int(uid) < 1000:
                accounts.append(username)

        return accounts


def generator():
    with open(FILE, encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if len(line) == 0 or line.startswith('#'):
                continue

            username, _, uid, *_ = line.split(':')

            if int(uid) < 1000:
                yield username


if __name__ == '__main__':
    fn = function()
    gene = generator()

    print(f'Function: {sys.getsizeof(fn)}')
    print(f'Generator: {sys.getsizeof(gene)}')

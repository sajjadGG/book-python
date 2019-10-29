FILE = r'../data/etc-hosts-simple.txt'
output = {}


with open(FILE) as file:
    for line in file:
        line = line.strip().split()
        ip = line[0]
        hosts = line[1:]

        if ip in output:
            output[ip] += hosts
        else:
            output[ip] = hosts


print(output)

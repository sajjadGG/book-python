FILE = r'../data/etc-hosts-simple.txt'
output = {}


with open(FILE) as file:
    for line in file:
        ip, *hosts = line.strip().split()

        if ip in output:
            output[ip] += hosts
        else:
            output[ip] = hosts


print(output)

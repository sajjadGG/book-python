PLN = 1
VAT = 23 / 100

net = 100 * PLN
tax = net * VAT
gross = net * (1+VAT)

print(f'Result [PLN]: {net=} {tax=} {gross=}')

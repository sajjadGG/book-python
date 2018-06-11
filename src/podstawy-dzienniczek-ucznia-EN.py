import statistics

ALLOWED_GRADES = (2, 3, 3.5, 4, 4.5, 5)
report_card = []

while True:
    try:
        grade = float(input('Put student grade: '))
    except ValueError:
        break

    if not grade:
        break
    if grade not in ALLOWED_GRADES:
        break

    report_card.append(grade)

mean = statistics.mean(report_card)
print(f'Your average: {mean}')

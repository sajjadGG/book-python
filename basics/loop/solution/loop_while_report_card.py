DATA = (2, 3, 3.5, 4, 4.5, 5)
GRADE_SCALE = []
report_card = []

i = 0

while i < len(DATA):
    grade = float(DATA[i])
    GRADE_SCALE.append(grade)
    i += 1

while True:
    grade = input('What grade you received?: ')

    if not grade:
        break

    grade = float(grade)

    if grade in GRADE_SCALE:
        report_card.append(grade)
    else:
        print('Grade is not allowed')

if report_card:
    mean = sum(report_card) / len(report_card)
    print(f'Mean: {mean}')
else:
    print('Empty report card')

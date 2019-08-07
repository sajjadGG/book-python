ALLOWED_GRADES_ORIGINAL = (2, 3, 3.5, 4, 4.5, 5)
ALLOWED_GRADES = []
report_card = []

i = 0

while i < len(ALLOWED_GRADES_ORIGINAL):
    grade = ALLOWED_GRADES_ORIGINAL[i]
    ALLOWED_GRADES.append(float(grade))
    i += 1

while True:
    grade = input('What grade you received?: ')

    if not grade:
        break

    grade = float(grade)

    if grade in ALLOWED_GRADES:
        print(f'Adding {grade}')
        report_card.append(grade)
    else:
        print('Grade is not allowed')

if report_card:
    average = sum(report_card) / len(report_card)
    print(f'Average: {average}')
else:
    print('Empty report card')

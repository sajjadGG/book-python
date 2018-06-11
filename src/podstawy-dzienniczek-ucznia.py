ALLOWED_GRADES = (2, 3, 3.5, 4, 4.5, 5)
ALLOWED_GRADES = [float(x) for x in ALLOWED_GRADES]
report_card = []


while True:
    grade = float(input('Grade: '))

    if grade in ALLOWED_GRADES:
        print(f'Adding {grade}')
        report_card.append(grade)
    else:
        print('Grade is not allowed')
        break


average = sum(report_card) / len(report_card)
print(f'Average: {average}')

STATUS_NORMAL = 'Normal'
STATUS_ELEVATED = 'Elevated'
STATUS_HYPERTENSION_STAGE_1 = 'Hypertension stage 1'
STATUS_HYPERTENSION_STAGE_2 = 'Hypertension stage 2'
STATUS_HYPERTENSIVE_CRISIS = 'Hypertensive Crisis'
STATUS_UNKNOWN = None


blood_pressure = input('What is your Blood Pressure: ')
sys, dia = blood_pressure.split('/')
sys = int(sys)
dia = int(dia)
status = STATUS_UNKNOWN


if sys < 120 and dia < 80:
    status = STATUS_NORMAL
elif 120 <= sys <= 129 and dia < 80:
    status = STATUS_ELEVATED
elif 130 <= sys <= 139 or 80 <= dia <= 89:
    status = STATUS_HYPERTENSION_STAGE_1
elif 140 <= sys or 90 <= dia:
    status = STATUS_HYPERTENSION_STAGE_2

if 180 <= sys or 120 <= dia:
    status = STATUS_HYPERTENSIVE_CRISIS

print(status)

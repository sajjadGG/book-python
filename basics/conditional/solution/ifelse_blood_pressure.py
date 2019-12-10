STATUS_NORMAL = 'Normal'
STATUS_ELEVATED = 'Elevated'
STATUS_HYPERTENSION_STAGE_1 = 'Hypertension stage 1'
STATUS_HYPERTENSION_STAGE_2 = 'Hypertension stage 2'
STATUS_HYPERTENSIVE_CRISIS = 'Hypertensive Crisis'
STATUS_UNKNOWN = None


blood_pressure = input('What is your Blood Pressure?: ')
systolic, diastolic = blood_pressure.strip().split('/')
systolic = int(systolic)
diastolic = int(diastolic)
status = STATUS_UNKNOWN


if systolic < 120 and diastolic < 80:
    status = STATUS_NORMAL
elif 120 <= systolic <= 129 and diastolic < 80:
    status = STATUS_ELEVATED
elif 130 <= systolic <= 139 or 80 <= diastolic <= 89:
    status = STATUS_HYPERTENSION_STAGE_1
elif 140 <= systolic or 90 <= diastolic:
    status = STATUS_HYPERTENSION_STAGE_2

if 180 <= systolic or 120 <= diastolic:
    status = STATUS_HYPERTENSIVE_CRISIS

print(status)


# Alternative solution
if 180 <= systolic or 120 <= diastolic:
    status = STATUS_HYPERTENSIVE_CRISIS
elif 140 <= systolic or 90 <= diastolic:
    status = STATUS_HYPERTENSION_STAGE_2
elif 130 <= systolic <= 139 or 80 <= diastolic <= 89:
    status = STATUS_HYPERTENSION_STAGE_1
elif 120 <= systolic <= 129 and diastolic < 80:
    status = STATUS_ELEVATED
elif systolic < 120 and diastolic < 80:
    status = STATUS_NORMAL

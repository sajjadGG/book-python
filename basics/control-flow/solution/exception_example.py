class CotangentError(Exception):
    pass


degrees = input('Type angle [deg]: ')

if int(degrees) == 180:
    raise CotangentError('Cotangent for 180 degrees is infinite')

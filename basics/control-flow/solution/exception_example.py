class CotangentInfiniteError(Exception):
    pass


degrees = input('Type angle [deg]: ')

if degrees == 180:
    raise CotangentInfiniteError('Cotangent for 180 degrees is infinite')

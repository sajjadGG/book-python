CREW_PRIMARY = [
    {'is_astronaut': True, 'name': 'Jan Twardowski'},
    {'is_astronaut': True, 'name': 'Mark Watney'},
    {'is_astronaut': True, 'name': 'Melissa Lewis'}]

CREW_BACKUP = [
    {'is_astronaut': True, 'name': 'Melissa Lewis'},
    {'is_astronaut': True, 'name': 'Mark Watney'},
    {'is_astronaut': False, 'name': 'Alex Vogel'}]


def check(field, value):
    def decorator(func):
        def wrapper(crew):
            for member in crew:
                if member.get(field) != value:
                    raise PermissionError
            return func(crew)
        return wrapper
    return decorator


@check(field='is_astronaut', value=True)
def launch(crew):
    print('Launch')


launch(CREW_PRIMARY)
launch(CREW_BACKUP)

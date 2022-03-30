
"""

Accept-Language: en-US,en;q=0.9,pl;q=0.8


Accept-Language

en-US,en-GB,en-AU,en-NZ,en;q=0.9,pl;q=0.8



en;q=0.9,pl;q=0.8,ua;q=0.7

"""







# username = request_data['username']
# password = request_data['password']
#
# user = await db.exdcute('...')
#
# return {'firstname': user.firstname, 'lastname': user.lastname}
#






from typing import TypedDict


class Response(TypedDict):
    id: int


@api('/user/login')
class UserLogin:
    response = {'id': int, 'username': str}

    #@require_jwt
    async def post(self, username: str, password: str) -> response:
        #u = select(User).where(username=username)
        return True


@api('/api/v1/user')
class User:
    params =

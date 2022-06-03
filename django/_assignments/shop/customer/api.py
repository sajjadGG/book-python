from ninja import Router
from shop.schemas import Unauthorized, UnprocessableEntity
from customer.schemas import UserCreate, UserLoginIn, UserLoginOut

router = Router()


@router.get('/')
def get_customer(request, id: int):
    return {'customer': 1}


@router.get('/')
def create_customer(request, user: UserCreate):
    return {'customer': 1}


@router.get('/')
async def index(request):
    return {'msg': 'hello world'}


@router.get('/user', tags=['user'])
async def hello_user(request, firstname: str, lastname: str):
    return {'msg': f'hello {firstname} {lastname}'}


@router.post('/user', tags=['user'])
async def create_user(request, user: UserCreate):
    return {'details': 'ok'}


@router.post('/login', tags=['user'], response={
    200: UserLoginOut,
    401: Unauthorized,
    422: UnprocessableEntity})
async def login(request, user: UserLoginIn):
    try:
        myuser = user.dict()
    except ValueError as err:
        return 422, {'details': err}

    if myuser:
        return 200, {'uid': 1, 'username': 'mwatney'}
    else:
        return 401, {'details': 'Invalid login/password'}

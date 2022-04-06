FastAPI Test Async
==================

>>> from unittest import IsolatedAsyncioTestCase
>>> from httpx import Response, AsyncClient
>>>
>>>
>>> BASE_URL = 'http://localhost:8000'
>>>
>>>
>>> async def request(method: str, url: str, *args, **kwargs) -> Response:
...     client: AsyncClient
...     async with AsyncClient(base_url=BASE_URL) as client:
...         return await client.request(method, url, *args, **kwargs)
>>>
>>>
>>> class MainTestAsync(IsolatedAsyncioTestCase):
...     async def test_main(self):
...         response = await request('GET', '/')
...         self.assertEqual(response.status_code, 200)
...         self.assertEqual(response.json(), {'message': 'main'})
...
...     async def test_hello(self):
...         response = await request('GET', '/hello', params={'firstname': 'Mark', 'lastname': 'Watney'})
...         self.assertEqual(response.status_code, 200)
...         self.assertEqual(response.json(), {'message': 'hello Mark Watney'})

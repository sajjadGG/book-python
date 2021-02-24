import uvicorn
from fastapi import FastAPI
from blog.views import api as blog
from user.views import api as user
from database import Model, engine


app = FastAPI()
app.include_router(blog)
app.include_router(user)

Model.metadata.create_all(engine)


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)

import uvicorn
from fastapi import FastAPI
from blog.views import api as blog
from auth.views import api as auth
from database import Model, engine


app = FastAPI()
app.include_router(auth)
app.include_router(blog)

Model.metadata.create_all(engine)


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)

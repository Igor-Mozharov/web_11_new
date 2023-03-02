from fastapi import FastAPI
from src.routes import contacts

app = FastAPI()

app.include_router(contacts.router)


@app.get('/')
def read_root():
    return {'message': 'hello world'}
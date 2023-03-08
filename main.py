from fastapi import FastAPI
from src.routes import contacts, auth

app = FastAPI()

app.include_router(contacts.router)
app.include_router(auth.router)


@app.get('/')
def read_root():
    return {'message': 'hello world'}
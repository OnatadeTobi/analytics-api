from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'hello': 'world'}


@app.get('/healthz')
def read_api_health():
    return {'status': 'ok'}
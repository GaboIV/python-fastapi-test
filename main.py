from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/url")
def read_root():
    return {"url": "www.gabo.lat"}

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root() -> dict:
    return {'msg': 'Welcome to Drive & Deal App!'}
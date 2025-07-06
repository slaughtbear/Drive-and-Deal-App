from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.routes.auth import auth_router


app = FastAPI()
templates = Jinja2Templates(directory="src/templates")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html",
    )


app.include_router(
    router=auth_router,
    prefix="/auth",
    tags=["Authentication"]
)
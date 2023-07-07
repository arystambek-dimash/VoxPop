from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request:Request):
    return templates.TemplateResponse("main/index.html", {"request": request})

@app.get("/categories")
def home(request:Request):
    return templates.TemplateResponse("main/categories.html", {"request": request})

@app.get("/feeds")
def home(request:Request,):
    return templates.TemplateResponse("main/feeds.html", {"request": request})


@app.get("/form")
def home(request:Request,):
    return templates.TemplateResponse("main/form.html", {"request": request})
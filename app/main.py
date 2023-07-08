from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .repository import CommentRepository
app = FastAPI()

repository = CommentRepository()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request:Request):
    return templates.TemplateResponse("main/index.html", {"request": request})

@app.get("/categories")
def home(request:Request):
    return templates.TemplateResponse("main/categories.html", {"request": request})

@app.get("/feeds")
def home(request:Request,check:str = "",search:str=""):
    if check:
        filtered_category = [i for i in repository.get_all() if i["category"] == check.lower()]
        filtered_category_children = []
        for i in filtered_category:
            if search.lower() in i["comment"].lower():
                filtered_category_children.append(i)
        return templates.TemplateResponse("main/feeds.html", {"request": request,"category":filtered_category_children})
    else:
        filtered_category = repository.get_all()
        filtered_category_children = []
        for i in filtered_category:
            if search.lower() in i["comment"].lower():
                filtered_category_children.append(i)
        return templates.TemplateResponse("main/feeds.html", {"request": request,"category":filtered_category_children})



@app.get("/form")
def home(request:Request,):
    return templates.TemplateResponse("main/form.html", {"request": request})

@app.post("/form")
def home(request:Request,):
    return templates.TemplateResponse("main/form.html", {"request": request})
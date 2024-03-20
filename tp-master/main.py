from fastapi import FastAPI, Request
from fastapi import Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db import Session,engine,Base
from routes import task as task_routes
from routes import user as user_routes
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class User(BaseModel):
    login: str
    password: str
    role: str
Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/galv/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("galv.html", {"request": request})

@app.get("/register/", response_class=HTMLResponse)
async def get_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.get("/login/")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/task/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("task.html", {"request": request})


origins = [
    "http://localhost:8000",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(task_routes.router,prefix="/api")
app.include_router(user_routes.router,prefix="/api")

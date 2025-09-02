from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import HTMLResponse, PlainTextResponse

app = FastAPI()
html_file = open("./lab1.html", "r").read()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return html_file


class Comment(BaseModel):
    username: str
    text: str


all_comments = []


@app.post("/comments")
def create_comment(comment: Comment):
    all_comments.append(comment)
    return "Comment created successfully"


@app.get("/comments", response_model=List[Comment])
def get_comments():
    return all_comments

import requests
from fastapi import APIRouter

router = APIRouter()


@router.get("/books")
def get_books(title: str):
    result = requests.get("https://www.googleapis.com/books/v1/volumes", params={"q": title}).json()
    books = result["items"]
    books_info = []
    for book in books:
        title = book["volumeInfo"]["title"]
        authors = book["volumeInfo"].get("authors", "Авторы неизвестны")
        published_date = book["volumeInfo"]["publishedDate"]
        description = book["volumeInfo"].get("description", "Описание отсутствует")
        books_info.append(
            {"Название: ": title, "Авторы: ": authors, "Дата издания: ": published_date, "Описание: ": description})
    return books_info


@router.get("/jokes")
def get_joke(theme: str):
    result = requests.get("https://api.humorapi.com/jokes/search",
                          params={"keywords": theme, "api-key": "8fe2aca25d5a4aff8ae30060b1cfd3f7",
                                  "number": 10}).json()["jokes"]
    jokes_list = []
    for jokes in result:
        joke = jokes["joke"]
        jokes_list.append({"Шутка: ": joke})
    return jokes_list

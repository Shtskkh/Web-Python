from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse

app = FastAPI()


class Product(BaseModel):
    product_id: int
    name: str
    category: str
    price: float


class Message(BaseModel):
    message: str


products = [
    Product(product_id=1, name="Wireless Mouse", category="Electronics", price=29.99),
    Product(product_id=2, name="Running Shoes", category="Footwear", price=79.95),
    Product(product_id=3, name="Coffee Maker", category="Appliances", price=49.50),
    Product(product_id=4, name="Fantasy Book", category="Books", price=14.99),
    Product(product_id=6, name="The Lord of the Rings Book", category="Books", price=15.99)
]


@app.get("/products/{product_id}", response_model=Product, responses={404: {"model": Message}})
def get_product(product_id: int):
    for product in products:
        if product.product_id == product_id:
            return product
    return JSONResponse(status_code=404, content={"message": "Not found"})


@app.get("/products/search/", response_model=List[Product], responses={404: {"model": Message}})
def get_products_search(keyword: str, category: str | None = None, limit: int = 10):
    filtered_products = []

    for product in products:
        if keyword.lower() in product.name.lower():
            if category is not None and product.category.lower() != category.lower():
                continue
            filtered_products.append(product)

    if len(filtered_products) == 0:
        return JSONResponse(status_code=404, content={"message": "No products found"})

    return filtered_products[:limit]

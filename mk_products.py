#!usr/bin/env python3

from app import db
from app.database import Product

def create_product(name, price, quantity, description):
    db.session.add(
        Product(
            name=name,
            price=price,
            quantity=quantity,
            description=description
        )
    )
    db.session.commit()

if __name__ == "__main__":
    create_product("Bananas", 10.00, 10, "real good")
    create_product("Oranges", 12.00, 50, "real good")
    create_product("Grapes", 11.50, 100, "real good")
    create_product("Strawberries", 10.25, 300, "real good")
    products = Product.query.all()
    print(products)
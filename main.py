# DEBUGGING ASSIGNMENT
# This file contains MANY intentional errors.
# The program should manage a list of products and print summary information.
# Fix all errors so the program runs correctly and produces logical output.

def calculate_total_price(products):
    total = 0
    for item in products:
        total = total + item["price"]
    return total


def apply_discount(price, discount):
    discount = int(discount)
    if discount > 1:
        discount = discount / 100
    if isinstance(price, str):
        if isinstance(price, float):
            price = price
        else:
            price = int(price)
    return price - (price * discount)


def update_stock(products, product_name, amount):
    amount = int(amount)
    for product in products:
        if product["name"] == product_name:
            product["stock"] = product["stock"] - amount
    return product


def get_average_price(products):
    total = calculate_total_price(products)
    return total / len(products)


def print_products(products):
    for i in range(len(products)):
        print(f"{products[i]["name"]} - {products[i]["price"]} - {products[i]["stock"]}")


products = [
    {"name": "Pencil", "price": 0.99, "stock": 100},
    {"name": "Notebook", "price": 2.50, "stock": 50},
    {"name": "Backpack", "price": 25, "stock": 20},
    {"name": "Marker", "price": 1.5, "stock": 70}
]

class Product:

    def __init__(self, product_id, company_id, name, category, price):
        self.product_id = product_id
        self.company_id = company_id
        self.name = name
        self.category = category
        self.price = price

    def describe(self):
        return (
            f"Product: {self.name}\n"
            f"Category: {self.category}\n"
            f"Price: ${self.price:,.2f}"
        )
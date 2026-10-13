class Order:
    def __init__(
        self,
        order_id,
        company_id,
        customer_id,
        product_id,
        quantity,
        unit_price,
        status="pending"
        
    ):
        self.order_id = order_id
        self.company_id = company_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price
        self.status = status
        
    def calculate_total(self):
        return self.quantity * self.unit_price
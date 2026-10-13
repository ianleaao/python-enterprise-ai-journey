class Customer:

    def __init__(self, customer_id, company_id, name, email, status, total_revenue):
        self.customer_id = customer_id
        self.company_id = company_id
        self.name = name
        self.email = email
        self.status = status
        self.total_revenue = total_revenue

    def describe(self):
        return (
            f"Customer: {self.name}\n"
            f"Email: {self.email}\n"
            f"Status: {self.status}\n"
            f"Total Revenue: ${self.total_revenue:,.2f}"
        )
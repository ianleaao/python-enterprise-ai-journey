class Company:

    def __init__(self, name, industry, revenue, employees):
        self.name = name
        self.industry = industry
        self.revenue = revenue
        self.employees = employees

    def revenue_per_employee(self):
        return self.revenue / self.employees

    def describe(self):
        return (
            f"Company: {self.name}\n"
            f"Industry: {self.industry}\n"
            f"Revenue: ${self.revenue:,.2f}\n"
            f"Employees: {self.employees}"
        )

    def is_high_revenue(self, threshold):
        if self.revenue > threshold:
            return True
        else:
            return False
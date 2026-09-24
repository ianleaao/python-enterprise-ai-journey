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

class CompanyAnalytics:

    def __init__(self, companies):
        self.companies = companies

    def high_revenue_companies(self, threshold):
        high_revenue = []

        for company in self.companies:
            if company.is_high_revenue(threshold):
                high_revenue.append(company)

        return high_revenue
    
    
    
company = Company("Atla", "Marketing and AI Software", 5000, 3) 
company2 = Company("America Airlines", "Airlines Company", 10000000, 3000) 
company3 = Company("Mira Safety", "Personal Protective Equipment (PPE)", 8000000, 100)

companies = [company, company2, company3] 


analytics = CompanyAnalytics(companies)

high_revenue = analytics.high_revenue_companies(1000000)

for company in high_revenue:
    print(company.describe())






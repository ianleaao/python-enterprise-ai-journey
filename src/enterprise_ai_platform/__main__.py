from .company import Company
from .analytics import CompanyAnalytics


company = Company("Atla", "Marketing and AI Software", 5000, 3)
company2 = Company("America Airlines", "Airlines Company", 10000000, 3000)
company3 = Company("Mira Safety", "Personal Protective Equipment (PPE)", 8000000, 100)

companies = [company, company2, company3]

analytics = CompanyAnalytics(companies)

high_revenue = analytics.high_revenue_companies(1000000)

for company in high_revenue:
    print(company.describe())
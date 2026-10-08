class CompanyAnalytics:

    def __init__(self, companies):
        self.companies = companies

    def high_revenue_companies(self, threshold):
        high_revenue = []

        for company in self.companies:
            if company.is_high_revenue(threshold):
                high_revenue.append(company)

        return high_revenue
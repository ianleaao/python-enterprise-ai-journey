from .company import Company
from .analytics import CompanyAnalytics
from .customer import Customer
from .product import Product
from .order import Order


company = Company(1,"Atla", "Marketing and AI Software", 5000, 3)
company2 = Company(2,"America Airlines", "Airlines Company", 10000000, 3000)
company3 = Company(3,"Mira Safety", "Personal Protective Equipment (PPE)", 8000000, 100)

customer = Customer(1,1,"John Smith","john@example.com","active",15000)

product = Product(1,1,"AI Marketing Tool","Software",99.99)
order = Order(1001,1,1,1,2,99.99)


print("\n=== CUSTOMER ===")
print(customer.describe())

print("\n=== PRODUCT ===")
print(product.describe())

print("\n=== ORDER ===")
print(f"Order ID: {order.order_id}")
print(f"Customer ID: {order.customer_id}")
print(f"Product ID: {order.product_id}")
print(f"Quantity: {order.quantity}")
print(f"Status: {order.status}")
print(f"Total: ${order.calculate_total():,.2f}")


companies = [company, company2, company3]

analytics = CompanyAnalytics(companies)

high_revenue = analytics.high_revenue_companies(1000000)

print("\n=== HIGH REVENUE COMPANIES ===")

for current_company in high_revenue:
    print(current_company.describe())
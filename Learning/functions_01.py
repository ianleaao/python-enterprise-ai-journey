def calculate_revenue(price,quantity,discount):
    invoicing =  price*quantity
    discount_amount = invoicing*discount/100
    return invoicing-discount_amount
total = calculate_revenue(100,3,22)

print (total)
import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import os

#ensuring 'data' directory exists
os.makedirs("data", exist_ok=True)

fake = Faker()

#loading products
products_df = pd.read_csv("data/products_data.csv")

#generating sales records
sales = []
for _ in range(500):
    product = products_df.sample(1).iloc[0]
    
    #random date in the past 12 months
    days_back = random.randint(0, 364)
    order_date = datetime.today() - timedelta(days=days_back)
    order_date = order_date.strftime('%Y-%m-%d')
    
    customer_id = fake.uuid4()
    customer_segment = random.choice(["VIP", "Regular", "New"])
    sales_channel = random.choice(["e-commerce", "direct"])
    quantity = random.randint(1, 10)
    unit_price = product['price']
    discount = product['discountPercentage']
    cost = unit_price * random.uniform(0.5, 0.8)
    gross_margin = (unit_price - cost) * quantity

    sales.append({
        "order_id": fake.uuid4(),
        "order_date": order_date,
        "customer_id": customer_id,
        "customer_segment": customer_segment,
        "product_id": product['id'],
        "product_title": product['title'],
        "product_category": product['category'],
        "product_type": product['brand'],
        "sales_channel": sales_channel,
        "quantity": quantity,
        "unit_price": unit_price,
        "discount": discount,
        "cost": round(cost, 2),
        "gross_margin": round(gross_margin, 2),
    })

sales_df = pd.DataFrame(sales)
sales_df.to_csv("data/sales_data.csv", index=False)

print("Generated 500 synthetic sales records to data/sales_data.csv (dates spread over last 12 months)")


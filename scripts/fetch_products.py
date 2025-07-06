import requests
import pandas as pd

url = "https://dummyjson.com/products?limit=100"
response = requests.get(url)
data = response.json()
products = data['products']

df = pd.DataFrame(products)
df.to_csv("data/products_data.csv", index=False)

print("Fetched and saved 100 products to data/products_data.csv")

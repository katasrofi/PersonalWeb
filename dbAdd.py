import json
from base.models import Product 

# Open Json File 
with open('../DataPreprocessing/AmazonData.json') as json_file:
    data = json.load(json_file)

import pandas as pd 

df = pd.json_normalize(data)

for index, item in df.iterrows():
    product = Product(
        url=item.get('url', ''),
        title=item.get('title', ''),
        asin=item.get('asin', ''),
        price=item.get('price', 0) or 0,  # Default price to 0 if missing or empty
        brand=item.get('brand', ''),
        product_details=item.get('product_details', ''),
        breadcrumbs=item.get('breadcrumbs', ''),
        images_list=item.get('images_list', ''),
        features=item.get('features', ''),
    )
    product.save()

print("Data successfully imported!")

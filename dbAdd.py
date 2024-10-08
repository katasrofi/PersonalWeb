import json
from base.models import Product 

# Open Json File 
with open('../DataPreprocessing/amazon_uk_shoes_dataset.json') as json_file:
    data = json.load(json_file)

for item in data:
    price = item.get('price') if item.get('price') else '0.00'
    product = Product(
        url=item['url'],
        title=item['title'],
        asin=item['asin'],
        price=price,
        brand=item['brand'],
        product_details=item['product_details'],
        breadcrumbs=item['breadcrumbs'],
        images_list=item['images_list'],
        features=item['features'],
    )
    product.save()

print("Data successfully imported")

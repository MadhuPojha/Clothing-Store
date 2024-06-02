# Importer for products


## How to use

1. Put files inside {project_folder}/product_data/import
2. That folder should contain "data.json" and /images/

``` Example of correct data.json file
{
    "clothing_items": [
        {
            "GUID": "1",
            "Title": "Blue Striped Shirt",
            "Description": "Blue shirt with white stripes",
            "Detailed Description": "Blue shirt with horizontal white stripes. Slim fit design with a button-down collar. Ideal for casual or semi-formal occasions.",
            "Category": "Top",
            "Price": 29.99,
            "Size Range": ["S", "M", "L", "XL"],
            "Color": "Blue/White"
        },
[...]
```
Images should be named {GUID}.jpg

3. Run ```python manage.py import_products```

4. A message should be output detailing how it went.
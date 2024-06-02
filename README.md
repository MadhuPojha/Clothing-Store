# Online Store

## General Info

Use ```python manage.py runserver``` to start the server.


## Importing products

1. Put files inside {project_folder}/product_data/import
2. That folder should contain "data.json" and /images/

### Example of correct data.json file (with 1 item)
```JSON
{
    "clothing_items": [
        {
            "GUID": "1",
            "Title": "Blue Striped Shirt",
            "Description": "Blue shirt with white stripes",
            "Category": "Top",
            "Price": 29.99,
        },
  ]
}
```
The above file is only the minimum amount of required data, more can be added but won't change the imported data.

3. Images should be named {GUID}.jpg

4. Run ```python manage.py import_products```

5. A message should be output detailing how it went.

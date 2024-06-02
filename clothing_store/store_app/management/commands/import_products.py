from django.core.management.base import BaseCommand, CommandError
from store_app.models import Product, ProductImages, Category
from django.conf import settings
from django.core.files.images import ImageFile
import json
from pathlib import Path

class Command(BaseCommand):
    help = "Import products from product_data along with pictures."


    def handle(self, *args, **options):
        import_folder: str = settings.IMPORT_FOLDER
        images: str = settings.IMPORT_FOLDER + settings.IMPORT_IMAGES

        product_list: list = []
        with open(import_folder + 'data.json', "r") as product_file:
            data: dict =  json.load(product_file)
            product_list = data["clothing_items"]
        fail_list: list = []
        for product in product_list:
            GUID: str = product["GUID"]
            image: Path = Path(images + f'{GUID}.jpg')
            success_count:int = 0

            if image.is_file():
                try:
                    # Check if category exists, otherwise create it
                    category_obj = Category.objects.filter(name=product["Category"]).first()
                    if category_obj == None:
                        category_obj = Category(
                            name = product["Category"],
                            description = product["Category"],
                            )
                        category_obj.save()
                    
                    # Create the product
                    product_entry = Product(
                        name=product["Title"],
                        category=category_obj,
                        price=product["Price"],
                        description=product["Description"],
                    )
                    product_entry.save()

                    # Store image and ref the Product
                    product_image = ProductImages(
                        product=product_entry,
                        image=ImageFile(open(image, "rb")),
                    )
                    product_image.save()

                except:
                    print("Failed")
                    fail_list.append(f"{GUID} Couldn't impport {GUID}.")

            else:
                fail_list.append(f'{GUID} is missing an image and was not imported.')
                
        for entry in fail_list:
            print(entry)
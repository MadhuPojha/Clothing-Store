from django.core.management.base import BaseCommand, CommandError
from store_app.models import Product, ProductImages
import json

class Command(BaseCommand):
    help = "Import products from product_data along with pictures."

    def handle(self, *args, **options):
        json_file
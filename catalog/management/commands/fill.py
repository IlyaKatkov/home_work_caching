from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories_list = [
            {'name': 'Еда', 'description': 'Вкусная'},
            {'name': 'Техника', 'description': 'Полезная'},
            {'name': 'Книги', 'description': 'Интересные'},
        ]

        product_list = [
            {'name': 'Яблоко', 'description': 'свежее', 'category_id': 1, 'price': '50'},
            {'name': 'Компьютер', 'description': 'игровой', 'category_id': 2, 'price': '70000'},
            {'name': 'Гарри Поттер', 'description': 'Тайная комната', 'category_id': 3, 'price': '500'}

        ]

        for category_item in categories_list:
            Category.objects.create(**category_item)

        products_for_create = []
        for product_item in product_list:
            category_id = product_item.pop('category_id')
            category = Category.objects.get(id=category_id)
            product_item['category'] = category
            products_for_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(products_for_create)
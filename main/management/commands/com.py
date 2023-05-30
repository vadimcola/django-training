from django.core.management import BaseCommand

from main.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'category_name': 'Одежда', 'description': 'Верхняя одежда'},
            {'category_name': 'Обувь', 'description': 'Детская обувь'},
            {'category_name': 'Головные уборы', 'description': 'Головные уборы'},
        ]

        category_create = []

        for i in category_list:
            category_create.append(Category(**i))

        Category.objects.all().delete()
        Category.objects.bulk_create(category_create)


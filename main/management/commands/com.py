from django.core.management import BaseCommand

from main.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'category_name': 'Легковые', 'description': 'Шина предназначена, для использования '
                                                         'на легковых автомобилях '},
            {'category_name': 'Грузовые', 'description': 'Шина предназначена, для использования '
                                                         'на грузовых автомобилях'},
            {'category_name': 'Индустриальная', 'description': 'Шина предназначена, для использования'
                                                               'на специальной строительной техники'},
        ]

        category_create = []

        for i in category_list:
            category_create.append(Category(**i))

        Category.objects.bulk_create(category_create)


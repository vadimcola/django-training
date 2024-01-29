from django.core.management import BaseCommand

from main.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):

        passenger_car = Category.objects.get(category_name='Легковые')
        trucks = Category.objects.get(category_name='Грузовые')
        industrial = Category.objects.get(category_name='Индустриальная')

        product_list = [
            {'product_name': 'Шина FORWARD ARCTIC 700', 'description': 'Форвард Арктик 700 – '
                                                                       'модель зимних шин для легковых '
                                                                       'автомобилей от Алтайского '
                                                                       'шинного комбината.Шины просто '
                                                                       'созданы для суровых условий нашей российской '
                                                                       'зимы. '
                                                                       'Покрышки выдерживают самые низкие '
                                                                       'температуры, не трескаются и не повреждаются. '
                                                                       'Особый рисунок протектора обеспечивает '
                                                                       'надежное сцепление с любым дорожным полотном – '
                                                                       'от льда до заснеженной дороги. Благодаря '
                                                                       'блокам, образующим направленный рисунок, '
                                                                       'и большому количеству ламелей шина не теряет '
                                                                       'управляемости на льду и способна выбраться '
                                                                       'из большого сугроба.',
             'picture': 'images/Arctic700.jpg', 'category': passenger_car, 'price': 2207},
            {'product_name': 'Шина FORWARD TRACTION О-40БМ', 'description': 'Грузовые шины Forward Traction О-40БМ '
                                                                            'обладают рядом '
                                                                            'отличных характеристик. Благодаря '
                                                                            'особому рисунку протектора '
                                                                            'шины можно использовать в условиях '
                                                                            'бездорожья, а прочный каркас '
                                                                            'и качественная резина позволяют шине '
                                                                            'выдерживать большие нагрузки.',
             'picture': 'images/O40bm.jpg', 'category': trucks, 'price': 13950},
            {'product_name': 'Шина FORWARD TRACTION 310', 'description': 'Грузовые шины Forward Traction 310 – пример '
                                                                         'отличного соотношения цены и качества. '
                                                                         'Покрышки выдерживают большие нагрузки и '
                                                                         'обеспечивают безопасное и комфортное '
                                                                         'движение по любым покрытиям.',
             'picture': 'images/310.jpg', 'category': trucks, 'price': 18507},
            {'product_name': 'Шина Nortec IND 02', 'description': 'Бескамерные индустриальные шины Нортек IND 02 '
                                                                  'устанавливаются на строительные, '
                                                                  'подъемно-транспортные и дорожные машины. Основные '
                                                                  'достоинства этой модели –прочность, '
                                                                  'износостойкость и хорошая проходимость.',
             'picture': 'images/IND02.jpg', 'category': industrial, 'price': 9195},
            {'product_name': 'Шина Nortec FT-214', 'description': 'NORTEC FT-214 - недорогие, но качественные шины '
                                                                  'для вилочных погрузчиков. Шины Нортек производятся '
                                                                  'на Алтайском шинном комбинате. Современное '
                                                                  'производство и качественное сырье позволяют '
                                                                  'предприятию радовать покупателя хорошим качеством '
                                                                  'продукции и при этом низкими ценами.',
             'picture': 'images/FT214.png', 'category': industrial, 'price': 5312}
        ]

        product_create = []

        for i in product_list:
            product_create.append(Product(**i))

        Product.objects.bulk_create(product_create)


# from django.core.management import BaseCommand

# from mailing_service.models import Category, Product, Version
# from users.models import User


# class Command(BaseCommand):
#
#     def handle(self, *args, **options):
        # category_list = [
        #     {'name': 'Овощи', 'desc': 'Описание категории овощи'},
        #     {'name': 'Фрукты', 'desc': 'Описание категории фрукты'},
        #     {'name': 'Бытовая химия', 'desc': 'Описание категории бытовая химия'}
        # ]
        # category_for_create = []
        # for item in category_list:
        #     category_for_create.append(Category(**item))
        # Category.objects.all().delete()
        # Category.objects.bulk_create(category_for_create)

        # users_list = [
        #     {'email': 'ivor@yandex.ru', 'phone': '892345678', 'country': 'РФ', 'is_activated': True, 'is_verificated': True},
        #     {'email': 'anna@yandex.ru', 'phone': '892378394', 'country': 'Бельгия', 'is_activated': True, 'is_verificated': True},
        #     {'email': 'ignat@yandex.ru', 'phone': '892647839', 'country': 'РФ', 'is_activated': True, 'is_verificated': True}
        # ]
        # users_for_create = []
        # for item in users_list:
        #     users_for_create.append(User(**item))
        # User.objects.all().delete()
        # User.objects.bulk_create(users_for_create)

        # cat1, _ = Category.objects.get_or_create(name='Овощи', defaults={
        #     "desc": "Описание категории овощи"
        # })
        # cat2, _  = Category.objects.get_or_create(name='Фрукты', defaults={
        #     "desc": "Описание категории фрукты"
        # })
        #
        # user1, _ = User.objects.get_or_create(email="ivor@yandex.ru", defaults={
        #     'phone': '892345678',
        #     'country': 'РФ'
        # })
        # user2, _ = User.objects.get_or_create(email="anna@yandex.ru", defaults={
        #     'phone': '892378394',
        #     'country': 'Бельгия'
        # })
        #
        #
        # product_list = [
        #     {'name': 'Помидор', 'desc': 'Описание помидорки', 'cat': cat1, 'price': '30', 'user': user1},
        #     {'name': 'Арбуз', 'desc': 'Описание арбуза', 'cat': cat2, 'price': '60', 'user': user2}
        # ]
        # product_for_create = []
        # for item in product_list:
        #     product_for_create.append(Product(**item))
        # Product.objects.all().delete()
        # Product.objects.bulk_create(product_for_create)

        # vers_pom = Product.objects.get(name='Помидор')
        # vers_arb = Product.objects.get(name='Арбуз')
        #
        # version_list = [
        #     {'num': '1', 'name': 'Первая', 'prod': vers_pom},
        #     {'num': '2', 'name': 'Вторая', 'prod': vers_pom, 'is_active': True},
        #     {'num': '1', 'name': 'Первая', 'prod': vers_arb},
        #     {'num': '2', 'name': 'Вторая', 'prod': vers_arb},
        #     {'num': '3', 'name': 'Третья', 'prod': vers_arb, 'is_active': True}
        # ]
        # version_for_create = []
        # for item in version_list:
        #     version_for_create.append(Version(**item))
        # Version.objects.all().delete()
        # Version.objects.bulk_create(version_for_create)

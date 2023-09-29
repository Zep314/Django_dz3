from django.core.management.base import BaseCommand
from .create_client import Command as cC
from .create_product import Command as cP
import logging
from faker import Faker

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    """
    Генерируем фейковые данные
    """
    help = "Generate fake data"

    def add_arguments(self, parser):
        parser.add_argument('clients', type=int, help='Amount of clients')
        parser.add_argument('products', type=int, help='Amount of products')

    def handle(self, *args, **kwargs):
        clients = kwargs.get('clients')
        products = kwargs.get('products')

#        cC.handle(self,name='xxx',email='xxx',phone='xxx',address='xxx')
        fake = Faker(locale="ru_RU")
        for _ in range(clients):
            cC.handle(self, name=fake.name(), email=fake.email(),
                      phone=fake.phone_number(), address=fake.address())
        logger.info(f'Added {clients} record into table Clients')

        for _ in range(products):
            cP.handle(self, name=f'{fake.word().title()} {fake.word()}',
                      description=fake.text(),
                      price=f'{fake.random_int(min=0, max=9999)}.{fake.random_int(min=0, max=99)}',
                      amount=fake.random_int(min=0, max=99))
        logger.info(f'Added {products} record into table Products')

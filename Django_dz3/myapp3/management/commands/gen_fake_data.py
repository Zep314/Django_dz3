from django.core.management.base import BaseCommand

import logging

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


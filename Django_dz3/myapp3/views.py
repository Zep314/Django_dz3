from django.shortcuts import render, redirect
import logging
from django.views import View
from .models import Client, Order

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    """
    Функция - загушка. Если вызов был без параметров.
    :param request:
    :return:
    """
    logger.info('Index page accessed! Redirect to /lastday/0/7')
    return redirect("/lastday/0/7")


class LastDay(View):
    def get(self, request, client_id, days=1):
        if client_id == 0:
            client_id = list(Client.objects.values_list('id', flat=True))[0]
        sql = """
            SELECT DISTINCT
                1 as id ,p.name, p.description, p.price, o.order_date 
            FROM myapp3_order o
            JOIN myapp3_order_products op ON op.order_id = o.id
            JOIN myapp3_product p ON op.product_id = p.id
            WHERE o.client_id=%s
            ORDER BY o.order_date 
            ;
            """
        orders = Order.objects.raw(sql, [client_id])
        # orders1 = Order.objects.filter(client_id=client_id). \
        #     values_list('products', 'total_price', 'order_date')
        orders1 = Order.objects.filter(client_id=client_id).prefetch_related('products')

        context = {'orders': orders,
                   'client_id': client_id,
                   'clients': Client.objects.all(),
                   'days': days,
                   }
        logger.info(f'orders1: {orders1}')
        return render(request, 'myapp3/orders.html', context)

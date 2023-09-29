from django.shortcuts import render, redirect
import logging
from django.views import View
from .models import Order

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    """
    Функция - загушка. Если вызов был без параметров.
    :param request:
    :return:
    """
    logger.info('Index page accessed! Redirect to /lastday/7')
    return redirect("/lastday/7")

class LastDay(View):
    def get(self, request, days=1):
#        return HttpResponse(f'Hello World from class! Days:{days}')
        orders = Order.objects.all()
        context = {'orders': orders}
        return render(request, 'myapp3/orders.html', context)

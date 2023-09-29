from django.shortcuts import render
import logging
from django.http import HttpResponse

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    """
    Функция - заглушка
    :param request:
    :return:
    """
    logger.info('Index page accessed')
    return HttpResponse('This is a index page!')

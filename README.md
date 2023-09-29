# Фреймворк Django (семинары)
## Урок 3. Шаблоны, классы и формы

### Задание 1

Продолжаем работать с товарами и заказами.

Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с 
сортировкой по времени:

- за последние 7 дней (неделю)
- за последние 30 дней (месяц)
- за последние 365 дней (год)

Товары в списке не должны повторятся.

==========================

Создайте три модели Django: клиент, товар и заказ.

Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.

Поля модели «Клиент»:
— имя клиента
— электронная почта клиента
— номер телефона клиента
— адрес клиента
— дата регистрации клиента

Поля модели «Товар»:
— название товара
— описание товара
— цена товара
— количество товара
— дата добавления товара

Поля модели «Заказ»:
— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
— связь с моделью «Товар», указывает на товары, входящие в заказ
— общая сумма заказа
— дата оформления заказа

Допишите несколько функций CRUD для работы с моделями по желанию. Что по вашему мнению актуально в такой базе данных.

### Решение
Выполняем стандартные процедуры для запуска нового приложения в новом проекте:

Устанавливаем Django:

    pip install django

Создаем проект для работы:

    django-admin startproject Django_dz3

Переходим в папку проекта:

    cd .\Django_dz3\

Создаем новое приложение в проекте:

    python manage.py startapp myapp3

Запускаем сервер проекта:

    python manage.py runserver

Редактируем файлы:

- [Django_dz2/Django_dz2/Django_dz2/settings.py](/Django_dz2/Django_dz2/settings.py)
- [Django_dz2/Django_dz2/Django_dz2/urls.py](/Django_dz2/Django_dz2/urls.py)
- [Django_dz2/Django_dz2/myapp2/urls.py](/Django_dz2/myapp2/urls.py)
- [Django_dz2/Django_dz2/myapp2/views.py](/Django_dz2/myapp2/views.py)

Создаем модель данных, в соответствие с заданием. 
Модель данных находится в файле: 

- [Django_dz2/Django_dz2/myapp2/models.py](/Django_dz2/myapp2/models.py)

Для каждой таблицы были реализованы все **CRUD** методы. Для таблицы заказов (Order) выполнена поддержка связи 
Many-to-Many с таблицей товаров (Product). 

Примеры методов находятся в пакете *commands*:

- [Django_dz2/Django_dz2/myapp2/management/commands/](/Django_dz2/myapp2/management/commands)

Создаем миграции для нашей модели данных (подготавливаем структуру базы данных для развертывания на сервере БД):

    python manage.py makemigrations myapp3

Применяем миграции (Физически создаем объекты на сервере БД):

    python manage.py migrate

После этого можно запускать команды для работы нашей модели с базой данных:

    python manage.py create_client.py
    python manage.py create_order.py
    python manage.py create_product.py
    python manage.py get_client.py 1
    python manage.py get_order.py 3
    python manage.py get_product.py 1
    python manage.py update_client.py 1
    python manage.py update_order.py 1
    python manage.py update_product.py 1
    python manage.py get_all_clients.py
    python manage.py get_all_orders.py
    python manage.py get_all_products.py
    python manage.py delete_client.py 2
    python manage.py delete_order.py 2
    python manage.py delete_product.py 2


Файл с журналом работы:

- [logs/django.log](/Django_dz2/logs/django.log) 

## Результат работы:

Длинные строки разделил вручную, чтобы было более понятно:

    (venv) C:\Work\python\Django\Django_dz2\Django_dz2>python manage.py get_all_clients
    INFO 2023-09-27 14:20:35,119 get_all_clients 30840 7576 Get all clients!
    <QuerySet [
    <Client: Name: Oliver, email: john@example.com, phone: +7-123-456-78-90, address: 221B Baker Street, London NW1 6XE, England, register_date: 2023-09-26 10:00:06.392644+00:00>, 
    <Client: Name: John, email: john@example.com, phone: +7-123-456-78-90, address: 221B Baker Street, London NW1 6XE, England, register_date: 2023-09-26 10:46:18.055859+00:00>, 
    <Client: Name: John, email: john@example.com, phone: +7-123-456-78-90, address: 221B Baker Street, London NW1 6XE, England, register_date: 2023-09-26 13:07:49.942485+00:00>
    ]>

    (venv) C:\Work\python\Django\Django_dz2\Django_dz2>python manage.py get_all_products
    INFO 2023-09-27 14:20:41,616 get_all_products 30656 25828 Get all products!
    <QuerySet [
    <Product: Name: Toyota ,Description: Best electric car ,Price: 0.50 ,Amount: 11 ,Create_date: 2023-09-26 12:12:00.113095+00:00 >, 
    <Product: Name: Tesla ,Description: Best electric car ,Price: 123456.78 ,Amount: 11 ,Create_date: 2023-09-26 12:13:51.920890+00:00 >, 
    <Product: Name: Tesla ,Description: Best electric car ,Price: 123456.78 ,Amount: 11 ,Create_date: 2023-09-26 12:49:38.977017+00:00 >, 
    <Product: Name: Tesla ,Description: Best electric car ,Price: 123456.78 ,Amount: 11 ,Create_date: 2023-09-26 13:08:10.021048+00:00 >
    ]>

    (venv) C:\Work\python\Django\Django_dz2\Django_dz2>python manage.py get_all_orders
    INFO 2023-09-27 14:20:46,718 get_all_orders 23632 12396 Get all orders!
    <QuerySet [
    <Order: Client: Name: Oliver, email: john@example.com, phone: +7-123-456-78-90, address: 221B Baker Street, London NW1 6XE, England, register_date: 2023-09-26 10:00:06.392644+00:00, Product[s]: <QuerySet []>, Total price: 321.09 ,Order_date: 2023-09-26 12:53:43.930464+00:00>, 
    <Order: Client: Name: Oliver, email: john@example.com, phone: +7-123-456-78-90, address: 221B Baker Street, London NW1 6XE, England, register_date: 2023-09-26 10:00:06.392644+00:00, Product[s]: <QuerySet []>, Total price: 321.09 ,Order_date: 2023-09-26 12:54:39.164671+00:00>, 
    <Order: Client: Name: Oliver, email: john@example.com, phone: +7-123-456-78-90, address: 221B Baker Street, London NW1 6XE, England, register_date: 2023-09-26 10:00:06.392644+00:00, Product[s]: <QuerySet [
        (3, 'Tesla', 'Best electric car', Decimal('123456.78'), 11, datetime.datetime(2023, 9, 26, 12, 13, 51, 920890, tzinfo=datetime.timezone.utc)), 
        (6, 'Tesla', 'Best electric car', Decimal('123456.78'), 11, datetime.datetime(2023, 9, 26, 12, 49, 38, 977017, tzinfo=datetime.timezone.utc))
        ]>, Total price: 44.44 ,Order_date: 2023-09-26 12:55:19.457471+00:00>, 
    <Order: Client: Name: Oliver, email: john@example.com, phone: +7-123-456-78-90, address: 221B Baker Street, London NW1 6XE, England, register_date: 2023-09-26 10:00:06.392644+00:00, Product[s]: <QuerySet []>, Total price: 321.09 ,Order_date: 2023-09-26 13:17:20.294280+00:00>, 
    <Order: Client: Name: Oliver, email: john@example.com, phone: +7-123-456-78-90, address: 221B Baker Street, London NW1 6XE, England, register_date: 2023-09-26 10:00:06.392644+00:00, Product[s]: <QuerySet []>, Total price: 321.09 ,Order_date: 2023-09-26 13:17:47.652770+00:00>, 
    <Order: Client: Name: Oliver, email: john@example.com, phone: +7-123-456-78-90, address: 221B Baker Street, London NW1 6XE, England, register_date: 2023-09-26 10:00:06.392644+00:00, Product[s]: <QuerySet [
        (3, 'Tesla', 'Best electric car', Decimal('123456.78'), 11, datetime.datetime(2023, 9, 26, 12, 13, 51, 920890, tzinfo=datetime.timezone.utc)), 
        (6, 'Tesla', 'Best electric car', Decimal('123456.78'), 11, datetime.datetime(2023, 9, 26, 12, 49, 38, 977017, tzinfo=datetime.timezone.utc)), 
        (7, 'Tesla', 'Best electric car', Decimal('123456.78'), 11, datetime.datetime(2023, 9, 26, 13, 8, 10, 21048, tzinfo=datetime.timezone.utc))
        ]>, Total price: 321.09 ,Order_date: 2023-09-27 11:01:16.769490+00:00>
    ]>

    (venv) C:\Work\python\Django\Django_dz2\Django_dz2>


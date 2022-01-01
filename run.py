from wsgiref.simple_server import make_server
from wolf_framework.main import Framework
from views_like_flask import routes

# Создаем объект WSGI-приложения
application = Framework(routes)

with make_server('', 8080, application) as httpd:
    print('Запуск на порту 8080...')
    httpd.serve_forever()


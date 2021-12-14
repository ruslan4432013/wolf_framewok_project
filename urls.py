from views import *

# Набор привязок: путь-контроллер
routes = {
    '/': Index(),
    '/about/': About(),
    '/contact/': Contact(),
    '/help/': Help()
}

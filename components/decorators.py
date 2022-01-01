# Декоратор для реализации маршрутизации
class AppRoute:
    def __init__(self, routes, url):
        """
        Сохраняем значение переданного параметра
        """
        self.routes = routes
        self.url = url

    def __call__(self, cls):
        """
        Сам декоратор
        """
        self.routes[self.url] = cls()


# Декоратор, как функция (из дз)
def app_route(routes: dict, url):
    def decorator(func):
        routes[url] = func()
        return routes
    return decorator

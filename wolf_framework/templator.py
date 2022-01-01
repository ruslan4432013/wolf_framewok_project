from jinja2 import FileSystemLoader
from jinja2.environment import Environment

def render(template_name, folder='templates', **kwargs):
    """
    :param template_name: Имя шаблона
    :param folder: Папка в которой ищем шаблон
    :param kwargs: параметры, передаваемые в шаблон
    :return:
    """

    env = Environment()  # Позволяет задать окружение для загрузки шаблонов
    env.loader = FileSystemLoader(folder)  # Задаем путь, по которому ищутся шаблоны и загружаются в окружение
    template = env.get_template(template_name)  # Обеспечивает загрузку шаблона с именем template_name из загрузчика
    return template.render(**kwargs)  # Выполняет загрузку шаблона и передачу в него контекста

from abc import abstractmethod

from wolf_framework.templator import render


# Класс-контроллер для простейшего рендеринга HTML-шаблонов
class TemplateView:
    template_name = 'template.html'

    def get_context_data(self):
        return {}

    def get_template(self):
        return self.template_name

    def render_template_with_context(self):
        template_name = self.get_template()
        context = self.get_context_data()
        return '200 OK', render(template_name, **context)

    def __call__(self, request):
        return self.render_template_with_context()


# Класс-контроллер для отображения списков записей
class ListView(TemplateView):
    queryset = []
    template_name = 'list.html'
    context_object_name = 'objects_list'

    def get_queryset(self):
        print(self.queryset)
        return self.queryset

    def get_context_object_name(self):
        return self.context_object_name

    def get_context_data(self):
        queryset = self.get_queryset()
        context_object_name = self.get_context_object_name()
        context = {context_object_name: queryset}
        return context


# Класс-контроллер для создания записи
class CreateView(TemplateView):
    template_name = 'create.html'

    @staticmethod
    def get_request_data(request):
        return request['data']

    def create_obj(self, data):
        pass

    def __call__(self, request):
        if request['method'] == 'POST':
            # метод пост
            data = self.get_request_data(request)
            self.create_obj(data)
            return self.render_template_with_context()
        else:
            return super().__call__(request)


# Класс-контроллер для удаления записей
class DeleteView(TemplateView):
    template_name = 'delete.html'

    @staticmethod
    def get_request_data(request):
        return request['data']

    @abstractmethod
    def delete_obj(self, data):
        pass

    def __call__(self, request):
        if request['method'] == 'POST':
            data = self.get_request_data(request)
            self.delete_obj(data)
            return self.render_template_with_context()
        else:
            return super().__call__(request)


# Класс-контроллер для обновления записей
class UpdateView(TemplateView):
    template_name = 'delete.html'

    @staticmethod
    def get_request_data(request):
        return request['data']

    @abstractmethod
    def update_obj(self, data):
        pass

    def __call__(self, request):
        if request['method'] == 'POST':
            data = self.get_request_data(request)
            self.update_obj(data)
            return self.render_template_with_context()
        else:
            return super().__call__(request)

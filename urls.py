from views import *

# Набор привязок: путь-контроллер
routes = {
    '/': Index(),
    '/about/': About(),
    '/study_programs/': StudyPrograms(),
    '/courses-list/': CoursesList(),
    '/create-course/': CreateCourse(),
    '/create-category/': CreateCategory(),
    '/category-list/': CategoryList(),
    '/contact/': Contact(),
    '/help/': Help()
}

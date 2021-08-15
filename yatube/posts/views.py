from django.shortcuts import render

context = {
        'title': 'Это главная страница проекта Yatube',
        'text': 'Здесь будет информация о группах проекта'
        }


def index(request):
    template = 'posts/index.html'
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    return render(request, template, context)

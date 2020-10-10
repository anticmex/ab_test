from collections import Counter
from django.http import HttpResponse
from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
dict_show = {}
counter_show = Counter()


counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing


    from_landing = request.GET.get('from-landing', '')
    if from_landing == 'test':
        counter_show.update({'test_from_landing': 1})
        counter_click.update({'click': 1})
    elif from_landing == 'original':
        counter_show.update({'original_from_landing': 1})
        counter_click.update({'click': 1})
    return render(request, 'index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    return render(request, 'landing.html')


def alternate(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    return render(request, 'landing_alternate.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    return render(request, 'stats.html', context={
        'test_conversion': counter_show['test_from_landing']/counter_click['click'],
        'original_conversion': counter_show['original_from_landing']/counter_click['click'],
    })

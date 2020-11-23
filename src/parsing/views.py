from django.shortcuts import render
from .models import City, Language, Vacancy
from .forms import FindForm

def vacancies_list(request):
    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    qs = []
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language
        qs = Vacancy.objects.filter(**_filter)
    context = {'object_list': qs, 'form': form}
    return render(request, 'parsing/vacancies_list.html', context)

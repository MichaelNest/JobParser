from django.urls import path, include
from .views import vacancies_list

app_name = 'parsing'

urlpatterns = [
    path('', vacancies_list, name='vacancies_list')
]
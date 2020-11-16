from django.shortcuts import render
import datetime

def home_view(request):
    date = datetime.datetime.now().date()
    name = 'Vasia'
    context = {'name': name, 'date': date}
    return render(request, 'home.html', context)
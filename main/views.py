from django.shortcuts import render
import datetime
from django.conf import settings
from .models import *

def index(request):
    videos = Videos.objects.all()
    categories = Category.objects.all()
    context = {'videos': videos, 'categories': categories}
    return render(request, 'main/index.html', context)

def by_category(request, category_id):
    videos = Videos.objects.filter(category=category_id)
    current_category = Category.objects.get(pk=category_id)
    categories = Category.objects.all()
    context = {'videos': videos, 'categories': categories, 'current_category': current_category}
    return render(request, 'main/by_category.html', context)
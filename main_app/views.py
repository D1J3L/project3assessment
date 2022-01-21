from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm
# Create your views here.

def index(request):
    widget_form = WidgetForm()
    widgets = Widget.objects.all()
    return render(request, 'index.html', {'widgets': widgets, 'widget_form': widget_form})


def add_widget(request):
    form = WidgetForm(request.POST)
    form.save()
    return redirect('/')

def delete_widget(request, id):
    Widget.objects.get(id=id).delete()
    return redirect('/')
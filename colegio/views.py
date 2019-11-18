from django.shortcuts import render
from django.views import generic
from .models import Curso, Pensum

class PensumListView(generic.ListView):
    model = Pensum
    template_name = "list.html"


class PensumDetailView(generic.DetailView):
    model = Pensum
    template_name = "detail.html"


class PensumCreateView(generic.CreateView):
    model = Pensum
    fields = '__all__'
    template_name = "form.html"


class PensumUpdateView(generic.UpdateView):
    model = Pensum
    fields = '__all__'
    template_name = "form.html"

from django.shortcuts import render
from .models import Graph


# Create your views here.
def graph_page(request):

    all_years = Graph.objects.all()
    context = {'all_years' : all_years}

    return render(request, 'graph.html', context)

from django.shortcuts import render
from django.views import View
# Create your views here.

class HomeView(View):
    """docstring for ."""
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'homepage/index.html', context)

from django.shortcuts import render
from django.views.generic import View


class Main(View):
    
    def get(self, request, *a, **kw):
        return render(request, "main/main.html")
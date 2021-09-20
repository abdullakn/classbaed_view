from django.shortcuts import render

from django.views.generic.base import TemplateView
from . models import *


# Create your views here.

class Sample1(TemplateView):
    template_name='index.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['posts']=Post.objects.all()
        print(context['posts'])
        return context

       

from django.urls import path
from django.views.generic import TemplateView
from . views import Sample1

urlpatterns = [
   
    path('',TemplateView.as_view(template_name='index.html' , extra_context={'title':"my title"})),
    path('sample1/',Sample1.as_view())
]

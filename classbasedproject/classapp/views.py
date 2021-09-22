from django import forms
from django.db.models.base import Model
from django.shortcuts import render
from django.urls.conf import path

from django.views.generic.base import TemplateView,RedirectView
from . models import *
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.utils import timezone
from . forms import AddForm



# Create your views here.

class Sample1(TemplateView):
    template_name='index.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['posts']=Post.objects.all()
        print(context['posts'])
        return context


class Sample2(RedirectView):
    # url='https://abdullakn.online'
    pattern_name = 'sample3'
    permanent=True

             

    def get_redirect_url(self, *args, **kwargs):
        # article = get_object_or_404(Post, pk=kwargs['pk'])
        # print(article)
        print(args)
        print(kwargs)
        print(super().get_redirect_url(*args, **kwargs))
        
        return super().get_redirect_url(*args, **kwargs)


class Sample3(TemplateView):
    template_name='detailsredirect.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['posts']=get_object_or_404(Post,pk=self.kwargs.get('pk'))
        return context        


class BookList(TemplateView):
    template_name='booklist.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['books']=Book.objects.all()
        return context    


class BookDetailView(DetailView):
    model=Book  
    template_name='book_detail.html'   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = timezone.now()
        return context   


class ListViewSample(ListView):
    print("listviewjjjjjjjjjjjjjjjjjj")
    Model=Post
    print(Model,"sssdddddddddddd")
    queryset=Post.objects.all()
    template_name="listview.html"   
    context_object_name='books'   
    paginate_by=1 


class AddBook(FormView):
    template_name='add_book.html'
    form_class=AddForm
    success_url='/sample1/'
    print(form_class)
    
    def form_valid(self, form):
        print(form,"after enter....................................")
        
        form.save()
        return super().form_valid(form)
        
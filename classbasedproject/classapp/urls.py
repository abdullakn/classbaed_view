
from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from . views import AddBook, ListViewSample, Sample1,Sample2,Sample3,BookList,BookDetailView
from django.views.generic.base import RedirectView

urlpatterns = [
   
    path('',TemplateView.as_view(template_name='index.html' , extra_context={'title':"my title"})),
    path('sample1/',Sample1.as_view()),


    #redirect view
    path('abdullakn.online',RedirectView.as_view(url='https://abdullakn.online')),
    path('sample2/<int:pk>/',Sample2.as_view(),name='sample2'),
    path('sample3/<int:pk>/',Sample3.as_view(),name='sample3'),


    #detail view
    path('book/',BookList.as_view(),name='booklist'),
    path('book/<slug:slug>/',BookDetailView.as_view(),name='bookdetail'),


    #list view
    path('listview/',ListViewSample.as_view(),name='listview'),


    #form view
    path('add_book/',AddBook.as_view(),name='add_book')

]

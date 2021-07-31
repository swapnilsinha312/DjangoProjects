from django.conf.urls import url
from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns=[
    path('',views.MainPage.as_view(), name='index'),
    #path(r'^$',views.MainPage.as_view(), name='index'),
    path('index/',views.MainPage.as_view() ,name='index'),
    path('blog_list/',views.BlogList.as_view(),name='blog_list'),
    path('blog_open/<int:pk>/',views.BlogOpen.as_view(),name='blog_open'),
    path('blog_create/',views.BlogCreate.as_view(),name='blog_create'),
    path('blog_form/',views.BlogForm.as_view(),name='blog_form') ,
    path('delete/<int:id>/',views.BlogDelete.as_view(),name='blog_delete'),
    #path('blog_list/blog_open/update/<int:pk>/',views.BlogDelete.as_view(),name='blog_update')
    #path(r'^details/(?P<id>\d+)/$',views.details,name='details')
    ]

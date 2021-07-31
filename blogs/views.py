from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from blogs.models import Blog
from blogs.forms import BlogForm
# Create your views here.
#def index(request):
    #blogs=Blog.objects.all()[:10]
    #context ={'title':'Latest Posts', 'posts': Blog}
    #return render(request, 'blogs\index.html' )
    #return HttpResponse('Hello from posts')

class MainPage(View):
    def get(self, request):
        return render(request,'blogs/index.html')

class BlogList(View):
    def get(self,request):
        allBlogs= Blog.objects.all()
        ctx= {'allBlogs':allBlogs}
        return render(request, 'blogs/blog_list.html',ctx)
        #return render(request,'blogs/index.html')

class BlogOpen(View):
    def get(self, request,pk):
         
        blog= Blog.objects.get(id=pk)
        ctx={'blog':blog}
        
        return render(request,'blogs/blog_open.html', ctx)


class BlogCreate(CreateView):
    model = Blog
    fields = '__all__'
    success_url = reverse_lazy('blog_list')

class BlogForm(View):
    def get(self,request):
        return render(request,'blogs/blog_form.html')

class BlogDelete(View):
    def get(self, request,id):
        blog= Blog.objects.get(id=id)
        blog.delete()
        return redirect('blog_list')

 
        
        
#Have to open blog using id
# have to make update delete and create methods
#  



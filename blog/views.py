from django.shortcuts import render
from .models import Post


def home(request):
    my_context = {
        'posts' : Post.objects.all()
    }
    return render(request=request, template_name='blog/home.html', context=my_context)

def about(request):
    return render(request=request, template_name='blog/about.html')

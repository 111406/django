from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Fang',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 9, 2022',
    },
    {
        'author': 'Ben',
        'title': 'Blog Post 2',
        'content': 'Sencond post content',
        'date_posted': 'April 10, 2022',
    },
]


def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})

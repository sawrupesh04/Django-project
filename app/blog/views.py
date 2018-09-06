from django.shortcuts import render, get_object_or_404

from .models import Blogs

def allblogs(request):
    blogs = Blogs.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})


def detail(request, blog_id):
    detailblog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detailblog})
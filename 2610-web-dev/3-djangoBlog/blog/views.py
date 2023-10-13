from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import blog, comment

# ---- VIEWS ----
# -- STATIC --
# ABOUT
def about(request):
    ip = request.META['REMOTE_ADDR']
    context = {"ip" : ip}
    return render(request, 'blog/about.html', context)
# TECHTIPS-
def techtips_minus_css(request):
    ip = request.META['REMOTE_ADDR']
    context = {"ip" : ip}
    return render(request, 'blog/techtips-css.html', context)
# TECHTIPS+
def techtips_plus_css(request):
    ip = request.META['REMOTE_ADDR']
    context = {"ip" : ip}
    return render(request, 'blog/techtips+css.html', context)

# -- DYNAMIC --
# HOME
def index(request):
    ip = request.META['REMOTE_ADDR']
    latest_blog_list = blog.objects.order_by('-posted')[:3]
    context = {'latest_blog_list' : latest_blog_list, "ip" : ip}
    return render(request, 'blog/home.html', context)

# ARCHIVE
def archive(request):
    ip = request.META['REMOTE_ADDR']
    blog_list = blog.objects.order_by('-posted')
    context = {'blog_list' : blog_list, "ip" : ip}
    return render(request, 'blog/archive.html', context)

# SINGLE BLOG ENTRY 
def blog_post(request, blog_id):
    ip = request.META['REMOTE_ADDR']
    post = get_object_or_404(blog, pk=blog_id)
    try:
        comments = post.get_comments()
    except:
        comments = None
    context = {'blog' : post, 'comments' : comments, "ip" : ip}
    return render(request, 'blog/entry.html', context)

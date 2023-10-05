from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('archive/', views.archive, name='archive'),
    path('<int:blog_id>/', views.blog_post, name='blog_post'),
    path('about.html', views.about, name='about'),
    path('techtips+css.html', views.techtips_plus_css, name='techtips+css'),
    path('techtips-css.html', views.techtips_minus_css, name='techtips-css'),
]
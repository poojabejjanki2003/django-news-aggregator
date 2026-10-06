from django.urls import path
from news.views import scrape, news_list, statichome
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('scrape/<str:name>', scrape, name='scrape'),

    path('news/', news_list, name='news_list'),

    path('news/about.html', views.about, name='about'),
    path('news/contact.html', views.contact, name='contact'),
    path('news/report.html', views.report, name='report'),
    path('news/login.html', views.login, name='login'),
     path('news/register.html', views.register, name='register'),
    path('news/homestatic.html', statichome, name='breakinghome'),
    path('contact-submit/', views.contact_submit, name='contact_submit'),
]
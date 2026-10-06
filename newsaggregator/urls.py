
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("news.urls")),
    path('home',include("news.urls")),
    path('about',include("news.urls")),
    path('contact',include("news.urls")),
    path('login',include("news.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name="about"),
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name="logout")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

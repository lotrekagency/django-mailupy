from django.contrib import admin
from django.urls import path, include
from . import views
from django.shortcuts import redirect

def redirect_to_admin(request):
    return redirect('/admin/')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("django_mailupy.urls")),
    path("test-mailupy/", views.test_mailupy),
    path("", redirect_to_admin),
]

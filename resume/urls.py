from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.accept, name='accept'),

    path('resume/<int:id>/', views.resume, name='resume'),
]
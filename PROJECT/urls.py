from django.contrib import admin
from django.urls import path
from todo.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', Tasks.as_view(),name='tasks'),
    path('login/', login,name='login'),
    path('<int:id>/edit/', edit,name='edit'),
    path('<int:id>/ochir/',task_ochir),

]

from django.contrib import admin
from django.urls import path
from todo.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', Tasks.as_view(),name='tasks'),
    path('', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('<int:id>/edit/', TaskEditView.as_view(),name='edit'),
    path('<int:id>/ochir/',task_ochir),

]

from django.urls import path

from . import views

urlpatterns = [
    # '/todo/'
    path('', views.index, name='todo_index'),
    # '/todo/list/'
    path('list/', views.list, name='toso_list'),
    # '/todo/1/'
    path('<int:todo_id>/', views.item, name='todo_item')
]

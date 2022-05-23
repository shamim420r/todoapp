from django.urls import path
from .import views

urlpatterns = [
    path('', views.todo_form, name='todo_insert'),
    path('<int:id>', views.todo_form, name='todo_update'),
    path('delete/<int:id>', views.todo_delete, name='todo_delete'),
    path('view/<int:id>', views.todo_view, name='todo_view'),
    path('list/', views.todo_list, name='todo_list'),
]
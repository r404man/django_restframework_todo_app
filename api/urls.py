from django.urls import path
from . import views

urlpatterns = [
    path('',views.ApiOverview, name="api-overview" ),
    path('task-list/',views.TaskList, name="task-list" ),
    path('task-detail/<int:pk>/',views.TaskDetail, name="task-detail" ),
    path('task-create/',views.TaskCreate, name="task-create" ),
    path('task-update/<int:pk>/',views.TaskUpdate, name="task-update" ),
    path('task-delete/<int:pk>/',views.TaskDelete, name="task-delete" ),
]
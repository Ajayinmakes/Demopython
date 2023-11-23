
from django.urls import path
from .import views

urlpatterns = [

    path('', views.add, name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbv home/',views.TaskListView.as_view(),name='cbv home'),
    path('cbv detail/<int:pk>/',views.TaskDetailView.as_view(), name='cbv detail'),
    path('cbv update/<int:pk>/',views.TaskUpdateView.as_view(),name='cbv update'),
    path('cbv delete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbv delete'),
]
from django.urls import path
from . import views


urlpatterns = [
    path('all/', views.AllList.as_view(), name='all'),
    path('active/', views.ActiveList.as_view(), name='active'),
    path('completed/', views.CompletedList.as_view(), name='completed'),
    path('edit/<int:pk>', views.TaskUpdate.as_view(), name='edit'),
    path('delete/<int:pk>', views.TaskDelete.as_view(), name='delete')
]
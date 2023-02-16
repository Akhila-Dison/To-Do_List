from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.add, name='add'),
    # path('details/', views.details, name='details'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),

]

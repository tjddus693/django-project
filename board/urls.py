from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.board1,name='board1'),
    path('list/', views.board2,name='board2'),
    path('board3/', views.board3,name='board3'),
    path('detail/<int:id>/', views.detail,name='detail'),
    path('update/<int:id>/', views.update,name='update'),
    path('delete/<int:id>/', views.delete,name='delete'),
    
]


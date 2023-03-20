from django.urls import path
from . import views

app_name = 'ranking'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), 
    path('preview/movies/<int:pk>/', views.MoviePeviewView.as_view(), name='preview'), 
    path('preview/movies/<int:pk>/<int:winner_id>', views.ResultView.as_view(), name='preview'), 
    path('ranking/movies/<int:pk>', views.RankingView.as_view(), name='ranking'), 
    path('sendData/', views.SendDataView.as_view(), name='pos'), 
    path('getData/', views.RequestDataView.as_view(), name='get'),
]
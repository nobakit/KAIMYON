from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test_db_ope', views.test_db_ope, name='test_db_ope'),
]
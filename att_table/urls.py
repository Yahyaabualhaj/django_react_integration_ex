

from django.urls import path
from . import views

urlpatterns = [

   # path('table/', views.TablesList.as_view(), name='lists'),
    path('', views.table, name='lists')
]

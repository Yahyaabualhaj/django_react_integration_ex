
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('att_table.urls')),
    # path('table/', views.ListView.as_view)
]

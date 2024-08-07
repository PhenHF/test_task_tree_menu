from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('tree_menu.urls', namespace='tree_menu'))
]

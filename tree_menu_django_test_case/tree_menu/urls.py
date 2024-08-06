from django.urls import path
from . import views

app_name = 'tree_menu'


urlpatterns = [
    path('', view=views.IndexPageView.as_view()),
    path('<path:menu_url>', view=views.SubMenuPageView.as_view(), name='menu')
]

from django.views.generic import TemplateView, ListView
from .models import MenuItem
from django.db.models import Q


class IndexPageView(TemplateView):
    template_name = 'index_menu.html'


class SubMenuPageView(ListView):
    template_name = 'items_menu.html'
    context_object_name = 'menu'

    def get_queryset(self):
        menu_url = self.kwargs.get('menu_url')

        return MenuItem.objects.filter(
            Q(menu__url=menu_url) | Q(parent__url=menu_url)
        )

from django import template


from ..models import Menu


register = template.Library()


@register.simple_tag()
def draw_menu(menu_name):
    return Menu.objects.filter(name=menu_name)

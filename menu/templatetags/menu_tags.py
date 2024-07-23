from django import template
from menu.models import MenuItem
from django.urls import resolve

register = template.Library()


def build_menu(menu_name, current_url):
    items = MenuItem.objects.filter(menu_name=menu_name)
    root_items = items.filter(parent=None)
    print(root_items)

    def render_item(item, is_active):
        children = items.filter(parent=item)
        has_children = children.exists()
        url = resolve(current_url)

        return {
            'item': item,
            'is_active': is_active,
            'children': children,
            'has_children': has_children,
        }

    def get_menu_structure():
        menu_structure = []
        for item in root_items:
            is_active = item.url == current_url
            menu_structure.append(render_item(item, is_active))
        return menu_structure

    return get_menu_structure()


@register.simple_tag(takes_context=True)
def render_menu(context, menu_name):
    current_url = context['request'].path
    return build_menu(menu_name, current_url)

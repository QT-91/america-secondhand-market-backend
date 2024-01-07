from wagtail import hooks
from wagtail.admin.menu import MenuItem
from django.urls import reverse
from django.urls import path
from django.http import HttpResponse


def admin_view(request):
    return HttpResponse(
        "I have approximate knowledge of many things!",
        content_type="text/plain")


@hooks.register('register_admin_urls')
def urlconf_time():
    return [
        path('../django-admin/', admin_view, name='django-admin'),
        path('../django-admin/socialaccount/socialapp/', admin_view, name='social-login-settings'),
        path('../api/docs', admin_view, name='ninja-api'),
    ]


@hooks.register('construct_settings_menu')
def hide_and_register_settings_menu_item(request, menu_items):
    
    groups = request.user.groups.values_list()
    groups = [group for _, group in groups]

    submenu1 = MenuItem('Social Login', reverse('social-login-settings'), icon_name='password', order=800)
    submenu2 = MenuItem('Django Admin', reverse('django-admin'), icon_name='cogs', order=900)
    submenu3 = MenuItem('Ninja API', reverse('ninja-api'), icon_name='link', order=1000)
    menu_items.extend([submenu1, submenu2, submenu3])
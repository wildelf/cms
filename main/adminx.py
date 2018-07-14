#! -*- coding:utf-8 -*-
import datetime
import logging

from django.contrib.auth.models import Group, Permission, User
from django.db import connection
from django.db.models import Count
from django.forms import Media
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _, ugettext

import socket

from main.models import SiteUser, SiteGroup, SitePermission,Article

from xadmin.models import Log
import xadmin
from xadmin.plugins.auth import UserAdmin, GroupAdmin
from xadmin.views import CommAdminView

logger = logging.getLogger(__name__)

class MainXadmin(object):
    hidden_menu = True


class GlobalSetting(object):
    menu_style = 'accordion'  # 'default'#default'#'accordion'
    show_bookmarks = False
    site_title = u'官网内容管理平台'
    site_footer = u'深圳市金未来信息技术有限公司'
    system_version = "V1.0"
    global_add_models = []
    enable_themes = True
    use_bootswatch = True


    def get_site_menu(self):
        return (
            {'title': '工作台', 'url': '/xadmin/', 'icon': 'shouye'},

            {'title': '内容管理', 'icon': 'fa fa-list', 'menus': (
                # {'title': '主页', 'perm': self.get_model_perm(Index, 'view'), 'icon': 'fa fa-users',
                #  'url': self.get_model_url(Index, 'changelist')},
            )},

            {'title': '历史查询', 'icon': 'fa fa-list', 'menus': (

            )},

            {'title': '日志管理', 'icon': 'fa fa-ticket', 'menus': (

            )},

        )


xadmin.site.register(CommAdminView, GlobalSetting)




class SiteUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)
    style_fields = {'user_permissions': 'm2m_transfer'}
    model_icon = 'fa fa-user'
    relfield_style = 'fk-ajax'
    # list_display = ('name','status',)
    # object_list_template = "xadmin/newproduct.html"
    # add_form_template = 'xadmin/model_form.html'   # newproduct.html'
    # add_form_template = 'xadmin/newproduct.html'
    # form = ETHProductForm


class SiteGroupAdmin(GroupAdmin):
    pass


class CGroupAdmin(object):
    list_display = ('name',)
    ordering = ('name',)





class SitePermissionAdmin(object):
    pass



class DashboardModelAdmin(object):
    pass



# xadmin.site.unregister(SiteUser)
# xadmin.site.unregister(Permission)
# xadmin.site.register(SitePermission, SitePermissionAdmin)
# xadmin.site.unregister(Group)
xadmin.site.register(Article)

# xadmin.site.register(SiteGroup, SiteGroupAdmin)





# -*- coding:utf8 -*-

import xadmin
from xadmin import views                # 导入xadmin的views

from .models import Users, Email, Banner


class BasdSetting(object):              # 主题管理器
    enable_themes = True                # 使用主题
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView, BasdSetting)      # 将主题管理器绑定views.BaseAdminView注册


class GlobalSettings(object):                               # 头部系统名称和底部版权管理器
    site_title = '人才教育管理系统'                              # 头部系统名称
    site_footer = '人才教育管理系统，人才教育公司版权所有'             # 底部版权
    menu_style = 'accordion'                                # 设置数据管理导航折叠，以每一个app为一个折叠框
xadmin.site.register(views.CommAdminView, GlobalSettings)   # 头部系统名称和底部版权管理器绑定views.CommAdminView注册



class UsersAdmin(object):               # 自定义用户信息数据表管理器类
    # 设置xadmin后台显示字段
    list_display = ['username', 'password', 'nick_name', 'gender', 'email', 'address', 'mobile',
                    'first_name', 'last_name', 'is_active', 'birday', 'last_login', 'date_joined']
    # 设置xadmin后台搜索字段，注意：搜索字段如果有时间类型会报错
    search_fields = ['username', 'password', 'nick_name', 'gender', 'email', 'address', 'mobile']
    # 设置xadmin后台过滤器帅选字段，时间用过滤器来做
    list_filter = ['username', 'password', 'nick_name', 'gender', 'email', 'address', 'mobile',
                    'first_name', 'last_name', 'is_active', 'birday', 'last_login', 'date_joined']
xadmin.site.register(Users, UsersAdmin)     # 将户信息数据表注册到xadmin后台显示


class EmailAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']
xadmin.site.register(Email, EmailAdmin)


class BannerAdmin(object):
    list_display = ['title', 'index', 'image', 'url', 'add_time']
    search_fields = ['title', 'index', 'image', 'url']
    list_filter = ['title', 'index', 'image', 'url', 'add_time']
xadmin.site.register(Banner, BannerAdmin)
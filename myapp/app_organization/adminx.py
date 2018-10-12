# -*- coding:utf8 -*-
import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):               # 自定义数据表管理器类

    # 设置xadmin后台显示字段
    list_display = ['name', 'desc', 'add_time']

    # 设置xadmin后台搜索字段，注意：搜索字段如果有时间类型会报错
    search_fields = ['name']

    # 设置xadmin后台过滤器帅选字段，时间用过滤器来做
    list_filter = ['name', 'desc', 'add_time']
xadmin.site.register(CityDict, CityDictAdmin)     # 将数据表注册到xadmin后台显示


class CourseOrgAdmin(object):
    list_display = ['user', 'desc', 'click', 'fav_nums', 'image', 'address', 'city', 'add_time']
    search_fields = ['name']
    list_filter = ['user', 'desc', 'click', 'fav_nums', 'image', 'address', 'city', 'add_time']
xadmin.site.register(CourseOrg, CourseOrgAdmin)


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click', 'fav_nums', 'add_time']
    search_fields = ['name']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click', 'fav_nums', 'add_time']
xadmin.site.register(Teacher, TeacherAdmin)
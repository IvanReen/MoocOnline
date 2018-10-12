# -*- coding:utf8 -*-
import xadmin

from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):               # 自定义数据表管理器类

    # 设置xadmin后台显示字段
    list_display = ['name', 'mobile', 'course_name', 'add_time']

    # 设置xadmin后台搜索字段，注意：搜索字段如果有时间类型会报错
    search_fields = ['name']

    # 设置xadmin后台过滤器帅选字段，时间用过滤器来做
    list_filter = ['name', 'mobile', 'course_name', 'add_time']
xadmin.site.register(UserAsk, UserAskAdmin)     # 将数据表注册到xadmin后台显示


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']
xadmin.site.register(CourseComments, CourseCommentsAdmin)


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']
xadmin.site.register(UserFavorite, UserFavoriteAdmin)


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message']
    list_filter = ['user', 'message', 'has_read', 'add_time']
xadmin.site.register(UserMessage, UserMessageAdmin)


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user']
    list_filter = ['user', 'course', 'add_time']
xadmin.site.register(UserCourse, UserCourseAdmin)
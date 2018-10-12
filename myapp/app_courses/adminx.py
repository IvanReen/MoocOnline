# -*- coding:utf8 -*-
import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):               # 自定义数据表管理器类

    # 设置xadmin后台显示字段
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']

    # 设置xadmin后台搜索字段，注意：搜索字段如果有时间类型会报错
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']

    # 设置xadmin后台过滤器帅选字段，时间用过滤器来做
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']
xadmin.site.register(Course, CourseAdmin)     # 将数据表注册到xadmin后台显示


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['name']
    list_filter = ['course__name', 'name', 'add_time']      # course__name 表示通过course外键字段查询关联表里的name字段
xadmin.site.register(Lesson, LessonAdmin)


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['name']
    list_filter = ['lesson', 'name', 'add_time']
xadmin.site.register(Video, VideoAdmin)


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['name']
    list_filter = ['course', 'name', 'download', 'add_time']
xadmin.site.register(CourseResource, CourseResourceAdmin)
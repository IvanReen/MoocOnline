# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models        # 导入models对象


class Users(models.Model):       # 创建类必须继承models.Model，类名将是在数据库里的表名称
    password = models.CharField(max_length=128, verbose_name='密码', default='', blank=False)         # 密码字段，长度128，默认值为空字符，前端不允许用户输入空
    last_login = models.DateTimeField(verbose_name='登录日期', null=True)                           # 允许为空
    is_superuser = models.BooleanField(max_length=1, verbose_name='用户身份', name=False)
    username = models.CharField(max_length=150, verbose_name='用户名', null=False, blank=False)
    first_name = models.CharField(max_length=30, verbose_name='拓展1', null=False)
    last_name = models.CharField(max_length=30, verbose_name='拓展2', null=False)
    email = models.EmailField(max_length=254, verbose_name='邮箱', null=False, blank=False)
    is_staff = models.BooleanField(max_length=1, verbose_name='是否是员工', null=False)
    is_active = models.BooleanField(max_length=1, verbose_name='是否激活', null=False)
    date_joined = models.DateTimeField(verbose_name='注册日期', null=True)
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default='')
    birday = models.DateField(verbose_name='生日', null=True)
    gender = models.CharField(max_length=3, verbose_name='性别', choices=(("male", "男"), ("female", "女")), default='male')
    address = models.CharField(max_length=100, verbose_name='地区', default='')
    mobile = models.CharField(max_length=11, verbose_name='手机', null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/%m', verbose_name='头像', default='image/default.png', max_length=100)

    class Meta:
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name


class Email(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(max_length=10, choices=(('register', '注册'), ('forget', '找回密码')), verbose_name='邮箱验证类型')
    send_time = models.DateTimeField(verbose_name='生成时间', default=datetime.now)

    class Meta:
        verbose_name = '用户邮箱验证码表'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='轮播图标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图片', max_length=100)  # 图片路径banner/%Y/%m  /年/月
    url = models.URLField(max_length=200, verbose_name='轮播图访问地址')
    index = models.ImageField(default=100, verbose_name='轮播图顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='轮播图添加时间')

    class Meta:
        verbose_name = '网站轮播图表'
        verbose_name_plural = verbose_name
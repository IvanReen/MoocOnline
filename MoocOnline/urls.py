from django.conf.urls import url, include                   # 导入django自在的include逻辑
from django.contrib import admin
from django.views.generic import TemplateView               # 导入django自带的TemplateView逻辑

import xadmin                                               # 导入xadmin

from app_users.views import deng_lu, zhu_ce, active_code, logout                 # 导入登录逻辑处理类

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url(r'^index.html', TemplateView.as_view(template_name='index.html'), name='index'),

    url(r'^register.html', zhu_ce.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls'), name='captcha'),
    url(r'^active/(?P<active_de>.*)/$', active_code.as_view(), name="user_active"),


    url(r'^login.html', TemplateView.as_view(template_name='login.html'), name='login'),
    url(r'^deng_lu', deng_lu.as_view(), name='deng_lu'),
    url(r'^logout', logout.as_view(), name='deng_lu'),
]
from django.conf.urls import url, include                   # 导入django自在的include逻辑
from django.contrib import admin
from django.views.generic import TemplateView               # 导入django自带的TemplateView逻辑

import xadmin                                               # 导入xadmin


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
]
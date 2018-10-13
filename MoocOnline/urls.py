# from django.contrib import admin
from django.urls import path

import xadmin                                               # 导入xadmin


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
]
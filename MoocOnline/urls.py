# from django.contrib import admin
from django.urls import path

import xadmin                             # 导入xadmin
from users.views import IndexView, LoginView, LogoutView, RegisterView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', IndexView.as_view(), name="index"),
    # 基于类方法实现登录,这里是调用它的方法
    path('login/', LoginView.as_view(), name="login"),

# 退出功能url
    path('logout/', LogoutView.as_view(), name="logout"),

# 注册url
    path("register/", RegisterView.as_view(), name = "register" ),
]
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
# 首页view
from django.urls import reverse
from django.views.generic.base import View

from courses.models import Course
from organization.models import CourseOrg
from users.forms import LoginForm
from users.models import Banner


class IndexView(View):
    def get(self,request):
        # 取出轮播图
        all_banner = Banner.objects.all().order_by('index')[:5]
        # 正常位课程
        courses = Course.objects.filter(is_banner=False)[:6]
        # 轮播图课程取三个
        banner_courses = Course.objects.filter(is_banner=True)[:3]
        # 课程机构
        course_orgs = CourseOrg.objects.all()[:15]
        return render(request, 'index.html', {
            "all_banner":all_banner,
            "courses":courses,
            "banner_courses":banner_courses,
            "course_orgs":course_orgs,
        })


class LoginView(View):
    # 直接调用get方法免去判断
    def get(self, request):
        # render就是渲染html返回用户
        # render三变量: request 模板名称 一个字典写明传给前端的值
        redirect_url = request.GET.get('next', '')
        return render(request, "login.html", {
            "redirect_url": redirect_url
        })

    def post(self, request):
        # 类实例化需要一个字典参数dict:request.POST就是一个QueryDict所以直接传入
        # POST中的usernamepassword，会对应到form中
        login_form = LoginForm(request.POST)

        # is_valid判断我们字段是否有错执行我们原有逻辑，验证失败跳回login页面
        if login_form.is_valid():
            # 取不到时为空，username，password为前端页面name值
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")

            # 成功返回user对象,失败返回null
            user = authenticate(username=user_name, password=pass_word)

            # 如果不是null说明验证成功
            if user is not None:
                # 只有当用户激活时才给登录
                if user.is_active:
                    # login_in 两参数：request, user
                    # 实际是对request写了一部分东西进去，然后在render的时候：
                    # request是要render回去的。这些信息也就随着返回浏览器。完成登录
                    login(request, user)
                    # 跳转到首页 user request会被带回到首页
                    # 增加重定向回原网页。
                    redirect_url = request.POST.get('next', '')
                    if redirect_url:
                        return HttpResponseRedirect(redirect_url)
                    # 跳转到首页 user request会被带回到首页
                    return HttpResponseRedirect(reverse("index"))
                # 即用户未激活跳转登录，提示未激活
                else:
                    return render(
                        request, "login.html", {
                            "msg": "用户名未激活! 请前往邮箱进行激活"})
            # 仅当用户真的密码出错时
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误!"})
        # 验证不成功跳回登录页面
        # 没有成功说明里面的值是None，并再次跳转回主页面
        else:
            return render(
                request, "login.html", {
                    "login_form": login_form})


class LogoutView(View):
    def get(self, request):
        # django自带的logout
        logout(request)
        # 重定向到首页,
        return HttpResponseRedirect(reverse("index"))
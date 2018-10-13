from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
# 首页view
from django.urls import reverse
from django.views.generic.base import View

from courses.models import Course
from operation.models import UserMessage
from organization.models import CourseOrg
from users.forms import LoginForm, RegisterForm
from users.models import Banner, UserProfile
from utils.email_send import send_register_eamil


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


# 注册功能的view
class RegisterView(View):
    # get方法直接返回页面
    def get(self, request):
        # 添加验证码
        register_form = RegisterForm()
        return render(
            request, "register.html", {
                'register_form': register_form})

    def post(self, request):
        # 实例化form
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # 这里注册时前端的name为email
            user_name = request.POST.get("email", "")
            # 用户查重
            if UserProfile.objects.filter(email=user_name):
                return render(
                    request, "register.html", {
                        "register_form": register_form, "msg": "用户已存在"})
            pass_word = request.POST.get("password", "")

            # 实例化一个user_profile对象，将前台值存入
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name

            # 默认激活状态为false
            user_profile.is_active = False

            # 加密password进行保存
            user_profile.password = make_password(pass_word)
            user_profile.save()

            # 写入欢迎注册消息
            user_message = UserMessage()
            user_message.user = user_profile.id
            user_message.message = "欢迎注册mtianyan慕课小站!! --系统自动消息"
            user_message.save()
            # 发送注册激活邮件
            send_register_eamil(user_name, "register")

            # 跳转到登录页面
            return render(request, "login.html", )
        # 注册邮箱form验证失败
        else:
            return render(
                request, "register.html", {
                    "register_form": register_form})
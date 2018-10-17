# MoocOnline
使用Python3.x与Django2.0.1开发的在线教育平台网站: http://www.imooc.pythonanywhere.com

## Quick Start

```
$ git clone https://github.com/smallren101/MoocOnline.git
$ cd MoocOnline
$ pip install -r requirements.txt
$ python manage.py runserver
```

use the address: http://127.0.0.1:8000/

## Contents：

1. 先安装mysql
   安装的时候需要密码设置为admin


修改settings.py文件
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "mooconline",
        'USER': 'root',
        'PASSWORD': "admin",
        'HOST': "127.0.0.1"
    }
}
```


2. 创建数据库
```
$ create database mooconline charset='utf8';
```

3. navicat 导入sql文件

4. pip install -r req.txt 安装依赖包

5. 然后pip install mysqlclient-1.3.12-cp36-cp36m-win_amd64.whl 安装mysqlclient驱动

6. 创建管理员账户
```
$ python manage.py createsuperuser
```
7. 收集静态文件
```
$ python manage.py collectstatic --noinput
$ python manage.py runserver
```

8. 浏览器中输入 127.0.0.1:8000访问
## 求打赏鼓励

很高兴我的项目代码对你有帮助，请我吃包辣条吧！

微信打赏:

![Image text](https://raw.githubusercontent.com/smallren101/MoocOnline/master/static/images/code.jpg)

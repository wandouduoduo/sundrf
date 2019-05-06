drf + xadmin + vue 打造生鲜平台

python版本3.6.4

安装方法：

1,安装所用模块

pip install -r requirement.txt

2,更改配置

sundjango/settings.py中

DATABASES配置改为自己mysql地址

EMAIL配置改为自己email的地址

3,生成数据表

python manager.py makemigrations

python manager.py migrate

4, 运行

python manager.py runserver

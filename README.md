# s12bbs
# Webchat
project webchat and bbs

### 运行环境
    django 1.9.5   pymysql   mysql

### 运行方法
    1.  进入mysql创建数据库 day20_s12bbs
        create database day20_s12bbs;
    2. 创建表单
        python3 manage.py migrate 
    3. 创建超级用户
        python3 manage.py createsuperuser
        输入用户名和密码
    4. 进入 admin 管理界面创建 板块 
    
    5. 运行
        python3 manage.py runserver
### 实现功能
    基于mysql数据库，利用bootstrap实现响应式布局以及附带有web聊天室，编辑和添加文档功能。
    后续目标是改进聊天室以及实现点赞和阅读量功能。

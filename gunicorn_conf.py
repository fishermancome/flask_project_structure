"""
gunicorn  启动命令 gunicorn wsgi:app -c gunicorn_conf.py
在centos下面gunicorn 命令找不到需制作软连接 或者使用gunicorn所在路径启动
"""

# 用于控制errorlog的信息级别，可以设置为debug、info、warning、error、critical
loglevel = 'debug'

# 监听IP放宽，以便于Docker之间、Docker和宿主机之间的通信
bind = "0.0.0.0:5001"
pidfile = "log/gunicorn.pid"
daemon = True
# 访问日志，可以通过access_log_format设置访问日志格式
accesslog = "log/access.log"
# 设置gunicorn访问日志格式，错误日志无法设置
# access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
errorlog = "log/debug.log"

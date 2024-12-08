from win10toast import ToastNotifier
#引入该库用于进行网络的访问请求
import requests
import os
import time
import socket
def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
ip_adress = get_host_ip()

print(ip_adress)

login_IP = f'http://10.1.99.100:801/eportal/portal/login?callback=dr1003&login_method=1&user_account="账户"user_password="密码"&wlan_user_ip&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=10.1.1.1&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=9914&lang=zh'

not_sign_in_title = '协议认证成功'
result_return = '密码错误'
signed_in_title = '已经在线'

already_icon = "Check.ico"
success_icon = "Check.ico"
false_icon = "Cross.ico"

try:
    r = requests.get(login_IP,
                    timeout = 1)
    req = r.text
    print(req)
except:
    req = 'False'


if signed_in_title in req:
    ToastNotifier().show_toast(title = "该设备已经登录",
               msg = "校园网状态",
               icon_path = already_icon,
               duration = 5,
               threaded = False)
    time.sleep(2)
    # os._exit(0)

elif not_sign_in_title in req:
    ToastNotifier().show_toast(title="登录成功",
                               msg="校园网状态",
                               icon_path=success_icon,
                               duration=5,
                               threaded=False)
    time.sleep(2)
    # os._exit(0)

else:
    ToastNotifier().show_toast(title="登录失败",
                               msg="校园网状态",
                               icon_path=false_icon,
                               duration=5,
                               threaded=False)
    time.sleep(2)
    # os._exit(0)

ToastNotifier().show_toast(
    title = "登录信息",
    msg = f"您的ip地址是:\n{ip_adress}\n您返回的状态码是:\n{req}",
icon_path = already_icon,
               duration = 5,
               threaded = False
)
os._exit(0)


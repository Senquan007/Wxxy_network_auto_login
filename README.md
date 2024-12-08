# Wxxy_network_auto_login
用于无锡学院的学生自动登录校园网的程序。
无锡学院校园网的认证服务是由 ([Dr.COM城市热点-新一代身份认证计费平台 (drcom.com.cn)](https://www.drcom.com.cn/)提供。

其认证网页请求方法采用的是 `GET` 方式，因此以下方法仅针对 `GET` 方式，对于 `POST` 请求方法的校园网认证无法使用。

![image](https://github.com/user-attachments/assets/75040c66-e195-4321-adef-e8ce5a4a4a4a)


## 方法一：（最为简单，仅针对 WxUer)

### 使用方法：

- 仅需找到对应的`URL`
- 在相应位置更换为自己的账号密码
- 将链接复制到浏览器中，访问该链接
- **手机电脑都可使用**

```yaml
# 出现以下提示代表成功登录
dr1003({"result":0,"msg":"IP: **.**.**.** 已经在线！","ret_code":2});
# or
dr1003({"result":1,"msg":"Portal协议认证成功！"});#

# 若出现以下提示则代表失败
dr1003({"result":0,"msg":"AC认证失败"});

```

### 该链接为运营商为 `无锡学院`

http://10.1.99.100:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=填写账号&user_password=填写密码&wlan_user_ip&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=3043&lang=zh

### 该链接为运营商为 `中国移动`

http://10.1.99.100:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=填写账号@cmcc&user_password=填写密码&wlan_user_ip&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=2098&lang=zh

### 该链接为运营商为 `中国联通`

http://10.1.99.100:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=填写账号@unicom&user_password=填写密码&wlan_user_ip&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=2098&lang=zh

### 该链接为运营商为 `中国电信`

http://10.1.99.100:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=填写账号@telecom&user_password=填写密码&wlan_user_ip&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=2098&lang=zh

### 对 `URL` 进行分析

| 参数名 | 内容 | 说明 |
| --- | --- | --- |
| 基本URL | http://10.1.99.100:801/eportal/portal/login | 登录页面的URL |
| callback | dr1003 | JSONP回调函数名称 |
| login_method | 1 | 登录方法类型 |
| user_account | ******* | 用户账号（运营商选择为无锡学院） |
|  | *******@cmcc | 用户账号（运营商选择为中国移动） |
|  | *******@unicom | 用户账号（运营商选择为中国联通） |
|  | *******@telecom | 用户账号（运营商选择为中国电信） |
| user_password | ******** | 用户密码 |
| wlan_user_ip |  | 用户IP地址（可留空） |
| wlan_user_ipv6 |  | 用户IPv6地址（空字段） |
| wlan_user_mac | 000000000000 | 用户MAC地址 |
| wlan_ac_ip |  | 接入控制器IP地址（空字段） |
| wlan_ac_name |  | 接入控制器名称（空字段） |
| jsVersion | 4.1.3 | 使用的JavaScript版本 |
| terminal_type | 1 | 设备类型 |
| lang | zh-cn | 语言设置（简体中文） |
| v | 3043 | 版本号 |


---

## 方法二：使用`Python`程序

****Python程序较为麻烦，主要牵扯第三方库以及环境的安装***

在使用此代码之前，需使用 `pip` 命令，安装对应的第三方库

### 使用提供的现成的代码，请在 line 32 处的位置填写相关信息

```python
#此IP的获取请参考方法2
login_IP = f'http://10.1.99.100:801/eportal/portal/login?callback=dr1003&login_method=1&user_account="填写你的账号@选择运营商"&user_password="你的密码"&wlan_user_ip={ip_adress}&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=10.1.1.1&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=9914&lang=zh'
```



**_经过实验发现，请求参数中的ip地址不是关键认证数据，可以忽略或删除_**

## 方法三：使用`Shell`命令进行登陆操作

****该步骤有入手难度，需要有一定`Linux`基础***

---

****声明：以下内容系为转载，有所改动***

**文章作者:** [JoyerLiu](mailto:undefined)

**文章链接:** https://blog.joyer.top/2021-12-03-3/

**版权声明:** 本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可协议。转载请注明来自 [Joyer的博客](https://blog.joyer.top/)！

---

### **第一步，获取GET url**

使用浏览器（最好是 Chrome 的内核浏览器）打开你的校园网链接，如本校的就是[南京信息工程大学滨江学院/无锡学院校园网登录界面](http://10.1.99.100/)。

按`F12`打开开发人员工具，选择`网络（NetWork）`，勾选`保存日志（Preserve log）`，并在页面中进行正常登陆。

![image](https://github.com/user-attachments/assets/3d7b1341-daad-46a3-bdc7-3bc7b6211215)
![image](https://github.com/user-attachments/assets/9bbb8314-94e4-4658-8079-06dfa2b596ee)


登录完成后，在开发者工具中的`网络（NetWork）`子页中寻找`请求url（GET url）`

大致长这个样子

```yaml
http://10.1.99.100:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=,0,账号@cmcc&user_password=密码&wlan_user_ip=内网IP&wlan_user_ipv6=&wlan_user_mac=设备MAC&wlan_ac_ip=10.1.1.1&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=9960&lang=zh
```

把这个url记下来，随后退出校园网登录，我们要测试这个url是否能够使用。

以Windows11系统为例，我们需要在`系统设置`-`网络和Internet`-`高级网络设置`-`硬件和连接属性` 中查找用来测试的设备的内网IP（以本校为例一般是10.x.x.x）（Windows这货藏重要信息是越来越能藏了），其他系统的设备请自行解决获取内网IP，网络上有很多办法。

获取到IP以后，我们要替换url中的`wlan_user_ip=`后面的IP（为了防止IP自动更换），并把它粘贴到浏览器网址栏中，敲击回车，如果显示登陆成功，恭喜你，这篇教程对你有用，请继续向下看，如果失败了请转到文章开头提到的甲烷气瓶博客的文章。

解决完请求url，我们要开始操作路由器获取它的内网IP了。

### **第二步，获取路由器内网IP**

为什么要获取内网IP呢，直接填入路由器的内网IP不行吗？因为校园网给予设备的IP是动态的，并且其生命只有一天甚至更少，所以我们每登录一次就要获取一次内网IP。

将你的路由器连上校园网，并用一台设备连接到路由器以便对路由器进行操作。进入你的路由器后台终端，也就是常说的黑底白字看起来贼高端的命令行窗口。一般来说路由器后台网页中可以找得到，您也可以用通过ssh登录进入路由器后台，但无论是哪种方式，切记一定要以管理员账号登陆，默认是root。

大部分的以Linux开发的系统都可以使用 `ip addr` 这条命令获取到设备的大部分网络信息，如果没找到，请尝试 `ifconfig`，都能获取到内网ip。

![image](https://github.com/user-attachments/assets/f62bcc48-b261-482d-a459-bb39c9376a21)


随后，请在密密麻麻的字行间找到属于您的路由器的内网ip，我们就只要它，请您记住这个位置，我们要开始截取它了。

这里给出我截取路由器内网ip地址的命令，您可以按照这个命令进行参考。

```yaml
 ip addr | grep eth0| grep inet | awk '{print $2}' | cut -d "/" -f 1
```

正所谓授人以鱼不如授人以渔，并且您需要按照您路由器的自身情况参与到构成专属于您的路由器的截取内网IP的命令中来，下面我来仔细讲讲用这行命令是如何截取出我们需要的内网IP的， 请看以下表格中对应的命令的具体作用，但羞于文笔不好，如果有不理解的可以前往表格中所指的链接查看更多（菜鸟教程对于学习计算机相关的朋友来说真是个好东西）。

请注意您的命令格式，使用 | 将两个命令隔开，“|”两边带有空格，并且第一个命令一定是`ip addr`（也就是您需要截取的内容的获取命令）

一个例子：

**plaintext**

| 命令 | grep inet | awk ‘{print $2}’ | cut -d “/“ -f 1 |
| --- | --- | --- | --- |
| 作用 | 定位到关键词”inet”的所在行 | 截取出当行的第2个字符块 | 截取出以”/“字符分割的前字符块 |
| 详细 | [菜鸟教程Linux grep](https://www.runoob.com/linux/linux-comm-grep.html) | [菜鸟教程Linux awk](https://www.runoob.com/linux/linux-comm-awk.html) | [菜鸟教程Linux cut](https://www.runoob.com/linux/linux-comm-cut.html) |

首先第一个，`grep inet`的作用，从字段中找到含有此关键词的对应行，这里我使用连接了校园网的网卡名称进行定位。

定位的结果：

```bash
		inet 127.0.0.1/8 scope host lo
    inet6 ::1/128 scope host 
    inet 192.168.50.115/24 brd 192.168.50.255 scope global eth0
    inet6 fe80::b079:86ff:fe91:7387/64 scope link 
    inet 192.168.11.1/24 brd 192.168.11.255 scope global br-lan
    inet6 fe80::b079:86ff:fe91:7388/64 scope link 
    inet6 fe80::4a8f:4cff:fef9:37df/64 scope link 
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
    inet6 fe80::42:a9ff:fe55:346a/64 scope link 
    inet6 fe80::b:d7ff:fe63:2678/64 scope link 
    inet 198.18.0.1/16 scope global utun
    inet6 fe80::94ee:f64a:3bd6:3107/64 scope link stable-privacy 
```

第二个，`grep eth0`，不再赘述，这里是直接截取到有内网IP的那一行。

截取结果：

```yaml
 inet 192.168.50.115/24 brd 192.168.50.255 scope global eth0
```

第三个，`awk '{print $2}'`,截取出第二个子块，也就是 inet 后面的IP，如果是`awk '{print $1}'`，截取出来的则是 inte 。

截取结果：

```yaml
10.2.91.138/18
```

还没完，我们还需要把子网掩码去掉，也就是‘/’后面的内容，第四个命令`cut -d "/" -f 1` ，这是个带有参数的命令，作用是截取“/”之前的文字段，如果 -f 的参数写的是 2，你将得到子网掩码 18。

```yaml
10.2.91.138
```

如果您如上成功写出您的命令并以此获取内网IP，那么请保存好这条命令。恭喜你，第二步的工作完成了，我们终于可以开始编写Shell脚本了！

### **第三步，编写脚本**

新建一个文本文档，用 Notepad++ 打开它，当然其他文本编辑器也是可以的。

这里给出我的脚本，仅供参考。

```yaml
CURRENT_IP=$(ip addr | grep eth0.1 | grep inet | awk '{print $2}' | cut -d "/" -f 1)
#linux
curl 'http://10.1.99.100:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=,0,账号@cmcc&user_password=密码&wlan_user_ip='$CURRENT_IP'&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=10.1.1.1&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=9960&lang=zh'
```

第一行定义一个变量 `CURRENT_IP` ，我们用它来存放内网IP，等号后面输入 $() （括号里放第二步您成功截取路由器IP的命令）。

第二行执行curl，后面使用单引号括住您在第一步能用来成功登录校园网的请求 url，并且将其中`wlan_user_ip`等号后面的内容改成变量`'$CURRENT_IP'`Ctrl+S保存。

这样一来，Shell 脚本也编好了。

### **第四步，上传路由器**

```bash
#创建存放shell命令的文件
mkdir /etc/drcom
#创建一个sh文件，用来存放命令
vi /etc/drcom/drcom.sh
#按下 “i” 键，进入输入模式
#将代码粘贴进去
#按 “ESC” ,输入“:wq ”，退出编辑

#输入命令
sh /etc/drcom/drcom.sh

# 出现以下提示代表成功登录
dr1003({"result":0,"msg":"IP: 10.2.92.120 已经在线！","ret_code":2});
# or
dr1003({"result":1,"msg":"Portal协议认证成功！"});#

# 若出现以下提示则代表失败
dr1003({"result":0,"msg":"AC认证失败"});

```

### **第五步，添加计划任务**

1. 首先，使用SSH或其他方式登录到您的OpenWrt设备。
2. 使用文本编辑器（如`vi`或`nano`）编辑`/etc/crontabs/root`文件。您可以使用以下命令之一：
    
    ```bash
    vi /etc/crontabs/root
    # 或者
    nano /etc/crontabs/root
    
    ```
    
3. 在文件中添加一行来设置cron作业。格式如下：
    
    ```bash
    #表示每天早上6点运行该命令
    0 6 * * * /etc/drcom/drcom.sh
    
    ```
    
    这里，`0 6 * * *`指定了作业的执行时间（分钟、小时、日、月、星期几），`/path/to/your/script.sh`是您的脚本路径。请确保将`/path/to/your/script.sh`替换为您的脚本实际路径。
    
4. 保存并关闭文件。如果您使用的是`vi`，可以通过按`ESC`键，然后输入`:wq`（写入并退出）来完成。如果您使用的是`nano`，可以通过按`Ctrl+O`，回车保存更改，然后按`Ctrl+X`退出。

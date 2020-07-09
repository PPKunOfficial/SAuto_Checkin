# 一款自动签到程序
# 前言
这个程序本身定位是自用,因为本人需要住宿.如今开源,请勿滥用!
# 使用方法
先把'.github/workflows/blank.yml'里的注释去掉,并且根据注释来修改自己的代码

```yaml
name: Auto_Checkin
on:
#  schedule:
#    - cron: 0 16 * * *
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8]
    steps:
    - name: Install_Python
      run: |
        sudo apt install python3
        sudo apt install python3-pip
        wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate
        python3 ./get-pip.py
        pip3 install requests
        pip3 install fake-useragent
        git clone  #git地址
    - name: Run_Python_Script
      run: |
        cd #目录名
        python3 checkin.py
```

cron指的是crontab,也就是定时任务,请按照cron表达式格式编写

然后创建"accouts.json",如果使用我的模板或者fork了我的仓库一般都会带模板json,请把模板的"xxx"改成与你对应的数据

```json
{
"sp": [ #列表,请不要改变列表名字(唯一标识符),按照示例一添加进列表,python运行时将循环列表
        {
            "name": "xxx", #名字
            "url": {
            "lu": "https://xxx/auth/login", #登录请求网址
            "cu": "https://xxx/user/checkin" #签到请求网址
            },
            "ac": {
            "u": "xxx", #用户名
            "p": "xxx" #密码
            }
        }
	]
}
```
# 申请适配

申请适配面板程序请提交"Issues",也可以通过邮件联系

pp520yo@gmail.com

# 目前支持
> sspanel

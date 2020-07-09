# .github/workflows/blank.yml请根据自己的需求进行调整
# 务必编写正确json，程序会自动循环sp里的列表
Json格式:

  {
    "sp":
    [
      {
      "name":"xxx", #机场名
      "url":
        {
          "lu":"https://xxx/auth/login", #登录网址
          "cu":"https://xxx/user/checkin" #签到网址
        },
      "ac":
        {
          "u":"xxx", #用户名
          "p":"xxx" #登陆密码
        }
      }
    ]
  }

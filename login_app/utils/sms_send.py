import urllib
from random import Random # 用于生成随机码
from login_app.models import PhoneVerifyRecord  # 邮箱验证model
import urllib.request as requ
# coding: utf-8
# 生成随机字符串


def random_str(randomlength=6):
    str = ''
    chars = '0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_sms(phone, send_type="register"):
    phone_record = PhoneVerifyRecord()  # 将给用户发的信息保存在数据库中
    code = random_str(6)
    phone_record.code = code
    phone_record.phone = phone
    phone_record.send_type = send_type
    # 接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
    # 账户注册：请通过该地址开通账户http://user.ihuyi.com/register.html
    # 注意事项：
    # （1）调试期间，请用默认的模板进行测试，默认模板详见接口文档；
    # （2）请使用 用户名 及 APIkey来调用接口，APIkey在会员中心可以获取；
    # （3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；
    # 用户名 查看用户名请登录用户中心->验证码、通知短信->帐户及签名设置->APIID
    account = "C97898079"
    # 密码 查看密码请登录用户中心->验证码、通知短信->帐户及签名设置->APIKEY
    password = "fd5d191c606e779beae51b85832a9f48"
    mobile = phone
    text = "您的验证码是：" + code + "。请不要把验证码泄露给其他人。"
    data = {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'}
    req = requ.urlopen(
        url='http://106.ihuyi.com/webservice/sms.php?method=Submit',
        data=urllib.parse.urlencode(data).encode(encoding='UTF8')
    )
    phone_record.save()
    content = req.read()
    print(content)

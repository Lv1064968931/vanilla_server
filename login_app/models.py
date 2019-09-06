from django.db import models


# Create your models here.

#用户模型
class User(models.Model):
    phone_num = models.CharField(max_length=11, unique=True, primary_key=True, verbose_name=u"手机号")
    password = models.CharField(max_length=256, verbose_name=u"密码")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_num

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = verbose_name

#验证码模型
class PhoneVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name=u"验证码")
    phone = models.CharField(max_length=11,verbose_name=u"手机号")

    send_type = models.CharField(verbose_name=u"验证码类型",max_length=10,choices=(("register", u"注册"), ("forget", u"找回密码")))
    send_time = models.DateTimeField(verbose_name=u"发送时间", auto_now_add=True)

    class Meta:
        verbose_name = u"手机验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.phone)


#词汇数据模型
class vocabulary(models.Model):
    id = models.CharField(max_length=255,primary_key=True,verbose_name=u"单词")
    alphabet = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    voice = models.CharField(max_length=255)
    word_type = models.CharField(max_length=255)

    def __unicode__(self):
        return self.id

    class Meta:
        verbose_name = u"词汇"
        verbose_name_plural =verbose_name

#名句数据模型
class Sentence(models.Model):
    senten = models.TextField(max_length=1000,verbose_name=u"名句")
    imag = models.ImageField(upload_to="imag_folder/",verbose_name='图片',null=True)

    def __unicode__(self):
        return self.senten

    class Meta:
        verbose_name = u"名句"
        verbose_name_plural = verbose_name

#用户数据模型
class Userdata(models.Model):
    phone_num = models.CharField(max_length=11,unique=True,primary_key=True,verbose_name=u"手机号")
    book_plan_title = models.CharField(max_length=255,verbose_name=u"单词书")
    book_plan_count = models.CharField(max_length=11,default="18",verbose_name=u"计划数")

    def __unicode__(self):
        return self.phone_num

    class Meta:
        verbose_name = u"用户数据"
        verbose_name_plural = verbose_name


#用户生词本模型
class Strangeword(models.Model):
    phone_num = models.CharField(max_length=11,verbose_name=u'手机号')
    word = models.CharField(max_length=255,verbose_name=u'单词')
    word_alphabet = models.CharField(max_length=255,verbose_name=u'音标')
    word_exp = models.CharField(max_length=255,verbose_name=u'释义')

    def __unicode__(self):
        return self.phone_num
    class Meta:
        verbose_name = u"生词本"
        verbose_name_plural = verbose_name


#用户打卡模型
class Clockingdata(models.Model):
    phone_num = models.CharField(max_length=11,unique=True,verbose_name=u'手机号')
    clock_day_count = models.CharField(max_length=255,default="0",verbose_name=u'打卡天数')
    word_total_count = models.CharField(max_length=255,default="0",verbose_name=u'记单词总数')

    def __unicode__(self):
        return self.phone_num
    class Meta:
        verbose_name = u'打卡数据'
        verbose_name_plural = verbose_name
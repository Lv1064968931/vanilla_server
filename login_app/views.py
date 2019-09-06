import random

from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

# Create your views here.

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from login_app.models import User, PhoneVerifyRecord, vocabulary, Sentence, Userdata, Strangeword, Clockingdata
from login_app.serializers import UserSerializer, VerifySerializer, VocabularySerializer, SentenceSerializer, \
    UserdataSerializer, StrangewordSerializer, ClockingdataSerializer
from login_app.utils.sms_send import send_register_sms


class UserSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VerifySet(viewsets.ModelViewSet):
    queryset = PhoneVerifyRecord.objects.all()
    serializer_class = VerifySerializer

class VocabularySet(viewsets.ModelViewSet):
    queryset = vocabulary.objects.all()
    serializer_class = VocabularySerializer

class SentenceSet(viewsets.ModelViewSet):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer

class UserdataSet(viewsets.ModelViewSet):
    queryset = Userdata.objects.all()
    serializer_class = UserSerializer

class StrangewordSet(viewsets.ModelViewSet):
    queryset = Strangeword.objects.all()
    serializer_class = StrangewordSerializer

class ClockingdataSet(viewsets.ModelViewSet):
    queryset = Clockingdata
    serializer_class = ClockingdataSerializer


#登录
def login(request):
    phone_num = request.POST.get('phone_num')
    password = request.POST.get('password')
    try:
        print("xxxxxx",phone_num)
        user = User.objects.get(phone_num=phone_num)
    except ObjectDoesNotExist:
        return HttpResponse("用户不存在")
    else:
        if password == user.password:
            return HttpResponse("登陆成功")
        else:
            return HttpResponse("用户名或密码错误")

#注册
def register(request):
    phone_num = request.POST.get('phone')
    password = request.POST.get('password')
    code = request.POST.get('code')
    user = User()
    clockingdata = Clockingdata()
    try:
        print("xxxx",phone_num)
        user = User.objects.get(phone_num=phone_num)
    except ObjectDoesNotExist:
        user.phone_num = phone_num
        user.password = password
        clockingdata.phone_num = phone_num
        try:
            code = PhoneVerifyRecord.objects.get(phone=phone_num).code
        except:
            return HttpResponse("验证码错误")
        else:
            user.save()
            clockingdata.save()
            return HttpResponse("注册成功")
    else:
        return HttpResponse("用户名重复")

#获取验证码
def get_phone_code(request):
    phone = request.POST.get('phone')
    print("xssax",phone)
    try:
        PhoneRecord = PhoneVerifyRecord.objects.get(phone=phone)
    except ObjectDoesNotExist:
        print('xxxxxx',)
        send_register_sms(phone, "register")
        return HttpResponse("已发送验证码")
    else:
        return HttpResponse("不可重复注册")

#取单词
@api_view(['POST', 'GET', 'DELETE'])
def fetch_random_word(request):
    if request.method == 'POST':
        randomcount = request.POST.get('randomcount')
        n = int(randomcount)
        i = random.randint(0,vocabulary.objects.all().count()-1)
        vocabularies = vocabulary.objects.all()[i:i+n]
        serializer = VocabularySerializer(vocabularies,many=True)
        print('xxxxxx', serializer.data)
        return Response(serializer.data,status=status.HTTP_200_OK)


#取名句
@api_view(['POST', 'GET', 'DELETE'])
def fetch_random_sentence(request):
    if request.method == 'POST':
        random_sentencecount = request.POST.get('random_sentencecount')
        n = int(random_sentencecount)
        senten = []
        a = 0
        while a<n:
            i = random.randint(0,
             Sentence.objects.all().count() - 1)
            senten.append(Sentence.objects.all()[i])
            a+=1
        senserializer = SentenceSerializer(senten,many=True)
        print('xxxxxx', senserializer.data)
        return Response(senserializer.data,status=status.HTTP_200_OK)


#上传用户数据
@api_view(['POST', 'GET', 'DELETE'])
def upload_userdata(request):
    if request.method == 'POST':
        phone_num = request.POST.get('phone_num')
        book_plan_title = request.POST.get('book_plan_title')
        book_plan_count = request.POST.get('book_plan_count')
        userdata = Userdata()
        try:
            userdata = Userdata.objects.get(phone_num = phone_num)
        except ObjectDoesNotExist:
            userdata.phone_num = phone_num
            userdata.save()
            return HttpResponse("添加用户成功")
        else:
            userdata.phone_num = phone_num
            userdata.book_plan_title = book_plan_title
            userdata.book_plan_count = book_plan_count
            userdata.save()
            return HttpResponse("上传成功")

#取出用户数据
@api_view(['POST', 'GET', 'DELETE'])
def download_userdata(request):
    if request.method == 'POST':
        phone_num = request.POST.get('phone_num')
        userdata = Userdata.objects.get(phone_num=phone_num)
        userdataserializer = UserdataSerializer(userdata)
        print('xxxxxx', userdataserializer.data)
        return Response(userdataserializer.data, status=status.HTTP_200_OK)


#上传用户生词
@api_view(['POST', 'GET', 'DELETE'])
def upload_strangeword(request):
    if request.method == 'POST':
        phone_num = request.POST.get('phone_num')
        word = request.POST.get('word')
        word_alphabet = request.POST.get('word_alphabet')
        word_exp = request.POST.get('word_exp')
        strangeword = Strangeword()

        strangeword.phone_num = phone_num
        strangeword.word = word
        strangeword.word_alphabet = word_alphabet
        strangeword.word_exp = word_exp
        strangeword.save()
        return HttpResponse("上传成功")

#下载用户生词
@api_view(['POST', 'GET', 'DELETE'])
def download_strangeword(request):
    if request.method == 'POST':
        phone_num = request.POST.get('phone_num')
        strangewords = Strangeword.objects.filter(phone_num=phone_num)
        strangewordserializer = StrangewordSerializer(strangewords,many=True)
        print('xxxxxx', strangewordserializer.data)
        return Response(strangewordserializer.data,status=status.HTTP_200_OK)

#上传用户打卡数据
@api_view(['POST', 'GET', 'DELETE'])
def upload_clockingdata(request):
    if request.method == 'POST':
        phone_num = request.POST.get('phone_num')
        clock_day_count = request.POST.get('clock_day_count')
        word_total_count = request.POST.get('word_total_count')
        clockingdata = Clockingdata()
        try:
            clockingdata = Clockingdata.objects.get(phone_num=phone_num)
        except ObjectDoesNotExist:
            clockingdata.phone_num = phone_num
            clockingdata.clock_day_count = "0"
            clockingdata.word_total_count = "0"
            clockingdata.save()
            return HttpResponse("添加用户成功")
        else:
            clockday = int(clock_day_count) + 1
            clockingdata.clock_day_count = str(clockday)
            clockingdata.word_total_count = str(int(clockingdata.word_total_count)+int(word_total_count))
            clockingdata.save()
            return HttpResponse("上传成功")

#取出用户打卡数据
@api_view(['POST', 'GET', 'DELETE'])
def download_clockingdata(request):
    if request.method == 'POST':
        phone_num = request.POST.get('phone_num')
        clockingdata = Clockingdata.objects.get(phone_num=phone_num)
        clockingdataserializer = ClockingdataSerializer(clockingdata)
        print('xxxxxx', clockingdataserializer.data)
        return Response(clockingdataserializer.data,status=status.HTTP_200_OK)

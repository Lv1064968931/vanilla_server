from django.contrib import admin

# Register your models here.

from . import models


admin.site.site_header = '恋语后台管理'
admin.site.site_title = '恋语'
date_hierarchy = 'pub_date'

admin.site.register(models.User)
admin.site.register(models.PhoneVerifyRecord)
admin.site.register(models.vocabulary)
admin.site.register(models.Sentence)
admin.site.register(models.Userdata)
admin.site.register(models.Strangeword)
admin.site.register(models.Clockingdata)

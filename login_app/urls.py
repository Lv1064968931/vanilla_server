
from django.conf.urls import url, include
from rest_framework import routers
from . import views

app_name = '[login1]'
router = routers.DefaultRouter()

router.register(r'User', views.UserSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

router.register(r'PhoneVerifyRecord', views.VerifySet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

router.register(r'vocabulary', views.VocabularySet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
router.register(r'Sentence', views.SentenceSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]


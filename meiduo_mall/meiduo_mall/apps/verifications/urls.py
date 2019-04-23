from django.conf.urls import url

from . import  views

urlpatterns = [
    #发送图形验证码
    url(r'^image_codes/(?P<uuid>[\w-]+)/$',views.ImageCodeView.as_view()),
    #发送短信验证吗
    url(r'^sms_codes/(?P<mobile>1[3-9]\d{9})/$', views.SMSCodeView.as_view()),

]
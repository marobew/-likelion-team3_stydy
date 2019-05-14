
from django.contrib import admin
from django.urls import path
import boram.views
import ahreum.views
import jungeun.views
import jeehyun.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', boram.views.boram, name='boram'),
    path('jeehyun/',jeehyun.views.jeehyun, name='jeehyun'),
    path('ahreum/',ahreum.views.ahreum,name='ahreum'),
    path('jungeun/', jungeun.views.jungeun, name='jungeun'),
]

from django.urls import path
from . views import *

urlpatterns = [
    path('',userRegistration,name='regist'),
    path('signin',signin_view,name='signin'),
    path('signout',signout_view,name='signout'),


]
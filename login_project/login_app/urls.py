from django.conf.urls import url,include
from django.contrib import admin
from login_app import views

app_name='login_app'
urlpatterns=[
	
	url(r'^register/$',views.register,name="register"),
	url(r'^user_login/$',views.user_login,name="user_login"),
	
]

from django.urls import path
from .import views

urlpatterns=[
    path("",views.signup_insert_page,name="insert_page"),
    path("upload/",views.signup_upload_page,name="upload_page"),
    path("login/",views.signup_login_page,name="login_page"),
]
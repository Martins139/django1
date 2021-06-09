from django.urls import path,include
from .views import signup, Login,result,homepage,success
app_name="students"

urlpatterns=[
    path('',homepage, name='home'),
    path('signup/',signup, name='signup'),
    path('login/',Login, name='login'),
    path('result/',result, name='result'),
    path('success/',success, name='success')

]
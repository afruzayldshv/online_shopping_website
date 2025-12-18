from django.urls import path
from. import views

app_name='users'

urlpatterns=[
    path('login/',views.show_login_page,name='login_page'),
    path('registration/',views.show_registration_page,name='registration_page'),
    path('logout/',views.logout_user,name='logout_page'),

]
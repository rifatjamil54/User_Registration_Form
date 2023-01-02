from django.urls import path
from . import views
urlpatterns = [
    path('singup/',views.singup_page_rendering,name='singup_url'),
    path('login/',views.login_page_rendering,name='login_url'),
    path('profile/',views.profile_page_rendering,name='profile_url'),
    path('logout/',views.logout_profile,name='logout_profile'),
    path('change_password/',views.changing_password,name='changing_password'),
    path('admin_user_profile/<int:id>',views.admin_user_profile,name='admin_user_profile'),



]
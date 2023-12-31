from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.SignUpViewClass.as_view(), name='register'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('login/',views.UserLoginViewClass.as_view(), name = 'login'),
    path('logout/',views.UserLogoutViewClass.as_view(), name = 'logout'),
    path('passwordChange/', views.ChangePassWordClass.as_view(), name='Changepaswwod'),
    path('ProfileChange/>', views.edit_profile, name='ProfileChange')

]
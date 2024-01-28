from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.SignUpViewClass.as_view(), name='register'),
     path('email_verification/<str:uidb64>/<str:token>/', views.EmailVerificationView.as_view(), name='email_verification'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('login/',views.UserLoginViewClass.as_view(), name = 'login'),
    path('logout/',views.user_logout_view, name = 'logout'),
    path('passwordChange/', views.ChangePassWordClass.as_view(), name='Changepaswwod'),
    path('ProfileChange/', views.edit_profile, name='ProfileChange'),
    path('Publishers/', views.Publishers_View.as_view(), name='Publishers'),
    path('searchPublisher/', views.Search_Publisher_Fillter, name='searchPublisher'),


]
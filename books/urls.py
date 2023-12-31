from django.urls import path,include
from . import views
urlpatterns = [
    path('Views_Details<int:id>/', views.ViewDetails,name='Views_Details'),
    path('borrow/<int:id>/<int:userid>/', views.borrow, name='buynow'),
    path('return/<int:id>/<int:userid>/<int:buyid>/', views.bookReturn, name='return'),
]
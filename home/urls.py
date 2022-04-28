from django.urls import path, include

from . import views
app_name = 'home'
urlpatterns = [

    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('home', views.home, name="home"),
    path('home/user/<int:people_id>/', views.detailUser, name='detail'),
    path('home/update/<int:people_id>/', views.updateUser, name='update'),
    path('home/tablelist', views.listUser, name='tablelist'),
    path('home/notification', views.listNotification, name='notification')
   # path('user/<int:people_id>', UpdateUser.as_view(), name='update'),
]

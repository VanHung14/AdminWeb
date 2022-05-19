from django.urls import path, include

from . import views
app_name = 'home'
urlpatterns = [
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('home', views.home, name="home"),
    path('home/user/<int:people_id>/', views.detailUser, name='detail'),
    path('home/update/<int:people_id>/', views.updateUser, name='update'),
    path('home/delete/<int:people_id>/', views.deleteUser, name='delete'),
    path('home/search/', views.searchUser, name='search'),
    path('home/tablelist', views.listUser, name='tablelist'),
<<<<<<< HEAD
=======
    path('home/notification', views.listNotification, name='notification'),
    path('home/statistical', views.statistical, name='statistical')
>>>>>>> origin/thongke
   # path('user/<int:people_id>', UpdateUser.as_view(), name='update'),
]

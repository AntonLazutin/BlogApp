from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('api/posts', views.post_list),
    path('api/users', views.user_list),
    path('logout/', views.logout_view, name="logout"),
    path('login/', views.login_view, name="login"),
    path('sign_up/', views.signup_page, name="sign_up"),
    path('posts/<int:pk>/', views.post_page, name="post"),
    path('profile/<int:pk>', views.profile_page, name="profile_page"),
    path('reaction/<int:pk>', views.reacted, name="reaction"),
]
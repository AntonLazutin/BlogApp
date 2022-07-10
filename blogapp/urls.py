from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('api/posts', views.post_list),
    path('api/users', views.user_list),
    path('logout/', views.logout_view, name="logout"),
    path('login/', views.login_view, name="login"),
    path('sign_up/', views.signup_page, name="sign_up"),
    path('{slug}/', views.post_page, name="post_page"),
    path('profile/<int:id>', views.profile_page, name="profile_page"),
]
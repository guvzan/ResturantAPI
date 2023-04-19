from django.urls import path, include

from .views import CreateUserAPIView

app_name = 'users'

userApiView = CreateUserAPIView()

urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('profile/<int:user_id>/', userApiView.show_profile, name='user_profile'),
    path('register/', userApiView.register_user, name='register'),
    path('', include('django.contrib.auth.urls')),

]
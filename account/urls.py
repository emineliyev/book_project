from django.urls import path
from account.views import login_view, user_logout, register_user, update_user


urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_user, name='register'),
    path('logout/', user_logout, name='logout'),
    path('update/', update_user, name='update')
]
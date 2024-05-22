from django.urls import path
from user.views import UserRegistrationView, UserLoginView, NotificationList, RoleList, UserList, RoleRetrieve

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/login/', UserLoginView.as_view(), name='user-login'),
    path('api/notifications/', NotificationList.as_view(), name='notification-list'),
    path('api/roles/', RoleList.as_view(), name='role-list'),
    path('api/user/<int:pk>/', UserList.as_view(), name='user-retrieve'),
    path('api/roles/<int:pk>/', RoleRetrieve.as_view(), name='role-retrieve'),
]

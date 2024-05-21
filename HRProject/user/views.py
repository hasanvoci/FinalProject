from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from user.models import User, Notification, Role
from user.serializers import UserSerializer, NotificationSerializer, RoleSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


# class UserLoginView(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         response = super(UserLoginView, self).post(request, *args, **kwargs)
#         token = Token.objects.get(key=response.data['token'])
#         user = User.objects.get(id=token.user_id)
#         serializer = UserSerializer(user)
#         return Response({
#             'token': token.key,
#             'user': serializer.data
#         })

class UserLoginView(ObtainAuthToken):
    """Custom User Login View"""

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk}, status=status.HTTP_200_OK)


class NotificationList(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [AllowAny]

class RoleList(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [AllowAny]

class RoleRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [AllowAny]

class UserList(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

from rest_framework import generics
from .models import User
from .serializers import UserSerializer


# GET all users and POST a new user
class UserListCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(is_deleted=False)


# GET one user, PUT update, PATCH partial update,
# DELETE soft delete
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(is_deleted=False)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save(update_fields=["is_deleted"])

from django.contrib.auth.models import User
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Community
from users.serializers import UserSerializer, CommunitySerializer

class UserList(generics.ListCreateAPIView):
    """
    List all users, or create a new one.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an existing user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, pk, format=None):
        user = self.get_object()
        user.communities.clear()
        user.is_active = False
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommunityList(generics.ListCreateAPIView):
    """
    List all Communities or create a new one.
    """
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

class CommunityDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an existing `Community`
    """
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

    def delete(self, request, pk, format=None, *args, **kwargs):
        community = self.get_object()
        community.users.clear()
        return self.destroy(request, *args, **kwargs)

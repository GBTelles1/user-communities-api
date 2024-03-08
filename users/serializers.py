from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Community

class UserSerializer(serializers.ModelSerializer):
    queryset = Community.objects.all()
    communities = serializers.PrimaryKeyRelatedField(many=True, queryset=queryset)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name','password', 'email', 'is_active','communities']

class CommunitySerializer(serializers.ModelSerializer):
    queryset = User.objects.all()
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=queryset)

    class Meta:
        model = Community
        fields = ['id', 'name', 'users']

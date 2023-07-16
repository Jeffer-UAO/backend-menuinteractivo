from rest_framework.serializers import ModelSerializer

from userClient.models import UserClient


class UserClientSerializer(ModelSerializer):

    class Meta:
        model = UserClient
        fields = ['id', 'title', 'password']

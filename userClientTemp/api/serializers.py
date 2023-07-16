from rest_framework.serializers import ModelSerializer

from userClientTemp.models import UserClientTemp


class UserClientTempSerializer(ModelSerializer):

    class Meta:
        model = UserClientTemp
        fields = ['id', 'title']

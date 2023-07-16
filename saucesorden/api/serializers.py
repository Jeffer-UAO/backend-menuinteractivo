from rest_framework.serializers import ModelSerializer

from saucesorden.models import Sauceorden


class SauceordenSerializer(ModelSerializer):

    class Meta:
        model = Sauceorden
        fields = ['id', 'sauces', 'order']

from rest_framework.serializers import ModelSerializer

from sauce.models import Sauce


class SauceSerializer(ModelSerializer):

    class Meta:
        model = Sauce
        fields = ['id', 'description', 'active']

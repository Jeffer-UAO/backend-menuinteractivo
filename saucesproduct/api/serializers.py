from rest_framework.serializers import ModelSerializer

from saucesproduct.models import Sauceproduct


class SauceproductSerializer(ModelSerializer):

    class Meta:
        model = Sauceproduct
        fields = ['id', 'sauces', 'product', 'description']

from rest_framework.serializers import ModelSerializer

from orders.models import Order
from products.api.serializers import ProductSerializer
from tables.api.serializers import TableSerializer
from sauce.api.serializers import SauceSerializer


class OrderSerializer(ModelSerializer):
    product_data = ProductSerializer(source='product', read_only=True)
    table_data = TableSerializer(source='table', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'status', 'table', 'table_data', 'product',
                  'product_data', 'payment', 'close', 'create_at',
                  'user', 'userTemp', 'comment', 'qty', 'tipo',  'number', 'price',
                  'discount', 'subtotal', 'salestax', 'total', 'shipto',
                  'salesman', 'prepared_at', 'delivered_at', 'sauces']

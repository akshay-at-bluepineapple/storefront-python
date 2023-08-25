from decimal import Decimal
from store.models import Product, Collection
from rest_framework import serializers

#here the api model is != data model

# class CollectionSerializer(serializers.Serializer):
#     id=serializers.IntegerField()
#     featured_product = serializers.CharField(max_length=255)
#     title =serializers.CharField(max_length=255)


# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length = 255)
#     unit_price = serializers.DecimalField(max_digits = 6,decimal_places=2)
#     price_with_tax =serializers.SerializerMethodField(method_name = 'calculate_tax')
#     # collection = serializers.PrimaryKeyRelatedField(
#     #     queryset=Collection.objects.all()
#     # )
#     # collection = serializers.StringRelatedField()
#     #collection = CollectionSerializer()

#     #can also generatrete hyperlink for the related object like collection in the above case
#     collection = serializers.HyperlinkedRelatedField(
#         queryset=Collection.objects.all(),
#         view_name='collection-details'
#     )

#     def calculate_tax(self,product:Product):
#         return product.unit_price * Decimal(0.15)


#model serializer

class CollectionSerializer(serializers.ModelSerializer):
    #products_count = serializers.IntegerField(read_only=True)
    class Meta:
        model =Collection
        fields=['id', 'title','products_count']

    products_count = serializers.IntegerField(read_only=True)



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=['id','title','description','slug','inventory','unit_price','price_with_tax','collection']

    price_with_tax =serializers.SerializerMethodField(method_name = 'calculate_tax')

    def calculate_tax(self,product:Product):
        return product.unit_price * Decimal(0.15)




from rest_framework import serializers
from .models import Users,Items,Tags

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('kai_email','kai_password')



class TagsSerializers(serializers.ModelSerializer):
    #  = serializers.RelatedField(source='Item', read_only=True)
    class Meta:
        model = Tags
        fields = ('kai_SKU','kai_tags')

class ItemsSerializers(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    class Meta:
        model = Items
        fields = ('kai_SKU','kai_Name','kai_Category','kai_instock','kai_available_stock','tags')

class TagsBulkCreateSerializer(serializers.ListSerializer):
    tag_data = TagsSerializers(many=True)
    class Meta:
        fields = ['tag_data']

    def create(self,validated_data):
        lst = []
        # for data in validated_data:
        #     lst.append(Tags(kai_SKU=data.SKU,kai_tags=data.tag))
        tags = validated_data.pop('Tags')
        SKU = validated_data.get('SKU')
        for i in range(len(tags)):
            lst.append(Tags(kai_tags=tags[i],kai_SKU=SKU))

        # product_data = [Tags(**item) for item in validated_data]  
        return Tags.objects.bulk_create(lst)
    




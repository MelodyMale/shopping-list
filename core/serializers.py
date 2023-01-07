from rest_framework import serializers
from core.models import Item


class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, max_length=100)
    checked = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.checked = validated_data.get("checked", instance.checked)
        instance.save()
        return instance

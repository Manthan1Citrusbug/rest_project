from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)


    def create(self, validated_data):
        return Student.objects.create(**validated_data)


    def update(self, instance, validated_data):
        # instance is old data stored in database
        # validated data is new data you want to store in database
        instance.name = validated_data.get('name', instance.name)
        print("OLD -- ",instance.roll)
        instance.roll = validated_data.get('roll', instance.roll)
        print("UPDATED -- ",instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
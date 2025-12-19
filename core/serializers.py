from rest_framework import serializers

class CourseSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    duration = serializers.CharField()

class StudentSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    course = serializers.CharField()  

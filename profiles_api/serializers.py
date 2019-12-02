from rest_framework import serializers


class ProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    last_login = serializers.DateTimeField()
    login_count = serializers.IntegerField()
    project_count = serializers.IntegerField()

from rest_framework import serializers

from .models import Task, AppUser

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    assigned_to_user = AppUserSerializer(source='assigned_to', read_only=True)
    class Meta:
        model = Task
        fields = [
            'id',
            'name',
            'description',
            'status',
            'assigned_to',
            'assigned_to_user'
        ]

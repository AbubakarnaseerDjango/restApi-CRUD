from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .  models import Task


class TaskSerializers(serializers.ModelSerializer):
     class Meta:
        model = Task
        fields = '__all__'
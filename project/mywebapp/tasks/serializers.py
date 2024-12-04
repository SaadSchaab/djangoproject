from tasks.models import PlannedTask

from rest_framework import serializers


class PlannedTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlannedTask
        fields = '__all__'
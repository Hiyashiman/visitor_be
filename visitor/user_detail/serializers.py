from rest_framework import serializers
from .models import UserDetail
class RapperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserDetail
        fields = ('__all__')
import logging
from rest_framework import serializers
from .models import EnergyPrice


class EnergyLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = EnergyPrice
        fields = '__all__'

    def get_field_names(self, declared_fields, info):
        request = self.context.get('request')
        region = request.parser_context.get('kwargs').get('region')

        return ('date', region,)

from rest_framework import fields, serializers
from beer.models import BeerModel, WhiskeyModel


class BeerModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = BeerModel

        fields = (
            'name',
            'beer_type',
            'description',
        )


class WhiskeyModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = WhiskeyModel
        fields = "__all__"

from rest_framework import serializers
from .models import Option, OptionPair


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'prompt', 'votes_total', 'other')


class OptionPairSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionPair
        fields = ('id', 'desc', 'prompt_a', 'prompt_b', 'votes_a', 'votes_b')
        depth = 1
from rest_framework import serializers
from .models import Option, OptionPair


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'prompt')


class OptionPairSerializer(serializers.ModelSerializer):
    prompt_a = OptionSerializer()
    prompt_b = OptionSerializer()

    class Meta:
        model = OptionPair
        fields = ('id', 'desc', 'prompt_a', 'prompt_b', 'votes_a', 'votes_b')

    def create(self, validated_data):
        prompt_a_data = validated_data.pop('prompt_a')
        prompt_b_data = validated_data.pop('prompt_b')
        prompt_a = Option.objects.create(**prompt_a_data)
        prompt_b = Option.objects.create(**prompt_b_data)
        op = OptionPair.objects.create(prompt_a=prompt_a, prompt_b=prompt_b, **validated_data)
        return op
        
class VoteSerializer(serializers.Serializer):
    op_id = serializers.IntegerField(read_only=True)
    new_votes_a = serializers.IntegerField(max_value=1, min_value=0)
    new_votes_b = serializers.IntegerField(max_value=1, min_value=0)
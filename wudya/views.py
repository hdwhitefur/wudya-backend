from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import OptionSerializer, OptionPairSerializer, VoteSerializer
from .models import Option, OptionPair
import random

class OptionView(viewsets.ModelViewSet):
    serializer_class = OptionSerializer
    queryset = Option.objects.all()

class OptionPairView(viewsets.ModelViewSet):
    serializer_class = OptionPairSerializer
    queryset = OptionPair.objects.all()

    @action(detail=False)
    def get_random(self, request):
        serializer = self.get_serializer(random.choice(OptionPair.objects.all()))
        return Response(serializer.data)

class VoteView(viewsets.ViewSet):
    serializer_class = VoteSerializer

    def update(self, request, pk=None):
        op = get_object_or_404(OptionPair, pk=pk)
        op.votes_a = op.votes_a + int(request.data['new_votes_a'])
        op.votes_b = op.votes_b + int(request.data['new_votes_b'])
        op.save()
        return Response()

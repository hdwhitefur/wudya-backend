from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OptionSerializer, OptionPairSerializer, VoteSerializer
from .models import Option, OptionPair

class OptionView(viewsets.ModelViewSet):
    serializer_class = OptionSerializer
    queryset = Option.objects.all()

class OptionPairView(viewsets.ModelViewSet):
    serializer_class = OptionPairSerializer
    queryset = OptionPair.objects.all()

class VoteView(APIView):
    def put(self, request):
        print(request)
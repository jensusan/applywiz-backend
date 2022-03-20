from django.shortcuts import render, redirect
from .models import Talent, Survey
from rest_framework import generics, permissions
from .serializers import TalentSerializer, SurveySerializer


class TalentList(generics.ListCreateAPIView):
    queryset = Talent.objects.all()
    serializer_class = TalentSerializer


class TalentDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Talent.objects.all()
    serializer_class = TalentSerializer


class SurveyList(generics.ListCreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    # permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     return self.request.user.survey.all()

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class SurveyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

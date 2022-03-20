from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('talent/', views.TalentList.as_view(), name='talent_list'),
    path('talent/<int:pk>', views.TalentDetail.as_view(), name='talent_details'),
    
    path('survey/', views.SurveyList.as_view(), name='survey_list'),
    path('survey/', views.SurveyDetail.as_view(), name='survey_details'),


    

  
]


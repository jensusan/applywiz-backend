from rest_framework import serializers
from .models import Talent, Survey
from rest_framework.fields import ReadOnlyField

class TalentSerializer(serializers.HyperlinkedModelSerializer):
    survey = serializers.HyperlinkedRelatedField(view_name='survey_details',
    many=True,
    read_only=True)

    class Meta:
       model = Talent
       fields=('id', 'first_name', 'last_name', 'phone_number', 'email', 'zip_code', 'website', 'survey')


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    talent = serializers.HyperlinkedRelatedField(view_name='talent_details',
    many=True,
    read_only=True)
    
    class Meta:
        model = Survey
        fields = ('id', 'role', 'education', 'certification',
        'role_important',
        'location', 'start_date', 'role_level', 'role_time', 'company_size', 'sponsorship', 'languages', 'specific_industry', 'veteran', 'disability', 'expected_salary', 'talent')

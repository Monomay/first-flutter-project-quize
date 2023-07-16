from rest_framework import serializers
from .models import Exam


class ExamSerializer(serializers.ModelSerializer):
       question = serializers.CharField(max_length=100)
       answer = serializers.CharField(max_length=100)
       class Meta:
        model = Exam
        fields = ('__all__')
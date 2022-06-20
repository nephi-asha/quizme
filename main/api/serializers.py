from main.models import Question
from rest_framework import serializers, viewsets


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['question', 'choice1', 'choice2',
                  'choice3', 'choice4', 'answer', 'domain']

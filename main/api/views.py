from .serializers import QuestionSerializer
from main.models import Question
from rest_framework import viewsets, permissions

OTHERS = 'OTHERS'
MATH = 'MATHEMATICS'
ENG = 'ENGLISH STUDIES'
GEO = 'GOEGRAPHY'
CHEM = 'CHEMISTRY'
PHY = 'PHYSICS'
HISTORY = 'HISTORY'
COMP = 'COMPUTER STUDIES'
CRS = 'CHRISTIAN RELIGIOUS STUDIES'
FMATH = 'FURTHER MATHEMATICS'
ECON = 'ECONOMICS'
BIO = 'BIOLOGY'
CIVIC = 'CIVIC EDUCATION'
NONE = 'NONE'


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class OthersViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(domain=OTHERS)
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class MathematicsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(domain=MATH)
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class EnglishViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(domain=ENG)
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class GeographyViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(domain=GEO)
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChemistryViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(domain=CHEM)
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class PhysicsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(domain=PHY)
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(domain=HISTORY)
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class ComputerViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(domain=COMP)
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class CRSViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(domain=CRS)
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class Further_MathViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(domain=FMATH)
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class EconomicsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(domain=ECON)
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class BiologyViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(domain=BIO)
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class CivicViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(domain=CIVIC)
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class NoneViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(domain=NONE)
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

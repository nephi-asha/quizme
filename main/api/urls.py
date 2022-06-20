from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet, basename='questions')
router.register(r'others', views.OthersViewSet, basename='others')
router.register(r'mathematics',
                views.MathematicsViewSet, basename='mathematics')
router.register(r'english', views.EnglishViewSet, basename='english')
router.register(r'geography',
                views.GeographyViewSet, basename='geography')
router.register(r'biology', views.BiologyViewSet, basename='biology')
router.register(r'chemistry',
                views.ChemistryViewSet, basename='chemistry')
router.register(r'physics', views.PhysicsViewSet, basename='physics')
router.register(r'history', views.HistoryViewSet, basename='history')
router.register(r'computer',
                views.ComputerViewSet, basename='computer')
router.register(r'crs', views.CRSViewSet, basename='crs')
router.register(r'further_math', views.Further_MathViewSet,
                basename='further_math')
router.register(r'economics',
                views.Further_MathViewSet, basename='economics')
router.register(r'civic', views.CivicViewSet, basename='civic')
router.register(r'none', views.NoneViewSet, basename='none')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls

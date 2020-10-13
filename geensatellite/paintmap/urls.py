from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import *

#Initialization of router
router = DefaultRouter()
router.register(r'api/associations', SocAssociationsViewSet, basename='paintmap')
router.register(r'api/farm', FarFarmsViewSet, basename='paintmap')
router.register(r'api/technical-assistants', SocTechnicalAssistantsViewSet, basename='paintmap')
router.register(r'api/technical-assistant/(?P<association>.+)/get', GetTechnicalAssistantsViewSet, basename='paintmap')
router.register(r'api/plots/(?P<farm>.+)/get', FarPlotsViewSet, basename='paintmap')
router.register(r'api/production-event/(?P<technical>.+)/get', GetProductionEventsViewSet, basename='paintmap')
router.register(r'api/production-events/(?P<technical>.+)/(?P<plot>.+)/get', FarProductionEventsViewSet, basename='paintmap')
router.register(r'api/block-form/(?P<form>.+)/get', FrmBlocksFormsViewSet, basename='paintmap')
""" router.register(r'api/question/(?P<block>.+)/(?P<type>.+)/get', FrmQuestionViewSet, basename='paintmap') """
router.register(r'api/question/(?P<form>.+)/(?P<type>.+)/get', FrmQuestionTestViewSet, basename='paintmap')
router.register(r'api/question-date/(?P<question>.+)/(?P<event>.+)/get', FarResponsesDateViewSet, basename='paintmap')
router.register(r'api/question-numeric/(?P<question>.+)/(?P<event>.+)/get', FarResponsesNumericViewSet, basename='paintmap')
#router.register(r'api/dataframe', TimeSeriesViewSet, basename='paintmap')
urlpatterns = [
    path('', include(router.urls))
]
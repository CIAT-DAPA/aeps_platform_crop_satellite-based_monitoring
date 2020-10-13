from django.shortcuts import render
from rest_framework import viewsets, mixins
from django.http import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_pandas import PandasSimpleView, PandasViewSet
from rest_framework.response import Response
from django.http import JsonResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic.base import TemplateView
#from rest_framework.views import APIView


#Local package function
from paintmap.scripts import gee_satellite_data
from paintmap.scripts import gee_plots
from paintmap.scripts import gee_functions

#Local apps
from .models import *
from .serializers import *

class SocAssociationsViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    """ViewSet for Associations"""
    serializer_class = SocAssociationsSerializer
    queryset = SocAssociations.objects.all()

class FarFarmsViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    """ViewSet for Associations"""
    serializer_class = FarFarmSerializer
    queryset = FarFarms.objects.all()
       
class GetTechnicalAssistantsViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    """ViewSet for Technical Assistants"""
    queryset = SocTechnicalAssistants.objects.all()
    serializer_class = SocTechnicalAssistantsSerializer

    def list(self, request, *args, **kwargs):
        association = self.kwargs['association']
        technicalAssistant = SocTechnicalAssistants.objects.filter(association=association)
        serialier = GetTechnicalAssistantsSerializer(technicalAssistant, many=True)
        return Response(serialier.data)

class GetProductionEventsViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    """ViewSet for Technical Assistants"""
    queryset = FarProductionEvents.objects.all()
    serializer_class = FarProductionEventsSerializer

    def list(self, request, *args, **kwargs):
        technical = self.kwargs['technical']
        productionEvents = FarProductionEvents.objects.filter(technical=technical)
        serialier = GetProductionEventsSerializer(productionEvents, many=True)
        return Response(serialier.data)

class SocTechnicalAssistantsViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    """ViewSet for Technical Assistants"""
    queryset = SocTechnicalAssistants.objects.all()
    serializer_class = SocTechnicalAssistantsSerializer

class FarPlotsViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    """ViewSet for Plots"""
    queryset = FarPlots.objects.all()
    serializer_class = FarPlotsSerializer
    def list(self, request, *args, **kwargs):
        farm = self.kwargs['farm']
        plots = FarPlots.objects.filter(farm=farm)
        serialier = FarPlotsSerializer(plots, many=True)
        return Response(serialier.data)

class FarProductionEventsViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    """ViewSet for Production Events"""
    queryset = FarProductionEvents.objects.all()
    serializer_class = FarProductionEventsSerializer
    def list(self, request, *args, **kwargs):
        technical = self.kwargs['technical']
        plot = self.kwargs['plot']
        productionEvents = FarProductionEvents.objects.filter(technical=technical, plot=plot)
        serialier = FarProductionEventsSerializer(productionEvents, many=True)
        return Response(serialier.data)

class FrmBlocksFormsViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    """ViewSet for Production Events"""
    queryset = FrmBlocksForms.objects.all()
    serializer_class = FrmBlocksFormSerializer
    def list(self, request, *args, **kwargs):
        form = self.kwargs['form']
        blockForm = FrmBlocksForms.objects.filter(form=form)
        serialier = FrmBlocksFormSerializer(blockForm, many=True)
        return Response(serialier.data)

class FrmQuestionViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    """ViewSet for Questions"""
    queryset = FrmQuestions.objects.all()
    serializer_class = FrmQuestionsSerializer
    def list(self, request, *args, **kwargs):
        block = self.kwargs['block']
        typeQuestion = self.kwargs['type']
        question = FrmQuestions.objects.filter(block=block, type=typeQuestion)
        serialier = FrmQuestionsSerializer(question, many=True)
        return Response(serialier.data)

class FrmQuestionTestViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
   """ViewSet for Production Events"""
   queryset = FrmBlocksForms.objects.all()
   serializer_class = FrmBlocksFormSerializer
   def list(self, request, *args, **kwargs):
        form = self.kwargs['form']
        typed = self.kwargs['type']
        blockForm = FrmBlocksForms.objects.filter(form=form).values_list('block_id', flat=True)
        question = FrmQuestions.objects.filter(block__in=blockForm, type=typed)
        serialier = FrmQuestionsSerializer(question, many=True)
        return Response(serialier.data)

class FarResponsesDateViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    """ViewSet for Production Events"""
    queryset = FarResponsesDate.objects.all()
    serializer_class = FarResponsesDateSerializer
    def list(self, request, *args, **kwargs):
        question = self.kwargs['question']
        event = self.kwargs['event']
        responsesDate = FarResponsesDate.objects.filter(question=question, event=event)
        serialier = FarResponsesDateSerializer(responsesDate, many=True)
        return Response(serialier.data)

class FarResponsesNumericViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    """ViewSet for Production Events"""
    queryset = FarResponsesNumeric.objects.all()
    serializer_class = FarResponsesNumericSerializer
    def list(self, request, *args, **kwargs):
        question = self.kwargs['question']
        event = self.kwargs['event']
        responsesNumeric = FarResponsesNumeric.objects.filter(question=question, event=event)
        serialier = FarResponsesNumericSerializer(responsesNumeric, many=True)
        return Response(serialier.data)
    

## region of interest
longitude = -79.84521567821503
latitude = -6.723309128386431
areaofinfluence = 20 ## this value is the circle radius, that will wrap the area of interest, in meters'

def getSentinel(startDate, endDate, area, lon, lat):
    """Instance a sentinel class"""
    sentinel3 = gee_satellite_data.get_gee_data(startDate,  ## start date
                                            endDate, ## end query date
                                            point_coordinates= [float(lon),float(lat)], ## region of interest
                                            mission= "sentinel2_sr", ## mission
                                            cloud_percentage= 80, ## clouds percentage allowed per image 
                                            buffer= float(area)                                           
                                           )
    return sentinel3                                           


def list_map(request, startDate, endDate, area, lon, lat):
    """List images available"""
    sentinel3 = getSentinel(startDate, endDate, area, lon, lat)
    #map = [1, 2, 4]
    area_dict = sentinel3.summary.to_dict('records')
    app_json = json.dumps(area_dict,sort_keys=True,indent=4,cls=DjangoJSONEncoder)

    return HttpResponse(app_json)

###


def viewMap(request, index, startDate, endDate, area, lon, lat):
    sentinel2 = getSentinel(startDate, endDate, area, lon, lat)
    sentinel2.add_vi_layer("ndvi")
    ### True-color image visualization
    ## defining visualization parameters
    truecolorParams = {'gamma': 1.3, 
                   'min': 57,
                   'max': 2000,
                   'bands': ['B4','B3','B2']
                   }

    ndviParams = {     'min': 0,
                   'max': 1,
                   'palette': ['#FF0000', '#00FF00'],
                   'bands': ['ndvi']
                   }
    ## image selection
    image_index = index
    truecolorimage = sentinel2.image_collection.toList(sentinel2.image_collection.size()).get(image_index)
    ndviimage = sentinel2.image_collection.toList(sentinel2.image_collection.size()).get(image_index)
    ## Visualization
    ### both images visualization
    map = gee_plots.plot_multiple_eeimage([truecolorimage, ndviimage], 
                                [truecolorParams, ndviParams], 
                                sentinel2.geometry, 
                                ['true color', 'ndvi'],zoom = 14)
    mapHtml = map._repr_html_()
    #context = {'map': mapHtml}
    #return render(request, 'filter.html', context)
    return HttpResponse(mapHtml)

def bands_table(request, startDate, endDate, area, lon, lat):
    sentinel2 = getSentinel(startDate, endDate, area, lon, lat)
    sentinel2.add_vi_layer("ndvi")
    band_table = gee_functions.get_band_timeseries_summary(sentinel2, 'ndvi')
    print(band_table)
    area_dict = band_table.to_dict('records')
    app_json = json.dumps(area_dict,sort_keys=True,indent=4,cls=DjangoJSONEncoder)
    return HttpResponse(app_json)                                               


def viewChart(request, startDate, endDate, area, lon, lat):
    sentinel2 = getSentinel(startDate, endDate, area, lon, lat)
    ### adding the ndvi layer
    sentinel2.add_vi_layer("ndvi")
    context = {}
    div = gee_plots.plot_vi_time_series(sentinel2, 'ndvi')

    context['graph'] = div
    return HttpResponse(div)
    ##return render(request, 'filter.html', context)


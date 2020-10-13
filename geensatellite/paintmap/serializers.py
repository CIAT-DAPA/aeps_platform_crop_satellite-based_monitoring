from rest_framework import serializers

#Local models
from .scripts.gee_satellite_data import *
from .models import *

class SocAssociationsSerializer(serializers.ModelSerializer):
    """Serializers for Associations"""
    class Meta:
        model = SocAssociations
        fields = '__all__'

class SoPeopleSerializer(serializers.ModelSerializer):
    """Serializers for Associations"""
    class Meta:
        model = SocPeople
        fields = '__all__'


class SocTechnicalAssistantsSerializer(serializers.ModelSerializer):
    """Serializer for Technical Assistants"""
    class Meta:
        model = SocTechnicalAssistants
        fields = '__all__'


class FarFarmSerializer(serializers.ModelSerializer):
    """Serializer for Farm"""
    class Meta:
        model = FarFarms
        fields = '__all__'

class FarPlotsSerializer(serializers.ModelSerializer):
    """Serializer for Plots"""
    class Meta:
        model = FarPlots
        fields = '__all__'

class GetFarPlotsSerializer(serializers.ModelSerializer):
    """Serializer for Plots"""
    farm = FarFarmSerializer(read_only=True)
    class Meta:
        model = FarPlots
        fields = '__all__'
    
class FarProductionEventsSerializer(serializers.ModelSerializer):
    """Serializer for Proudction Events"""
    class Meta:
        model = FarProductionEvents
        fields = '__all__'

class GetProductionEventsSerializer(serializers.ModelSerializer):
    """Serializer for Proudction Events"""
    plot = GetFarPlotsSerializer(read_only=True)
    class Meta:
        model = FarProductionEvents
        fields = '__all__'

class GetTechnicalAssistantsSerializer(serializers.ModelSerializer):
    """Serializer for Technical Assistants"""
    person = SoPeopleSerializer(read_only=True)
    class Meta:
        model = SocTechnicalAssistants
        fields = '__all__'


class FrmFormSerializer(serializers.ModelSerializer):
    """Serializer for Proudction Events"""
    class Meta:
        model = FrmForms
        fields = '__all__'

class FrmQuestionsSerializer(serializers.ModelSerializer):
    """Serializer for Proudction Events"""
    class Meta:
        model = FrmQuestions
        fields = '__all__'


class FrmBlocksSerializer(serializers.ModelSerializer):
    """Serializer for Proudction Events"""
    class Meta:
        model = FrmBlocks
        fields = '__all__'

class FrmBlocksFormSerializer(serializers.ModelSerializer):
    """Serializer for Proudction Events"""
    form = FrmFormSerializer(read_only=True)
    block = FrmBlocksSerializer(read_only=True)
    class Meta:
        model = FrmBlocksForms
        fields = '__all__'

class FarResponsesDateSerializer(serializers.ModelSerializer):
    """Serializer for Proudction Events"""
    class Meta:
        model = FarResponsesDate
        fields = '__all__'

class FarResponsesNumericSerializer(serializers.ModelSerializer):
    """Serializer for Proudction Events"""
    class Meta:
        model = FarResponsesNumeric
        fields = '__all__'
   
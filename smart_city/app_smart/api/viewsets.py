
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from app_smart.api import serializer
from . .models import ContadorData, LuminosidadeData, Sensor, TemperaturaData, UmidadeData
from rest_framework import viewsets
from app_smart.api.filters import SensorFilter, TemperaturaDataFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response

class CreateUserAPIViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer
    # permission_classes = [permissions.IsAdminUser]
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = serializer.SensorSerializer
    permission_class = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SensorFilter
    
class SensorFilterView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        tipo = request.data.get('tipo', None)
        localizacao = request.data.get('localizacao', None)
        responsavel = request.data.get('responsavel', None)
        status_operacional = request.data.get('status_operacional', None)
        
        filters = Q() #inicializa um filtro vazio
        if tipo:
            filters &= Q(tipo__icontains=tipo)
        if localizacao:
            filters &= Q(localizacao__icontains=localizacao)
        if responsavel:
            filters &= Q(responsavel__icontains=responsavel)
        if status_operacional is not None:
            filters &= Q(status_operacional=status_operacional)
            
        queryset = Sensor.objects.filter(filters)
        serializers = serializer.SensorSerializer(queryset, many=True)
        return Response(serializers.data)
    
class TemperaturaDataViewSet(viewsets.ModelViewSet):
    queryset = TemperaturaData.objects.all()
    serializer_class = serializer.TemperaturaDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TemperaturaDataFilter
    
class ContadorDataViewSet(viewsets.ModelViewSet):
    queryset = ContadorData.objects.all()
    serializer_class = serializer.ContadorDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class UmidadeDataViewSet(viewsets.ModelViewSet):
    queryset = UmidadeData.objects.all()
    serializer_class = serializer.ContadorDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class LuminosidadeDataViewSet(viewsets.ModelViewSet):
    queryset = LuminosidadeData.objects.all()
    serializer_class = serializer.ContadorDataSerializer
    permission_classes = [permissions.IsAuthenticated]
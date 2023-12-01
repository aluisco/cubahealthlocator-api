from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from core.models import Provincia, Municipio, Institucion, Tipo
from api.serializers import ProvinciaSerializers, MunicipioSerializers, InstitucionSerializers, TipoSerializers


class ProvinciaList(APIView):
    def get(self, request):
        provincias = Provincia.objects.all()
        data = ProvinciaSerializers(provincias, many=True).data
        return Response(data)


class ProvinciaDetail(APIView):
    def get(self, request, pk):
        provincia = get_object_or_404(Provincia, pk=pk)
        data = ProvinciaSerializers(provincia).data
        return Response(data)


class MunicipioList(APIView):
    def get(self, request):
        municipios = Municipio.objects.all()
        data = MunicipioSerializers(municipios, many=True).data
        return Response(data)


class MunicipioDetail(APIView):
    def get(self, request, pk):
        municipio = get_object_or_404(Municipio, pk=pk)
        data = MunicipioSerializers(municipio).data
        return Response(data)


class TipoList(APIView):
    def get(self, request):
        tipo = Tipo.objects.all()
        data = TipoSerializers(tipo, many=True).data
        return Response(data)


class TipoDetail(APIView):
    def get(self, request, pk):
        tipo = get_object_or_404(Tipo, pk=pk)
        data = TipoSerializers(tipo).data
        return Response(data)


class InstitucionList(APIView):
    def get(self, request):
        instituciones = Institucion.objects.filter(disponible=True)
        data = InstitucionSerializers(instituciones, many=True).data
        return Response(data)


class InstitucionDetail(APIView):
    def get(self, request, pk):
        institucion = get_object_or_404(Institucion, pk=pk)
        data = InstitucionSerializers(institucion).data
        return Response(data)

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from core.models import Provincia, Municipio, Institucion, InstImagenes
from api.serializers import ProvinciaSerializers, MunicipioSerializers, InstitucionSerializers, InstImagenesSerializers


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


class ImagenesList(APIView):
    def get(self, request):
        imagenes = InstImagenes.objects.filter(disponible=True)
        data = InstImagenesSerializers(imagenes, many=True).data
        return Response(data)


class ImagenesDetail(APIView):
    def get(self, request, pk):
        imagen = get_object_or_404(InstImagenes, pk=pk)
        data = InstImagenesSerializers(imagen).data
        return Response(data)

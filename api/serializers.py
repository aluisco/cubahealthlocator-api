from rest_framework.serializers import ModelSerializer

from core.models import Provincia, Municipio, Institucion


class ProvinciaSerializers(ModelSerializer):
    class Meta:
        model = Provincia
        fields = '__all__'


class MunicipioSerializers(ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'


class InstitucionSerializers(ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'


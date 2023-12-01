from django.forms import ModelForm
from core.models import Provincia, Municipio, Institucion


class ProvinciaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Provincia
        fields = ('nombre', 'descripcion_es', 'descripcion_en', 'imagen')
        exclude = ('total_mun', 'total_int')


class MunicipioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Municipio
        fields = ('provincia', 'nombre', 'descripcion_es', 'descripcion_en', 'imagen')
        exclude = ('total_int',)


class InstitucionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Institucion
        fields = '__all__'

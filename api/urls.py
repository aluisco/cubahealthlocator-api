from django.urls import path

from api.views import ProvinciaList, ProvinciaDetail, MunicipioList, MunicipioDetail, InstitucionList, InstitucionDetail, ImagenesList, ImagenesDetail

urlpatterns = [
    path("provincia/", ProvinciaList.as_view(), name="api_province_list"),
    path("provincia/<int:pk>/", ProvinciaDetail.as_view(), name="api_province_detail"),
    path("municipio/", MunicipioList.as_view(), name="api_municipio_list"),
    path("municipio/<int:pk>/", MunicipioDetail.as_view(), name="api_municipio_detail"),
    path("institucion/", InstitucionList.as_view(), name="api_institucion_list"),
    path("institucion/<int:pk>/", InstitucionDetail.as_view(), name="api_institucion_detail"),
    path("imagenes/", ImagenesList.as_view(), name="api_instimagenes_list"),
    path("imagenes/<int:pk>/", ImagenesDetail.as_view(), name="api_instimagenes_detail"),
]



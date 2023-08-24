from django.urls import path

from api.views import ProvinciaList, ProvinciaDetail, MunicipioList, MunicipioDetail, InstitucionList, InstitucionDetail, ImagenesList, ImagenesDetail

urlpatterns = [
    path("provincia/", ProvinciaList.as_view(), name="province_list"),
    path("provincia/<int:pk>/", ProvinciaDetail.as_view(), name="province_detail"),
    path("municipio/", MunicipioList.as_view(), name="municipio_list"),
    path("municipio/<int:pk>/", MunicipioDetail.as_view(), name="municipio_detail"),
    path("institucion/", InstitucionList.as_view(), name="institucion_list"),
    path("institucion/<int:pk>/", InstitucionDetail.as_view(), name="institucion_detail"),
    path("imagenes/", ImagenesList.as_view(), name="instimagenes_list"),
    path("imagenes/<int:pk>/", ImagenesDetail.as_view(), name="instimagenes_detail"),
]

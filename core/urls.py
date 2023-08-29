from django.urls import path
from core.views import dashboard, ProvinciaListView, ProvinciaDeleteView, ProvinciaUpdate, MunicipioListView, \
    MunicipioDeleteView, MunicipioUpdate, InstitucionListView, InstitucionDeleteView, InstitucionUpdate, MunicipioAdd, \
    ProvinciaAdd, estadisticas

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('estadisticas/', estadisticas, name='estadisticas'),
    path('provincias/', ProvinciaListView.as_view(), name='provincia_list'),
    path('provincias/add/', ProvinciaAdd, name='provincia_add'),
    path('provincias/<int:pk>/remove/', ProvinciaDeleteView.as_view(), name='provincia_delete'),
    path('provincias/<int:pk>/edit/', ProvinciaUpdate, name='provincia_edit'),
    path('municipios/', MunicipioListView.as_view(), name='municipios_list'),
    path('municipios/add/', MunicipioAdd, name='municipios_add'),
    path('municipios/<int:pk>/remove/', MunicipioDeleteView.as_view(), name='municipios_delete'),
    path('municipios/<int:pk>/edit/', MunicipioUpdate, name='municipios_edit'),
    path('instituciones/', InstitucionListView.as_view(), name='instituciones_list'),
    path('instituciones/<int:pk>/remove/', InstitucionDeleteView.as_view(), name='instituciones_delete'),
    path('instituciones/<int:pk>/edit/', InstitucionUpdate, name='instituciones_edit'),
]

handler404 = 'core.views.error_404_view'
handler500 = 'core.views.error_500_view'

from django.urls import path
from core.views import dashboard, ProvinciaListView, ProvinciaDeleteView, ProvinciaUpdate

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('provincias/', ProvinciaListView.as_view(), name='provincia_list'),
    path('provincias/<int:pk>/remove/', ProvinciaDeleteView.as_view(), name='provincia_delete'),
    path('provincias/<int:pk>/edit/', ProvinciaUpdate, name='provincia_edit'),
]

handler404 = 'core.views.error_404_view'
handler500 = 'core.views.error_500_view'

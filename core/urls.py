from django.urls import path

from core.views import ProvinciaList, ProvinciaDetail

urlpatterns = [
    path("provincia/", ProvinciaList.as_view(), name="province_list"),
    path("provincia/<int:pk>/", ProvinciaDetail.as_view(), name="province_detail")
]

from django.urls import path
from core.views import dashboard

urlpatterns = [
    path('', dashboard, name='dashboard')
]

handler404 = 'core.views.error_404_view'

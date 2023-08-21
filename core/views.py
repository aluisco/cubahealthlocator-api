from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from core.models import Provincia
from core.serializers import ProvinciaSerializers


class ProvinciaList(APIView):
    def get(self, request):
        polls = Provincia.objects.all()[:20]
        data = ProvinciaSerializers(polls, many=True).data
        return Response(data)


class ProvinciaDetail(APIView):
    def get(self, request, pk):
        poll = get_object_or_404(Provincia, pk=pk)
        data = ProvinciaSerializers(poll).data
        return Response(data)


def Index(request):
    return redirect(reverse_lazy('admin:index'))

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from core.forms import ProvinciaForm, MunicipioForm, InstitucionForm
from core.models import Provincia, Municipio, Institucion


@login_required
def dashboard(request):
    context = {
        'municipio': Municipio.objects.count(),
        'provincia': Provincia.objects.count(),
        'instituciones': Institucion.objects.count(),
        'urgencia': Institucion.objects.filter(urgencia=True).count(),
    }
    return render(template_name='dashboard/dashboard.html', request=request, context=context)


@login_required
def estadisticas(request):
    return render(template_name='estadisticas/estadisticas.html', request=request)


def error_404_view(request, exception=None):
    return render(request, '404.html')


def error_500_view(request, exception=None):
    return render(request, '500.html')


class ProvinciaListView(LoginRequiredMixin, ListView):
    model = Provincia
    template_name = "provincia/provincia.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProvinciaDeleteView(LoginRequiredMixin, DeleteView):
    model = Provincia

    @method_decorator(csrf_exempt, xframe_options_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(xframe_options_exempt)
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self, **kwargs):
        return reverse_lazy('provincia_list')

    def delete(self, request, *args, **kwargs):
        pid = self.kwargs['id']
        province = Provincia.objects.filter(id=pid)
        province.delete()
        return reverse_lazy('provincia_list')


class ProvinciaAddView(LoginRequiredMixin, CreateView):
    template_name = 'provincia/provincia_add.html'
    form_class = ProvinciaForm
    success_url = reverse_lazy('provincia_list')

    def get_context_data(self, **kwargs):
        context = super(ProvinciaAddView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return super(ProvinciaAddView, self).form_valid(form)


class ProvinciaEditView(LoginRequiredMixin, UpdateView):
    template_name = 'provincia/provincia_edit.html'
    model = Provincia
    form_class = ProvinciaForm
    success_url = reverse_lazy('provincia_list')


class MunicipioListView(LoginRequiredMixin, ListView):
    model = Municipio
    template_name = "municipio/municipio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MunicipioDeleteView(LoginRequiredMixin, DeleteView):
    model = Municipio

    @method_decorator(csrf_exempt, xframe_options_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(xframe_options_exempt)
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self, **kwargs):
        return reverse_lazy('municipio_list')

    def delete(self, request, *args, **kwargs):
        pid = self.kwargs['id']
        municipio = Municipio.objects.filter(id=pid)
        municipio.delete()
        return HttpResponse('')


class MunicipioAddView(LoginRequiredMixin, CreateView):
    template_name = 'municipio/municipio_add.html'
    form_class = MunicipioForm
    success_url = reverse_lazy('municipios_list')

    def get_context_data(self, **kwargs):
        context = super(MunicipioAddView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return super(MunicipioAddView, self).form_valid(form)


class MunicipioEditView(LoginRequiredMixin, UpdateView):
    template_name = 'municipio/municipio_edit.html'
    model = Municipio
    form_class = MunicipioForm
    success_url = reverse_lazy('municipios_list')


class InstitucionListView(LoginRequiredMixin, ListView):
    model = Institucion
    template_name = "institucion/institucion.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class InstitucionDeleteView(LoginRequiredMixin, DeleteView):
    model = Institucion

    @method_decorator(csrf_exempt, xframe_options_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(xframe_options_exempt)
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self, **kwargs):
        return reverse_lazy('instituciones_list')

    def delete(self, request, *args, **kwargs):
        pid = self.kwargs['id']
        institucion = Institucion.objects.filter(id=pid)
        institucion.delete()
        return reverse_lazy('instituciones_list')


class InstitucionAddView(LoginRequiredMixin, CreateView):
    template_name = 'institucion/institucion_add.html'
    form_class = InstitucionForm
    success_url = reverse_lazy('instituciones_list')

    def get_context_data(self, **kwargs):
        context = super(InstitucionAddView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return super(InstitucionAddView, self).form_valid(form)


class InstitucionEditView(LoginRequiredMixin, UpdateView):
    template_name = 'institucion/institucion_edit.html'
    model = Institucion
    form_class = InstitucionForm
    success_url = reverse_lazy('instituciones_list')



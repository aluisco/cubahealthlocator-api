from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DeleteView
from core.models import Provincia, Municipio, Institucion, InstImagenes


@login_required
def dashboard(request):
    context = {
        'municipio': Municipio.objects.count(),
        'provincia': Provincia.objects.count(),
        'instituciones': Institucion.objects.count(),
    }
    return render(template_name='dashboard/dashboard.html', request=request, context=context)


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
        return HttpResponse('')


@login_required
@csrf_exempt
def ProvinciaUpdate(request, pk):
    if request.method == 'POST':
        provincia = Provincia.objects.get(pk=pk)
        nombre = request.POST['nombre']
        provincia.nombre = nombre
        provincia.save()
        return HttpResponse('')
    else:
        return redirect(reverse_lazy('provincia_list'))


@login_required
@csrf_exempt
def ProvinciaAdd(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        nuevo = Provincia(nombre=nombre)
        nuevo.save()
        return HttpResponse('')
    else:
        return redirect(reverse_lazy('provincia_list'))


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


@login_required
@csrf_exempt
def MunicipioUpdate(request, pk):
    if request.method == 'POST':
        municipio = Municipio.objects.get(pk=pk)
        nombre = request.POST['nombre']
        municipio.nombre = nombre
        municipio.save()
        return HttpResponse('')
    else:
        return redirect(reverse_lazy('municipio_list'))


@login_required
@csrf_exempt
def MunicipioAdd(request):
    if request.method == 'POST':
        provincia = request.POST['id']
        nombre = request.POST['nombre']
        nuevo = Municipio(nombre=nombre, provincia_id=provincia)
        nuevo.save()
        return HttpResponse('')
    else:
        return redirect(reverse_lazy('municipio_list'))


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
        return HttpResponse('')


@login_required
@csrf_exempt
def InstitucionUpdate(request, pk):
    if request.method == 'POST':
        institucion = Institucion.objects.get(pk=pk)
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        institucion.nombre = nombre
        institucion.direccion = direccion
        institucion.save()
        return HttpResponse('')
    else:
        return redirect(reverse_lazy('instituciones_list'))

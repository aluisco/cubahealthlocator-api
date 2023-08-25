from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DeleteView
from core.models import Provincia


@login_required
def dashboard(request):
    return render(template_name='dashboard/dashboard.html', request=request)


def error_404_view(request, exception=None):
    return render(request, '404.html')


def error_500_view(request, exception=None):
    return render(request, '500.html')


class ProvinciaListView(LoginRequiredMixin, ListView):
    model = Provincia
    template_name = "provincia/provincia_list.html"

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

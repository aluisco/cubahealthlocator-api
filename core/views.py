from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):
    return render(template_name='dashboard/dashboard.html', request=request)


def logout_view(request):
    logout(request)

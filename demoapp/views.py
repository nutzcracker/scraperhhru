from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from .models import Job
import datetime
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt


class MainView(View):

    def get(self, request, *args, **kwargs):
        jobs = Job.objects.all()
        json = {}

        return render(
            request,'demoapp/home.html', context={'jobs': jobs})

@csrf_exempt
def filter_view(request):
    data = []
    if request.method == 'POST':
        time = request.POST.get('time')
        limit = datetime.datetime.now() - datetime.timedelta(hours=int(time))
        new_jobs = Job.objects.filter(created_date__gt=limit)
        for job in new_jobs:
            data.append(model_to_dict(job))
        return JsonResponse({'jobs':data}, safe=False)

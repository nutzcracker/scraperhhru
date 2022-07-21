from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from .models import Job
from datetime import datetime
from django.http import JsonResponse


class MainView(View):

    def get(self, request, *args, **kwargs):
        jobs = Job.objects.all()
        json = {}

        return render(request,'demoapp/home.html', context={'jobs': jobs}
        )

def Filter(request):
        if request.method == 'GET':
            time = request.GET.get('time')
            limit = datetime.datetime.now() - datetime.timedelta(hours=time)
            new_jobs = Job.objects.filter(created_date_gt=limit)
            data.append({'njobs':new_jobs})
        return JsonResponse(data)
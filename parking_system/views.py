from django.shortcuts import render

from .models import Slot,Floor


def home(request):
    floors = Floor.objects.all().prefetch_related('slots')
    # import pdb
    # pdb.set_trace()
    return render(request,'parking_system/home.html',{'floor':floors})

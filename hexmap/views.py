from django.http import JsonResponse
from django.shortcuts import render
from django.forms.models import model_to_dict

from .models import *

def region_to_dict(region):
    data = {}
    data['coordinates'] = {'x':region.coordinate.x, 'y':region.coordinate.y, 'z':region.coordinate.z}
    data['name'] = region.name
    data['type'] = region.region_type.name
    return data


def region_detail_json(request, pk):
    #qs = Region.objects.filter(pk=pk).values()
    #return JsonResponse({'region':list(qs)})
    qs = Region.objects.filter(pk=pk)
    region_list = []
    for item in qs:
        region_list.append(region_to_dict(item))
    return JsonResponse({'region':region_list})
    
def region_list_json(request):
    qs = Region.objects.all()
    region_list = []
    for item in qs:
        region_list.append(region_to_dict(item))
    return JsonResponse({'region':region_list})
    

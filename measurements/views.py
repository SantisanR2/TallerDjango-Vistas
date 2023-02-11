from .logic import measurements_logic as ml
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def measurments_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurment_dto = ml.get_measurment(id)
            measurment = serializers.serialize('json', [measurment_dto,])
            return HttpResponse(measurment, 'application/json')
        else:
            measurments_dto = ml.get_measurments()
            measurments = serializers.serialize('json', measurments_dto)
            return HttpResponse(measurments, 'application/json')

    if request.method == 'POST':
        measurment_dto = ml.create_measurment(json.loads(request.body))
        measurment = serializers.serialize('json', [measurment_dto,])
        return HttpResponse(measurment, 'application/json')

@csrf_exempt
def measurment_view(request, pk):
    if request.method == 'GET':
        measurment_dto = ml.get_measurment(pk)
        measurment = serializers.serialize('json', [measurment_dto,])
        return HttpResponse(measurment, 'application/json')

    if request.method == 'PUT' or request.method == 'PATCH':
        measurment_dto = ml.update_measurment(pk, json.loads(request.body))
        measurment = serializers.serialize('json', [measurment_dto,])
        return HttpResponse(measurment, 'application/json')
    
    if request.method == 'DELETE':
        ml.delete_measurment(pk)
        return HttpResponse(status=204)
from .logic import measurements_logic as ml
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get('id',None)
        if id:
            measurment_dto = ml.get_measurement(id)
            measurment = serializers.serialize('json', [measurment_dto,])
            return HttpResponse(measurment, 'application/json')

        else:
            measurments_dto = ml.get_measurements()
            measurments = serializers.serialize('json', measurments_dto)
            return HttpResponse(measurments, 'application/json')

    if request.method == 'POST':
        measurment_dto = ml.create_measurement(json.loads(request.body))
        measurment = serializers.serialize(json, [measurment_dto,])
        return HttpResponse(measurment, 'application/json')

@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        measurment_dto = ml.get_measurement(pk)
        measurment = serializers.serialize('json', [measurment_dto,])
        return HttpResponse(measurment, 'application/json')

def update_measurement(request, pk):
    if request.method == 'PUT':
        measurment_dto = ml.update_measurement(pk, json.loads(request.body))
        measurment = serializers.serialize('json', [measurment_dto,])
        return HttpResponse(measurment, 'application/json')

def delete_measurement(request, pk):
    if request.method == 'DELETE':
        measurment_dto = ml.delete_measurement(pk)
        measurment = serializers.serialize('json', [measurment_dto,])
        return HttpResponse(measurment, 'application/json')

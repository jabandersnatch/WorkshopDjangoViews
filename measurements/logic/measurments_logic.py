from ..models import Measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(mes_pk:int)->Measurement:
    measurment = Measurement.objects.get(pk=var_pk)
    return measurment
def update_variable(mes_pk:int, new_mes):
    variable = get_measurement(mes_pk)
    variable

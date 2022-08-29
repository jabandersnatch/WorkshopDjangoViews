from ..models import Measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(mes_pk:int)->Measurement:
    measurment = Measurement.objects.get(pk=mes_pk)
    return measurment

def update_measurement(mes_pk:int, new_mes)->Measurement:
    measurment = get_measurement(mes_pk)
    measurment.variable= new_mes["variable"]
    measurment.value = new_mes["value"]
    measurment.unit = new_mes["unit"]
    measurment.place = new_mes["place"]
    measurment.dateTime = new_mes["dateTime"]
    measurment.save()
    return measurment

def create_measurement(mes)->Measurement:
    measurment = Measurement(
        variable=mes["variable"],
        value = mes["value"],
        unit = mes["unit"],
        place = mes["place"],
        dateTime = mes["dateTime"]
        )
    measurment.save()
    return measurment

def delete_measurement(mes_pk:int):
    measurment = get_measurement(mes_pk)
    measurment.delete()
    return measurment

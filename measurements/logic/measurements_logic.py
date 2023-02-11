from ..models import Measurement
from variables.logic.variables_logic import get_variable

def get_measurments():
    measurments = Measurement.objects.all()
    return measurments

def get_measurment(var_pk):
    measurment = Measurement.objects.get(pk=var_pk)
    return measurment

def update_measurment(var_pk, new_var):
    measurment = get_measurment(var_pk)
    measurment.variable = get_variable(new_var["variable"])
    measurment.value = new_var["value"]
    measurment.unit = new_var["unit"]
    measurment.place = new_var["place"]
    measurment.save()
    return measurment

def create_measurment(var):
    measurment = Measurement(variable=get_variable(var["variable"]), value=var["value"], unit=var["unit"], place=var["place"])
    measurment.save()
    return measurment

def delete_measurment(var_pk):
    measurment = get_measurment(var_pk)
    measurment.delete()
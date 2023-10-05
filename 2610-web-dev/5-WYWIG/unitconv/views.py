from django.http import JsonResponse, QueryDict
from django.shortcuts import render
from .models import unitconv

# does calculations from db
def helper(fromType, toType, value):
    startUnit = unitconv.objects.get(abbreviation=fromType)
    endUnit = unitconv.objects.get(abbreviation=toType)
    conversionFactor = float(startUnit.conversionFactor)
    weightInToz = float(value) * (1 / conversionFactor)
    return weightInToz * float(endUnit.conversionFactor)

# responds to requests of the form 'convert?from=lb&to=t_oz&value=3.14159'
def convert(request):
    context = {}

    # check to make sure all parameters are there
    if 'from' not in request.GET or 'to' not in request.GET or 'value' not in request.GET:
        context['error'] = 'Invalid unit conversion request'
    else:
        # get values from request
        fromType = request.GET['from'] # from is a string which identifies the type of units the input value represents
        toType = request.GET['to'] # to is a string representing the type of units the user wants value converted into
        value = request.GET['value'] # value is a floating-point number representing the number of from units

        # error checking values
        fromTypeValid = False
        toTypeValid = False
        valueTypeValid = False
        # check unit types
        unitTypes = ['T', 'g', 't_oz', 'kg', 'lb', 'oz']
        for unit in unitTypes:
            if fromType == unit:
                fromTypeValid = True
            if toType == unit:
                toTypeValid = True
        # check for valid float
        try:
            float(value)
            if float(value) > 0:
                valueTypeValid = True
            else:
                valueTypeValid = False
        except ValueError:
            valueTypeValid = False

        # appropriate response
        if not fromTypeValid or not toTypeValid or not valueTypeValid: # responses were not valid types
            context['error'] = 'Invalid unit conversion request'
        else:
            context['units'] = toType
            context['value'] = helper(fromType, toType, value)

    # return json response
    return JsonResponse(context)
# from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse
# from .serializers import EmployeeSerializer
# from .models import Employee
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from rest_framework import status
# # Create your views here.

# @csrf_exempt
# def employeeListView(request):
#     if request.method == 'GET':
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         jsondata = JSONParser().parse(request)
#         serializer = EmployeeSerializer(data=jsondata)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe=False)
#         else:
#             return JsonResponse(serializer.errors, safe=False)
#         # return JsonResponse({'message': 'POST Request'})

# @csrf_exempt
# def employeeDetailView(request, pk):
#     try:
#         employee = Employee.objects.get(pk=pk)
#         # return JsonResponse({'message': 'Employee was retrieved successfully!'})
#     except Employee.DoesNotExist:
#         return JsonResponse({'message': 'The employee does not exist'})
    
#     if request.method == 'GET':
#         serializer = EmployeeSerializer(employee)
#         return JsonResponse(serializer.data, safe=False)
#         # pass
    
#     elif request.method == 'PUT':
#         jsondata = JSONParser().parse(request)
#         serializer = EmployeeSerializer(employee, data=jsondata)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe=False)
#         else:
#             return JsonResponse(serializer.errors, safe=False)
#         # pass
        
#     elif request.method == 'DELETE':
#         employee.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
#         # return JsonResponse({'message': 'Employee was deleted successfully!'})
#         # pass




from django.shortcuts import render
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET', 'POST'])
def employeeListView(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # jsondata = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        # return JsonResponse({'message': 'POST Request'})


@api_view(['GET', 'PUT', 'DELETE'])
def employeeDetailView(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        print(employee)
        # return JsonResponse({'message': 'Employee was retrieved successfully!'})
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
        # pass
    
    elif request.method == 'PUT':
        # jsondata = JSONParser().parse(request)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        # pass
        
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # return JsonResponse({'message': 'Employee was deleted successfully!'})
        # pass
# from .models import Employee
# from rest_framework import serializers

# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         name = serializers.CharField(max_length=30)
#         email = serializers.EmailField()
#         password = serializers.CharField(max_length=30)
#         phone = serializers.CharField(max_length=10)
from .models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = ['name', 'email', 'password', 'phone']
        fields = '__all__'

        
    # def create(self, validated_data):
    #     return Employee.objects.create(**validated_data)
    
    # def update(self, employee, validated_data):
    #     # employee.name = validated_data.get('name', employee.name)
    #     # employee.email = validated_data.get('email', employee.email)
    #     # employee.password = validated_data.get('password', employee.password)
    #     # employee.phone = validated_data.get('phone', employee.phone)
    #     newEmployee = Employee(**validated_data)
    #     newEmployee.id = employee.id
    #     newEmployee.save()
    #     # employee.save()
    #     return newEmployee

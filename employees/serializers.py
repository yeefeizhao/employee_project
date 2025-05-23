from rest_framework import serializers 
from .models import Employee, Department, Performance

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), source='department', write_only=True
    )

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'phone', 'address', 'date_of_joining', 'department', 'department_id']

class PerformanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), source='employee', write_only=True
    )

    class Meta:
        model = Performance
        fields = ['id', 'employee', 'employee_id', 'rating', 'review_date']
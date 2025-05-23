from rest_framework import serializers
from .models import Attendance
from employees.serializers import EmployeeSerializer
from employees.models import Employee

class AttendanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), source='employee', write_only=True
    )

    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'employee_id', 'date', 'status']
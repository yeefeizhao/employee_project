from django.shortcuts import render
from rest_framework import viewsets
from attendance.models import Attendance
from .serializers import AttendanceSerializer
from django_filters.rest_framework import DjangoFilterBackend

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employee__id', 'date', 'status']

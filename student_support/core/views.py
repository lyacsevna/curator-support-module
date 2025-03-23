from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Activity, FinancialSupport, Grade, Dormitory, Penalty
from .serializers import StudentSerializer, ActivitySerializer, FinancialSupportSerializer, GradeSerializer, DormitorySerializer, PenaltySerializer

def home(request):
    return render(request, 'home.html')

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class FinancialSupportViewSet(viewsets.ModelViewSet):
    queryset = FinancialSupport.objects.all()
    serializer_class = FinancialSupportSerializer


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class DormitoryViewSet(viewsets.ModelViewSet):
    queryset = Dormitory.objects.all()
    serializer_class = DormitorySerializer


class PenaltyViewSet(viewsets.ModelViewSet):
    queryset = Penalty.objects.all()
    serializer_class = PenaltySerializer

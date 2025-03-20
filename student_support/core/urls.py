from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, ActivityViewSet, FinancialSupportViewSet, GradeViewSet, DormitoryViewSet, PenaltyViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'financial-support', FinancialSupportViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'dormitories', DormitoryViewSet)
router.register(r'penalties', PenaltyViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
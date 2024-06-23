from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['education', 'hospital', 'specialty']
    search_fields = ['license_number']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.object.all()
    serializers_class = MedicalRecordSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.object.all()
    serializers_class = AppointmentSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.object.all()
    serializers_class = MedicationSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FitnessProgramViewSet(viewsets.ModelViewSet):
    queryset = FitnessProgram.object.all()
    serializers_class = FitnessProgramSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.object.all()
    serializers_class = NotificationSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
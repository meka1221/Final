from rest_framework import serializers
from .models import *


class DoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class MedicalRecordSerializers(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'


class AppointmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class MedicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'


class FitnessProgramSerializers(serializers.ModelSerializer):
    class Meta:
        model = FitnessProgram
        fields = '__all__'


class NotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

from .models import Doctor
from modeltranslation.translator import register, TranslationOptions


@register(Doctor)
class DoctorTranslationOptions(TranslationOptions):
    fields = ('speciality', 'education', 'hospital')


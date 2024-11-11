from modeltranslation.translator import translator, TranslationOptions
from .models import *

class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

translator.register(Services, ServiceTranslationOptions)

class StagesTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

translator.register(Stages, StagesTranslationOptions)

class ServicesDescript2TranslationOptions(TranslationOptions):
    fields = ('name','description')

translator.register(ServicesDescript2, ServicesDescript2TranslationOptions)

class ProjectsTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

translator.register(Projects, ProjectsTranslationOptions)

class AboutDescriptionTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

translator.register(AboutDescription, AboutDescriptionTranslationOptions)

class FeedbackTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

translator.register(Feedback, FeedbackTranslationOptions)


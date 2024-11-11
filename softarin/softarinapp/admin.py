from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
# Register your models here.
from .models import *



admin.site.register(Services)
# admin.site.register(ServicesImages)
admin.site.register(ServicesDescript2)
admin.site.register(Projects)
# admin.site.register(AboutDescription)
admin.site.register(Feedback)
admin.site.register(Contact)
admin.site.register(Stages)


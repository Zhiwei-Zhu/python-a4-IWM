from django.contrib import admin

from .models import Questions
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fields = ['text']

admin.site.register(Questions)